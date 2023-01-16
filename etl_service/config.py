from pydantic import BaseSettings


class Settings(BaseSettings):
    tenant_id: str
    client_secret: str
    vault_url: str

    class Config:
        env_file = ".env"


settings = Settings()
