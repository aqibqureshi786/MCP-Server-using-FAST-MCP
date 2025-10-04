#!/usr/bin/env python3
"""
Gemini SDK integration with FastMCP Server
This script demonstrates how to use Google's Gemini API with our FastMCP server
"""

import asyncio
import os
import sys
from fastmcp import Client
from google import genai

# Try to load from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, continue without it
    pass

# Configuration
FASTAPI_BASE_URL = "http://localhost:8000"
MCP_SERVER_SCRIPT = "mcp_server.py"

async def main():
    """Main function to demonstrate Gemini + MCP integration"""
    
    # Check if GEMINI_API_KEY is set
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable is not set")
        print("Please set your Gemini API key:")
        print("export GEMINI_API_KEY='your-api-key-here'")
        return
    
    # Initialize Gemini client
    try:
        gemini_client = genai.Client(api_key=api_key)
        print("[SUCCESS] Gemini client initialized successfully")
    except Exception as e:
        print(f"[ERROR] Error initializing Gemini client: {e}")
        return
    
    # Initialize FastMCP client
    try:
        mcp_client = Client(MCP_SERVER_SCRIPT)
        print("[SUCCESS] FastMCP client initialized successfully")
    except Exception as e:
        print(f"[ERROR] Error initializing MCP client: {e}")
        return
    
    # Example interactions
    examples = [
        "Get all users from the FastAPI application",
        "Create a new user named Alice with email alice@example.com and age 28",
        "Get the health status of the application",
        "Update user with ID 1 to have the name 'John Updated'",
        "Show me information about the FastAPI application"
    ]
    
    print("\nStarting Gemini + MCP integration demo...")
    print("=" * 60)
    
    async with mcp_client:
        for i, prompt in enumerate(examples, 1):
            print(f"\nExample {i}: {prompt}")
            print("-" * 40)
            
            try:
                response = await gemini_client.aio.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt,
                    config=genai.types.GenerateContentConfig(
                        temperature=0.1,
                        tools=[mcp_client.session],  # Pass the FastMCP client session
                    ),
                )
                print(f"Gemini Response: {response.text}")
                
            except Exception as e:
                print(f"[ERROR] {e}")
            
            # Add a small delay between requests
            await asyncio.sleep(1)
    
    print("\n[SUCCESS] Demo completed!")

def check_fastapi_running():
    """Check if FastAPI is running"""
    try:
        import requests
        response = requests.get(f"{FASTAPI_BASE_URL}/health", timeout=2)
        return response.status_code == 200
    except:
        return False

if __name__ == "__main__":
    print("FastAPI + FastMCP + Gemini Integration Demo")
    print("=" * 50)
    
    # Check if FastAPI is running
    if not check_fastapi_running():
        print("[WARNING] FastAPI application doesn't seem to be running")
        print("Please start the FastAPI app first:")
        print("python start_fastapi.py")
        print("\nOr manually with:")
        print("uvicorn main:app --reload")
        print()
    
    # Run the async main function
    asyncio.run(main())
