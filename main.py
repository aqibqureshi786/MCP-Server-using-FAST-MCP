from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Sample FastAPI App", version="1.0.0")

# Sample data models
class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

# In-memory storage for demo
users_db = [
    User(id=1, name="John Doe", email="john@example.com", age=30),
    User(id=2, name="Jane Smith", email="jane@example.com", age=25),
    User(id=3, name="Bob Johnson", email="bob@example.com", age=35),
]

@app.get("/")
async def root():
    return {"message": "Welcome to Sample FastAPI App with MCP Server!"}

@app.get("/users", response_model=List[User])
async def get_users():
    """Get all users"""
    return users_db

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Get a specific user by ID"""
    user = next((user for user in users_db if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=User)
async def create_user(user: UserCreate):
    """Create a new user"""
    new_id = max([u.id for u in users_db]) + 1 if users_db else 1
    new_user = User(id=new_id, **user.dict())
    users_db.append(new_user)
    return new_user

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    """Update an existing user"""
    user_index = next((i for i, u in enumerate(users_db) if u.id == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    users_db[user_index] = User(id=user_id, **user.dict())
    return users_db[user_index]

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete a user"""
    user_index = next((i for i, u in enumerate(users_db) if u.id == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = users_db.pop(user_index)
    return {"message": f"User {deleted_user.name} deleted successfully"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "users_count": len(users_db)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
