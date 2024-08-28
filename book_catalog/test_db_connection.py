from sqlalchemy import create_engine

DATABASE_URL = "postgresql://book_catalog_db_hg7v_user:xYRp6A9Ns6wVPtcz9B1nIykuoLod8Yc1@dpg-cr7grsa3esus7389kkf0-a:5432/book_catalog_db_hg7v"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
