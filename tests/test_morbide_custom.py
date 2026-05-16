from calculators.morbide_custom import SoftLensInput, calculate_soft_lens


def test_toric_example():
    params = SoftLensInput(
        k_flat_mm=7.80,
        k_steep_mm=7.55,
        hvid_mm=11.80,
        sphere_spectacle=-3.75,
        cyl_spectacle=-1.25,
        axis=180,
        lens_type="torica",
        material_group="definitive65_74",
        ocular_sag_um=3600,
    )
    out = calculate_soft_lens(params)
    assert out.td_mm == 14.0
    assert out.bc_mm == 8.70
    assert out.sag_target_min_um == 3720
    assert out.sag_target_max_um == 3880


def test_bitoric_internal_toricity_present():
    params = SoftLensInput(
        k_flat_mm=7.65,
        k_steep_mm=7.20,
        hvid_mm=11.70,
        sphere_spectacle=-5.50,
        cyl_spectacle=-2.75,
        axis=95,
        lens_type="bitorica",
        material_group="definitive65_74",
    )
    out = calculate_soft_lens(params)
    assert out.internal_toricity_mm is not None
    assert out.internal_toricity_mm >= 0.20


def test_spherical_no_axis_required():
    params = SoftLensInput(
        k_flat_mm=7.90,
        k_steep_mm=7.80,
        hvid_mm=11.60,
        sphere_spectacle=-2.00,
        lens_type="sferica",
        material_group="benz_g3x_g4x_hydro49",
    )
    out = calculate_soft_lens(params)
    assert out.cyl_cl == 0.0
    assert out.axis is None
