from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Cadastral check'
    description = 'Matching a cadastral number against given coordinates'
    database_url: str = 'sqlite+aiosqlite:///./cadastral.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
