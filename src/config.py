"""Single source of truth for all configuration."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Anthropic
    anthropic_api_key: str
    anthropic_model_id: str = "claude-opus-4-6"
    anthropic_region: str = "us-east-1"

    # Postgres / pgvector
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "governed_agent"
    postgres_user: str = "postgres"
    postgres_password: str = "changeme"

    # App
    log_level: str = "INFO"
    embed_batch_size: int = 100
    retrieval_top_k: int = 5

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
