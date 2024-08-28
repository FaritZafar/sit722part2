import os

class Settings:
    DATABASE_URL: str = os.getenv("book_catalog_db")
settings = Settings()
