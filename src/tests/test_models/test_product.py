from core.models.product import Product

def test_product_marsbar(product_marsbar_fixture: Product):
    assert product_marsbar_fixture.name == "Mars"
    assert product_marsbar_fixture.price == 1.0
    assert product_marsbar_fixture.category.name == "Chocolate"
    assert product_marsbar_fixture.category.description == "A preparation of roasted and ground cacao seeds."

def test_product_tonybar(product_tonybar_fixture: Product):
    assert product_tonybar_fixture.name == "Tony's"
    assert product_tonybar_fixture.price == 5.95
    assert product_tonybar_fixture.category.name == "Chocolate"
    assert product_tonybar_fixture.category.description == "A preparation of roasted and ground cacao seeds."

