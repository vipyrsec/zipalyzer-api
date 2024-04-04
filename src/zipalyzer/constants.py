"""
Loads configuration from environment variables and `.env` files.

By default, the values defined in the classes are used, these can be overridden by an env var with the same name.

An `.env` file is used to populate env vars, if present.
"""

from os import getenv

from pydantic_settings import BaseSettings, SettingsConfigDict

# Git SHA for Sentry
GIT_SHA = getenv("GIT_SHA", "development")


class EnvConfig(BaseSettings):
    """Our default configuration for models that should load from .env files."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )


class _Sentry(EnvConfig, env_prefix="sentry_"):
    dsn: str = ""
    environment: str = "production"
    release_prefix: str = "zipalyzer"


Sentry = _Sentry()
