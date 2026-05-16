from calculators.product_catalog import ProductQuery, select_products


def test_select_keratoconus_returns_med_conus():
    query = ProductQuery(
        indication="cheratocono",
        bc_mm=8.10,
        dia_mm=14.50,
        sphere_d=-6.00,
        cyl_d=-2.50,
        prefer_silicone_hydrogel=True,
    )
    matches = select_products(query)
    assert matches
    assert matches[0].product.name == "MED CONUS / KERATOPLUS"
    assert matches[0].score > 0


def test_select_prismatic_checks_prism_range():
    query = ProductQuery(
        indication="prismatica",
        bc_mm=8.20,
        dia_mm=14.00,
        sphere_d=-1.00,
        cyl_d=-1.00,
        prism_d=3.00,
    )
    matches = select_products(query)
    assert matches[0].product.name == "MED PRISMODIREZIONALE"
    assert not any("Prisma" in warning for warning in matches[0].warnings)


def test_out_of_range_generates_warning():
    query = ProductQuery(
        indication="filtrante",
        dia_mm=16.00,
    )
    matches = select_products(query)
    assert matches
    assert any("DIA" in warning for warning in matches[0].warnings)
