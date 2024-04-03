import os
from functools import lru_cache


class Config:
    DEBUG = False
    OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")


class ProductionConfig(Config):
    ...


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


@lru_cache
def get_config():
    config = {
        "production": ProductionConfig,
        "development": DevelopmentConfig,
        "testing": TestingConfig,
    }
    env = os.getenv("APP_ENV", "development")
    return config.get(env, DevelopmentConfig)
