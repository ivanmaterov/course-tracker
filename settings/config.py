import secrets
from typing import Any, List, Optional, Union

from pydantic import (
    AnyHttpUrl,
    HttpUrl,
    PostgresDsn,
    ValidationInfo,
    field_validator,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl]

    @field_validator('BACKEND_CORS_ORIGINS', mode='before')
    def assemble_cors_origins(
        cls,
        value: Union[str, List[str]],
    ) -> Union[List[str], str]:
        if isinstance(value, str) and not value.startswith('['):
            return [i.strip() for i in value.split(',')]
        elif isinstance(value, (list, str)):
            return value
        raise ValueError(value)

    PROJECT_NAME: str

    # TODO: Add support of sentry
    SENTRY_DSN: Optional[HttpUrl] = None

    @field_validator('SENTRY_DSN', mode='before')
    def sentry_dsn_can_be_blank(cls, value: str) -> Optional[str]:
        if not value or len(value) == 0:
            return None
        return value

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @field_validator('SQLALCHEMY_DATABASE_URI', mode='before')
    def assemble_db_connection(
        cls,
        value: Optional[str],
        info: ValidationInfo,
    ) -> Any:
        data = info.data
        if isinstance(value, str):
            return value
        return PostgresDsn.build(
            scheme='postgresql',
            username=data.get('POSTGRES_USER'),
            password=data.get('POSTGRES_PASSWORD'),
            host=data.get('POSTGRES_SERVER'),
            path=data.get('POSTGRES_DB'),
        )

    SQLALCHEMY_TESTING_DATABASE_URI: Optional[PostgresDsn] = None
    POSTGRES_TESTING_DB: Optional[str] = None

    @field_validator('SQLALCHEMY_TESTING_DATABASE_URI', mode='before')
    def assemble_testing_db_connection(
        cls,
        value: Optional[str],
        info: ValidationInfo,
    ) -> Any:
        data = info.data
        return PostgresDsn.build(
            scheme='postgresql',
            username=data.get('POSTGRES_USER'),
            password=data.get('POSTGRES_PASSWORD'),
            host=data.get('POSTGRES_SERVER'),
            path=data.get('POSTGRES_TESTING_DB', 'testing_db'),
        )

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file='.env',
        env_file_encoding='utf-8',
    )


settings = Settings()
