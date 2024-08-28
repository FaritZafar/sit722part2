import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://book_catalog_db_hg7v_user:xYRp6A9Ns6wVPtcz9B1nIykuoLod8Yc1@dpg-cr7grsa3esus7389kkf0-a:5432/book_catalog_db_hg7v")

settings = Settings()
