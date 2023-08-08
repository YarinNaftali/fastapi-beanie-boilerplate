from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    mongo_uri: str = Field(env="MONGO_URI")
    db_name: str = Field(env="DB_NAME")

    class Config:
        env_file = "..\.env"
        env_file_encoding = "utf-8"