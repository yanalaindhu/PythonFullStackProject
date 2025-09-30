from src.db import DatabaseManager

# Users Logic
class UserManager:
    """
    Handles CRUD operations for users.
    """
    def __init__(self):
        self.db = DatabaseManager()
    
    def add_user(self, username: str, email: str, password: str):
        if not username or not email or not password:
            return {"success": False, "message": "Username, email, and password are required."}
        result = self.db.create_user(username, email, password)
        if result and result.data:
            return {"success": True, "message": "User added successfully.", "user": result.data[0]}
        else:
            return {"success": False, "message": "Failed to add user."}

    def get_user(self, user_id: int):
        result = self.db.fetch_user_by_id(user_id)
        if result and result.data:
            return {"success": True, "user": result.data[0]}
        else:
            return {"success": False, "message": "User not found."}

    def get_all_users(self):
        result = self.db.fetch_users()
        if result and result.data:
            return {"success": True, "users": result.data}
        else:
            return {"success": True, "users": [], "message": "No users found."}

    def update_user(self, user_id: int, username=None, email=None, password=None):
        result = self.db.update_user(user_id, username, email, password)
        if result and result.data:
            return {"success": True, "message": "User updated successfully.", "user": result.data[0]}
        else:
            return {"success": False, "message": "Failed to update user or user not found."}

    def delete_user(self, user_id: int):
        result = self.db.delete_user(user_id)
        if result and result.data:
            return {"success": True, "message": "User deleted successfully."}
        else:
            return {"success": False, "message": "Failed to delete user or user not found."}

# Journal Entries Logic
class JournalManager:
    """
    Handles CRUD operations for journal entries.
    """
    def __init__(self):
        self.db = DatabaseManager()

    def add_entry(self, user_id: int, title: str, content: str):
        if not user_id or not title or not content:
            return {"success": False, "message": "User ID, title, and content are required."}
        result = self.db.insert_entry(user_id, title, content)
        if result and result.data:
            return {"success": True, "message": "Journal entry added successfully.", "entry": result.data[0]}
        else:
            return {"success": False, "message": "Failed to add journal entry."}

    def get_entries(self, user_id: int):
        result = self.db.fetch_entries(user_id)
        if result and result.data:
            return {"success": True, "entries": result.data}
        else:
            return {"success": True, "entries": [], "message": "No entries found for this user."}

    def get_entry_by_id(self, entry_id: int):
        result = self.db.fetch_entry_by_id(entry_id)
        if result and result.data:
            return {"success": True, "entry": result.data[0]}
        else:
            return {"success": False, "message": "Entry not found."}

    def update_entry(self, entry_id: int, title=None, content=None):
        result = self.db.update_entry(entry_id, title, content)
        if result and result.data:
            return {"success": True, "message": "Journal entry updated successfully.", "entry": result.data[0]}
        else:
            return {"success": False, "message": "Failed to update entry or entry not found."}

    def delete_entry(self, entry_id: int):
        result = self.db.delete_entry(entry_id)
        if result and result.data:
            return {"success": True, "message": "Journal entry deleted successfully."}
        else:
            return {"success": False, "message": "Failed to delete entry or entry not found."}
