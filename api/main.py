from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Import logic classes
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import UserManager, JournalManager

# ------------------- App Setup -------------------
app = FastAPI(title="Daily Journal Web API", version="1.0")

# Allow frontend apps (Streamlit/React) to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create manager instances
user_manager = UserManager()
journal_manager = JournalManager()

# ------------------- Data Models -------------------
class CreateUser(BaseModel):
    username: str
    email: str
    password: str

class UpdateUser(BaseModel):
    username: str = None
    email: str = None
    password: str = None

class CreateEntry(BaseModel):
    user_id: int
    title: str
    content: str

class UpdateEntry(BaseModel):
    title: str = None
    content: str = None

# ------------------- Endpoints -------------------
@app.get("/")
def home():
    return {"message": "Daily Journal Web App is running"}

# ------------------- Users -------------------
@app.get("/users")
def get_all_users():
    return user_manager.get_all_users()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    response = user_manager.get_user(user_id)
    if not response["success"]:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@app.post("/users")
def create_user(user: CreateUser):
    response = user_manager.add_user(user.username, user.email, user.password)
    if not response["success"]:
        raise HTTPException(status_code=400, detail=response["message"])
    return response

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    response = user_manager.update_user(user_id, user.username, user.email, user.password)
    if not response["success"]:
        raise HTTPException(status_code=400, detail=response["message"])
    return response

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    response = user_manager.delete_user(user_id)
    if not response["success"]:
        raise HTTPException(status_code=400, detail=response["message"])
    return response

# ------------------- Journal Entries -------------------
@app.get("/entries/{user_id}")
def get_entries(user_id: int):
    return journal_manager.get_entries(user_id)

@app.get("/entry/{entry_id}")
def get_entry(entry_id: int):
    response = journal_manager.get_entry_by_id(entry_id)
    if not response["success"]:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@app.post("/entries")
def create_entry(entry: CreateEntry):
    response = journal_manager.add_entry(entry.user_id, entry.title, entry.content)
    if not response["success"]:
        raise HTTPException(status_code=400, detail=response["message"])
    return response

@app.put("/entries/{entry_id}")
def update_entry(entry_id: int, entry: UpdateEntry):
    response = journal_manager.update_entry(entry_id, entry.title, entry.content)
    if not response["success"]:
        raise HTTPException(status_code=400, detail=response["message"])
    return response

@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: int):
    response = journal_manager.delete_entry(entry_id)
    if not response["success"]:
        raise HTTPException(status_code=400, detail=response["message"])
    return response

# ------------------- Run -------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
