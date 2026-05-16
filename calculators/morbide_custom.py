from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Optional, Literal, Dict, Any
import math


LensType = Literal["sferica", "torica", "bitorica"]
MaterialGroup = Literal[
    "benz_g3x_g4x_hydro49",
    "contaflex67_ultraperm74_g72hw",
    "definitive65_74",
]


@dataclass
class SoftLensInput:
    k_flat_mm: float
    k_steep_mm: float
    hvid_mm: float
    sphere_spectacle: float
    cyl_spectacle: float = 0.0
    axis: Optional[int] = None
    vertex_distance_mm: float = 12.0
    lens_type: LensType = "sferica"
    material_group: MaterialGroup = "definitive65_74"
    ocular_sag_um: Optional[float] = None
    notes: str = ""


@dataclass
class SoftLensOutput:
    lens_type: str
    material_group: str
    td_mm: float
    bc_mm: float
    sphere_cl: float
    cyl_cl: float
    axis: Optional[int]
    internal_toricity_mm: Optional[float]
    corneal_astigmatism_d: float
    sag_target_min_um: Optional[float]
    sag_target_max_um: Optional[float]
    warnings: list[str]
    rationale: list[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# Offset BC da Ks secondo tabella MedLac caricata nel progetto.
# Chiave: lens_type -> fascia TD -> gruppo materiale -> offset mm.
BC_OFFSETS = {
    "sferica": [
        (0.0, 13.40, {"benz_g3x_g4x_hydro49": 0.60, "contaflex67_ultraperm74_g72hw": 0.70, "definitive65_74": 0.50}),
        (13.50, 13.90, {"benz_g3x_g4x_hydro49": 0.70, "contaflex67_ultraperm74_g72hw": 0.80, "definitive65_74": 0.60}),
        (14.00, 14.40, {"benz_g3x_g4x_hydro49": 0.90, "contaflex67_ultraperm74_g72hw": 1.00, "definitive65_74": 0.80}),
        (14.50, 14.90, {"benz_g3x_g4x_hydro49": 1.10, "contaflex67_ultraperm74_g72hw": 1.20, "definitive65_74": 1.00}),
        (15.00, 99.00, {"benz_g3x_g4x_hydro49": 1.20, "contaflex67_ultraperm74_g72hw": 1.30, "definitive65_74": 1.10}),
    ],
    "torica": [
        (0.0, 13.40, {"benz_g3x_g4x_hydro49": 0.70, "contaflex67_ultraperm74_g72hw": 0.80, "definitive65_74": 0.60}),
        (13.50, 13.90, {"benz_g3x_g4x_hydro49": 0.80, "contaflex67_ultraperm74_g72hw": 0.90, "definitive65_74": 0.70}),
        (14.00, 14.40, {"benz_g3x_g4x_hydro49": 1.00, "contaflex67_ultraperm74_g72hw": 1.10, "definitive65_74": 0.90}),
        (14.50, 14.90, {"benz_g3x_g4x_hydro49": 1.20, "contaflex67_ultraperm74_g72hw": 1.30, "definitive65_74": 1.10}),
        (15.00, 99.00, {"benz_g3x_g4x_hydro49": 1.30, "contaflex67_ultraperm74_g72hw": 1.40, "definitive65_74": 1.20}),
    ],
    "bitorica": [
        (0.0, 13.40, {"benz_g3x_g4x_hydro49": 0.70, "contaflex67_ultraperm74_g72hw": 0.80, "definitive65_74": 0.60}),
        (13.50, 13.90, {"benz_g3x_g4x_hydro49": 0.80, "contaflex67_ultraperm74_g72hw": 0.90, "definitive65_74": 0.70}),
        (14.00, 14.40, {"benz_g3x_g4x_hydro49": 1.00, "contaflex67_ultraperm74_g72hw": 1.10, "definitive65_74": 0.90}),
        (14.50, 14.90, {"benz_g3x_g4x_hydro49": 1.20, "contaflex67_ultraperm74_g72hw": 1.30, "definitive65_74": 1.10}),
        (15.00, 99.00, {"benz_g3x_g4x_hydro49": 1.30, "contaflex67_ultraperm74_g72hw": 1.40, "definitive65_74": 1.20}),
    ],
}


def round_quarter(x: float) -> float:
    return round(x * 4) / 4


def round_step(x: float, step: float) -> float:
    value = round(x / step) * step
    # Evita artefatti floating-point tipo 8.700000000000001.
    return round(value, 2)


def vertex_convert(power_d: float, vertex_mm: float) -> float:
    """Convert spectacle-plane power to corneal-plane CL power."""
    d_m = vertex_mm / 1000.0
    return power_d / (1 - d_m * power_d)


def radius_mm_to_d(radius_mm: float, refractive_index: float = 1.3375) -> float:
    """Keratometric diopters from radius in mm."""
    return (refractive_index - 1.0) / (radius_mm / 1000.0)


def select_td(hvid_mm: float, lens_type: LensType) -> float:
    add = 2.00 if lens_type == "sferica" else 2.20
    return round_step(hvid_mm + add, 0.10)


def select_bc(k_flat_mm: float, td_mm: float, lens_type: LensType, material_group: MaterialGroup) -> float:
    for low, high, offsets in BC_OFFSETS[lens_type]:
        if low <= td_mm <= high:
            return round_step(k_flat_mm + offsets[material_group], 0.05)
    raise ValueError(f"TD fuori range tabellare: {td_mm}")


def estimate_internal_toricity(k_flat_mm: float, k_steep_mm: float) -> Optional[float]:
    """Indicazione per morbida bitorica: 0.20 mm fino a 2.00 D di astigmatismo corneale,
    poi +0.10 mm per ogni 1.00 D oltre 2.00 D.
    """
    k_flat_d = radius_mm_to_d(k_flat_mm)
    k_steep_d = radius_mm_to_d(k_steep_mm)
    corneal_astig_d = abs(k_steep_d - k_flat_d)
    if corneal_astig_d <= 2.00:
        return 0.20
    extra = math.ceil(corneal_astig_d - 2.00)
    return round_step(0.20 + 0.10 * extra, 0.10)


def calculate_soft_lens(params: SoftLensInput) -> SoftLensOutput:
    warnings: list[str] = []
    rationale: list[str] = []

    if params.k_flat_mm <= 0 or params.k_steep_mm <= 0:
        raise ValueError("K in mm non valido.")
    if params.hvid_mm <= 0:
        raise ValueError("HVID non valido.")
    if params.lens_type in ("torica", "bitorica") and params.axis is None:
        warnings.append("Asse mancante: necessario per ordine torico/bitorico.")

    td = select_td(params.hvid_mm, params.lens_type)
    bc = select_bc(params.k_flat_mm, td, params.lens_type, params.material_group)

    # Conversione al piano corneale dei meridiani principali.
    sphere_cl = round_quarter(vertex_convert(params.sphere_spectacle, params.vertex_distance_mm))
    cyl_cl = 0.0
    if abs(params.cyl_spectacle) >= 0.25 and params.lens_type in ("torica", "bitorica"):
        meridian_sphere = params.sphere_spectacle
        meridian_plus_cyl = params.sphere_spectacle + params.cyl_spectacle
        cl_sphere_meridian = vertex_convert(meridian_sphere, params.vertex_distance_mm)
        cl_plus_cyl_meridian = vertex_convert(meridian_plus_cyl, params.vertex_distance_mm)
        sphere_cl = round_quarter(cl_sphere_meridian)
        cyl_cl = round_quarter(cl_plus_cyl_meridian - cl_sphere_meridian)

    k_flat_d = radius_mm_to_d(params.k_flat_mm)
    k_steep_d = radius_mm_to_d(params.k_steep_mm)
    corneal_astig_d = round(abs(k_steep_d - k_flat_d), 2)

    internal_toricity = None
    if params.lens_type == "bitorica":
        internal_toricity = estimate_internal_toricity(params.k_flat_mm, params.k_steep_mm)

    sag_min = sag_max = None
    if params.ocular_sag_um is not None:
        sag_min = round(params.ocular_sag_um + 120, 0)
        sag_max = round(params.ocular_sag_um + 280, 0)
        rationale.append("Target sagittale: CL-SAG circa OC-SAG + 120/280 µm, se misurazione affidabile.")
    else:
        warnings.append("OC-SAG non disponibile: validare fitting con centraggio, movimento, push-up e biomicroscopia.")

    rationale.append(f"TD calcolato da HVID: {params.hvid_mm:.2f} + {'2.00' if params.lens_type == 'sferica' else '2.20'} mm.")
    rationale.append(f"BC calcolata da Ks/K piatto {params.k_flat_mm:.2f} mm + offset tabellare per materiale/diametro.")
    rationale.append("Potere convertito al piano corneale con distanza apice dichiarata.")

    if params.lens_type == "bitorica":
        rationale.append("Toricità interna stimata secondo astigmatismo corneale: 0.20 mm fino a 2.00 D, poi incremento progressivo.")

    return SoftLensOutput(
        lens_type=params.lens_type,
        material_group=params.material_group,
        td_mm=td,
        bc_mm=bc,
        sphere_cl=sphere_cl,
        cyl_cl=cyl_cl,
        axis=params.axis,
        internal_toricity_mm=internal_toricity,
        corneal_astigmatism_d=corneal_astig_d,
        sag_target_min_um=sag_min,
        sag_target_max_um=sag_max,
        warnings=warnings,
        rationale=rationale,
    )
