from core.schemas.category import Category

def test_category(category_chocolate_fixture: Category):
    assert category_chocolate_fixture.name == "Chocolate"
    assert category_chocolate_fixture.description == "A preparation of roasted and ground cacao seeds."