import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class DatabaseManager:
    # ---------- USERS ----------
    def create_user(self, username: str, email: str, password: str):
        return supabase.table("users").insert({
            "username": username,
            "email": email,
            "password": password
        }).execute()

    def fetch_users(self):
        return supabase.table("users").select("*").execute()

    def fetch_user_by_id(self, user_id: int):
        return supabase.table("users").select("*").eq("user_id", user_id).execute()

    def update_user(self, user_id: int, username=None, email=None, password=None):
        update_data = {}
        if username: update_data["username"] = username
        if email: update_data["email"] = email
        if password: update_data["password"] = password
        return supabase.table("users").update(update_data).eq("user_id", user_id).execute()

    def delete_user(self, user_id: int):
        return supabase.table("users").delete().eq("user_id", user_id).execute()

    # ---------- JOURNAL ENTRIES ----------
    def insert_entry(self, user_id: int, title: str, content: str):
        return supabase.table("journal_entries").insert({
            "user_id": user_id,
            "title": title,
            "content": content
        }).execute()

    def fetch_entries(self, user_id: int):
        return supabase.table("journal_entries")\
            .select("*")\
            .eq("user_id", user_id)\
            .order("created_at", desc=True)\
            .execute()

    def fetch_entry_by_id(self, entry_id: int):
        return supabase.table("journal_entries")\
            .select("*")\
            .eq("entry_id", entry_id)\
            .execute()

    def update_entry(self, entry_id: int, title=None, content=None):
        update_data = {}
        if title: update_data["title"] = title
        if content: update_data["content"] = content
        return supabase.table("journal_entries").update(update_data).eq("entry_id", entry_id).execute()

    def delete_entry(self, entry_id: int):
        return supabase.table("journal_entries").delete().eq("entry_id", entry_id).execute()
