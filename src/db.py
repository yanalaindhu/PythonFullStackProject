import os
import bcrypt
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase=create_client(url,key)
# Users CRUD
   
def create_user(username: str, email: str, password: str):
    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    return supabase.table("users").insert({
        "username": username,
        "email": email,
        "password": hashed_pw
    }).execute()


def fetch_users():
    return supabase.table("users").select("*").execute()

def update_user(user_id: int, username=None, email=None, password=None):
    update_data = {}
    if username: update_data["username"] = username
    if email: update_data["email"] = email
    if password:
        update_data["password"] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    return supabase.table("users").update(update_data).eq("user_id", user_id).execute()


def delete_user(user_id: int):
    return supabase.table("users").delete().eq("user_id", user_id).execute()

    ##Journal Entries CRUD 

def insert_entry(user_id: int, title: str, content: str):
    """Create a new journal entry"""
    return supabase.table("journal_entries").insert({
        "user_id": user_id,
        "title": title,
        "content": content
    }).execute()

def fetch_entries(user_id: int):
    """Get all journal entries for a user (latest first)"""
    return supabase.table("journal_entries")\
        .select("*")\
        .eq("user_id", user_id)\
        .order("created_at", desc=True)\
        .execute()
def update_entry(entry_id: int, title=None, content=None):
    """Update a journal entry's title and/or content"""
    update_data = {}
    if title: update_data["title"] = title
    if content: update_data["content"] = content
    return supabase.table("journal_entries")\
        .update(update_data)\
        .eq("entry_id", entry_id)\
        .execute()


def delete_entry(entry_id: int):
    """Delete a journal entry by ID"""
    return supabase.table("journal_entries")\
        .delete()\
        .eq("entry_id", entry_id)\
        .execute()
