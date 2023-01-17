from pydantic import BaseSettings


class Settings(BaseSettings):
    client_id: str
    tenant_id: str
    client_secret: str
    vault_url: str

    class Config:
        env_file = ".env"


settings = Settings()
