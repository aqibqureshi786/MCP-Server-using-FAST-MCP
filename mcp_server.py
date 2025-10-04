#!/usr/bin/env python3
"""
MCP Server for FastAPI Sample App
This server provides tools to interact with the FastAPI application
"""

import asyncio
import json
import sys
from typing import Any, Dict, List, Optional
import httpx
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("FastAPI Sample App MCP Server")

# Configuration
FASTAPI_BASE_URL = "http://localhost:8000"

@mcp.tool()
def get_all_users() -> str:
    """Get all users from the FastAPI application"""
    try:
        import requests
        response = requests.get(f"{FASTAPI_BASE_URL}/users")
        response.raise_for_status()
        users = response.json()
        return json.dumps(users, indent=2)
    except Exception as e:
        return f"Error fetching users: {str(e)}"

@mcp.tool()
def get_user_by_id(user_id: int) -> str:
    """Get a specific user by ID from the FastAPI application"""
    try:
        import requests
        response = requests.get(f"{FASTAPI_BASE_URL}/users/{user_id}")
        response.raise_for_status()
        user = response.json()
        return json.dumps(user, indent=2)
    except Exception as e:
        return f"Error fetching user {user_id}: {str(e)}"

@mcp.tool()
def create_user(name: str, email: str, age: Optional[int] = None) -> str:
    """Create a new user in the FastAPI application"""
    try:
        import requests
        user_data = {"name": name, "email": email}
        if age is not None:
            user_data["age"] = age
        
        response = requests.post(f"{FASTAPI_BASE_URL}/users", json=user_data)
        response.raise_for_status()
        new_user = response.json()
        return json.dumps(new_user, indent=2)
    except Exception as e:
        return f"Error creating user: {str(e)}"

@mcp.tool()
def update_user(user_id: int, name: str, email: str, age: Optional[int] = None) -> str:
    """Update an existing user in the FastAPI application"""
    try:
        import requests
        user_data = {"name": name, "email": email}
        if age is not None:
            user_data["age"] = age
        
        response = requests.put(f"{FASTAPI_BASE_URL}/users/{user_id}", json=user_data)
        response.raise_for_status()
        updated_user = response.json()
        return json.dumps(updated_user, indent=2)
    except Exception as e:
        return f"Error updating user {user_id}: {str(e)}"

@mcp.tool()
def delete_user(user_id: int) -> str:
    """Delete a user from the FastAPI application"""
    try:
        import requests
        response = requests.delete(f"{FASTAPI_BASE_URL}/users/{user_id}")
        response.raise_for_status()
        result = response.json()
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error deleting user {user_id}: {str(e)}"

@mcp.tool()
def get_health_status() -> str:
    """Get the health status of the FastAPI application"""
    try:
        import requests
        response = requests.get(f"{FASTAPI_BASE_URL}/health")
        response.raise_for_status()
        health = response.json()
        return json.dumps(health, indent=2)
    except Exception as e:
        return f"Error checking health: {str(e)}"

@mcp.tool()
def get_app_info() -> str:
    """Get basic information about the FastAPI application"""
    try:
        import requests
        response = requests.get(f"{FASTAPI_BASE_URL}/")
        response.raise_for_status()
        info = response.json()
        return json.dumps(info, indent=2)
    except Exception as e:
        return f"Error fetching app info: {str(e)}"

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
