from supabase import create_client

from app.config import SUPABASE_KEY, SUPABASE_URL


def supabase_client():
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    try:
        yield client
    finally:
        pass
