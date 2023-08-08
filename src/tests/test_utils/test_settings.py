from core.settings import Settings

def test_settings(settings: Settings):
    assert settings.mongo_uri is not None
    assert settings.db_name is not None
    