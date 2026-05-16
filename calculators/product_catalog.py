from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Optional, Literal


Indication = Literal[
    "cornea_regolare",
    "cornea_irregolare",
    "cheratocono",
    "prismatica",
    "multifocale",
    "controllo_miopia",
    "terapeutica",
    "filtrante",
]


@dataclass(frozen=True)
class ParameterRange:
    min_value: float
    max_value: float
    step: Optional[float] = None
    unit: str = ""

    def contains(self, value: Optional[float]) -> bool:
        if value is None:
            return True
        return self.min_value <= value <= self.max_value

    def label(self) -> str:
        step = f" step {self.step:g}" if self.step else ""
        return f"{self.min_value:g}-{self.max_value:g} {self.unit}{step}".strip()


@dataclass(frozen=True)
class ProductSpec:
    name: str
    manufacturer: str
    indications: tuple[Indication, ...]
    geometry: str
    replacement: str
    materials: tuple[str, ...]
    bc_range: Optional[ParameterRange]
    dia_range: Optional[ParameterRange]
    sphere_range: Optional[ParameterRange]
    cyl_range: Optional[ParameterRange]
    add_range: Optional[ParameterRange] = None
    prism_range: Optional[ParameterRange] = None
    notes: str = ""

    def to_dict(self) -> dict:
        data = asdict(self)
        return data


@dataclass
class ProductQuery:
    indication: Indication
    bc_mm: Optional[float] = None
    dia_mm: Optional[float] = None
    sphere_d: Optional[float] = None
    cyl_d: Optional[float] = None
    add_d: Optional[float] = None
    prism_d: Optional[float] = None
    prefer_silicone_hydrogel: bool = False


@dataclass
class ProductMatch:
    product: ProductSpec
    score: int
    warnings: list[str]
    reasons: list[str]

    def to_dict(self) -> dict:
        return {
            "product": self.product.to_dict(),
            "score": self.score,
            "warnings": self.warnings,
            "reasons": self.reasons,
        }


MEDLAC_PRODUCTS: tuple[ProductSpec, ...] = (
    ProductSpec(
        name="MED 02 PRISMA / SOFT BITORIC",
        manufacturer="MedLac",
        indications=("cornea_regolare",),
        geometry="morbida bitorica ad aberrazioni compensate",
        replacement="2 mesi",
        materials=("BENZ G3X", "BENZ G4X", "CONTAFLEX 67", "HYDRO 49"),
        bc_range=ParameterRange(7.30, 9.50, 0.10, "mm"),
        dia_range=ParameterRange(13.40, 15.20, 0.10, "mm"),
        sphere_range=ParameterRange(-30.00, 30.00, 0.25, "D"),
        cyl_range=ParameterRange(-8.00, -0.50, 0.25, "D"),
        notes="Indicata quando serve stabilizzazione torica/bitorica custom su cornea regolare.",
    ),
    ProductSpec(
        name="MED PRISMODIREZIONALE",
        manufacturer="MedLac",
        indications=("prismatica",),
        geometry="morbida specialist per correzioni prismatiche",
        replacement="trimestrale",
        materials=("G4X DK 23",),
        bc_range=ParameterRange(6.00, 9.00, 0.01, "mm"),
        dia_range=ParameterRange(11.00, 15.00, 0.01, "mm"),
        sphere_range=ParameterRange(-20.00, 20.00, 0.25, "D"),
        cyl_range=ParameterRange(-5.00, -0.25, 0.25, "D"),
        prism_range=ParameterRange(0.50, 5.00, 0.50, "Dpt"),
        notes="Prodotto specialistico per lievi/medie deviazioni; richiede controllo della base prismatica.",
    ),
    ProductSpec(
        name="MED MULTIVISION SOFT",
        manufacturer="MedLac",
        indications=("multifocale", "cornea_regolare"),
        geometry="morbida multifocale centro vicino / centro lontano / opzione DEC",
        replacement="2-12 mesi secondo variante",
        materials=("BENZ G3X", "BENZ G4X", "BENZ G5X", "DEFINITIVE 74"),
        bc_range=ParameterRange(7.30, 9.80, 0.05, "mm"),
        dia_range=ParameterRange(13.80, 15.00, 0.10, "mm"),
        sphere_range=ParameterRange(-30.00, 30.00, 0.25, "D"),
        cyl_range=ParameterRange(-6.00, -0.50, 0.25, "D"),
        add_range=ParameterRange(0.50, 3.50, 0.25, "D"),
        notes="Per presbiopia; valutare dominanza, centratura e possibile decentramento ottico DEC.",
    ),
    ProductSpec(
        name="MED CONTROL",
        manufacturer="MedLac",
        indications=("controllo_miopia",),
        geometry="morbida biasferica con defocus periferico",
        replacement="2 mesi",
        materials=("DEFINITIVE 74", "ULTRAPERM 74"),
        bc_range=ParameterRange(7.30, 9.50, 0.05, "mm"),
        dia_range=ParameterRange(13.40, 15.20, 0.10, "mm"),
        sphere_range=ParameterRange(-20.00, -1.00, 0.25, "D"),
        cyl_range=ParameterRange(-6.00, -0.50, 0.25, "D"),
        notes="Tre profili di defocus: junior, regular, large. Richiede follow-up progressione miopica.",
    ),
    ProductSpec(
        name="MED CONUS / KERATOPLUS",
        manufacturer="MedLac",
        indications=("cornea_irregolare", "cheratocono"),
        geometry="morbida per cheratocono con geometria interna sfero-asferica",
        replacement="3-6 mesi secondo variante",
        materials=("DEFINITIVE 65", "HYDRO 59"),
        bc_range=ParameterRange(7.30, 9.50, 0.05, "mm"),
        dia_range=ParameterRange(13.40, 15.20, 0.10, "mm"),
        sphere_range=ParameterRange(-30.00, 10.00, 0.25, "D"),
        cyl_range=ParameterRange(-8.00, -0.50, 0.25, "D"),
        notes="Prima opzione morbida custom quando si cerca comfort su cornea irregolare/cheratocono selezionato.",
    ),
    ProductSpec(
        name="MED BIOPROTECT",
        manufacturer="MedLac",
        indications=("terapeutica",),
        geometry="morbida terapeutica ad ampio diametro",
        replacement="2 mesi",
        materials=("ULTRAPERM 74",),
        bc_range=ParameterRange(8.60, 8.60, 0.10, "mm"),
        dia_range=ParameterRange(16.50, 16.50, None, "mm"),
        sphere_range=ParameterRange(-20.00, 20.00, 0.25, "D"),
        cyl_range=None,
        notes="Uso terapeutico/protettivo; eventuale porto prolungato solo secondo indicazione e controllo medico.",
    ),
    ProductSpec(
        name="MED FILTER / MED FILTER TORIC",
        manufacturer="MedLac",
        indications=("filtrante",),
        geometry="morbida colorata filtrante",
        replacement="semestrale",
        materials=("HYDRO 49", "HEMA 38", "BENZ G3X", "BENZ G5X"),
        bc_range=ParameterRange(7.50, 9.50, 0.10, "mm"),
        dia_range=ParameterRange(11.00, 14.80, 0.10, "mm"),
        sphere_range=ParameterRange(-30.00, 30.00, 0.25, "D"),
        cyl_range=ParameterRange(-6.00, -0.50, 0.25, "D"),
        notes="Per necessità filtranti, fotofobia, contrasto o estetica; selezionare diametro zona filtro.",
    ),
)


def _range_check(label: str, spec_range: Optional[ParameterRange], value: Optional[float]) -> tuple[int, Optional[str], Optional[str]]:
    if value is None or spec_range is None:
        return 0, None, None
    if spec_range.contains(value):
        return 1, f"{label} nel range {spec_range.label()}.", None
    return -3, None, f"{label} {value:g} fuori range {spec_range.label()}."


def select_products(query: ProductQuery, products: tuple[ProductSpec, ...] = MEDLAC_PRODUCTS) -> list[ProductMatch]:
    matches: list[ProductMatch] = []
    for product in products:
        if query.indication not in product.indications:
            continue

        score = 10
        reasons = [f"Indicazione compatibile: {query.indication}."]
        warnings: list[str] = []

        for label, spec_range, value in (
            ("BC", product.bc_range, query.bc_mm),
            ("DIA", product.dia_range, query.dia_mm),
            ("Sfera", product.sphere_range, query.sphere_d),
            ("Cilindro", product.cyl_range, query.cyl_d),
            ("Addizione", product.add_range, query.add_d),
            ("Prisma", product.prism_range, query.prism_d),
        ):
            delta, reason, warning = _range_check(label, spec_range, value)
            score += delta
            if reason:
                reasons.append(reason)
            if warning:
                warnings.append(warning)

        if query.prefer_silicone_hydrogel:
            if any("DEFINITIVE" in m or "ULTRAPERM" in m for m in product.materials):
                score += 2
                reasons.append("Preferenza SiHy/alta permeabilità compatibile con materiali disponibili.")
            else:
                warnings.append("Preferenza SiHy non evidente nei materiali elencati per questo prodotto.")

        matches.append(ProductMatch(product=product, score=score, warnings=warnings, reasons=reasons))

    return sorted(matches, key=lambda item: item.score, reverse=True)
