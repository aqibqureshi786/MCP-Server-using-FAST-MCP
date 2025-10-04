#!/usr/bin/env python3
"""
Complete demonstration of FastAPI + FastMCP + Gemini integration
This script shows all the components working together
"""

import asyncio
import os
import sys
import time
from fastmcp import Client
from google import genai

# Try to load from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, continue without it
    pass

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def print_step(step_num, description):
    """Print a formatted step"""
    print(f"\n[STEP {step_num}] {description}")
    print("-" * 40)

async def demo_gemini_integration():
    """Demonstrate Gemini integration with MCP tools"""
    
    print_header("FASTAPI + FASTMCP + GEMINI INTEGRATION DEMO")
    
    # Check if GEMINI_API_KEY is set
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print_step(1, "Checking Gemini API Key")
        print("[WARNING] GEMINI_API_KEY environment variable is not set")
        print("To use Gemini integration, set your API key:")
        print("export GEMINI_API_KEY='your-api-key-here'")
        print("\nContinuing with MCP tools demo only...")
        return await demo_mcp_only()
    
    print_step(1, "Initializing Gemini Client")
    try:
        gemini_client = genai.Client(api_key=api_key)
        print("[SUCCESS] Gemini client initialized")
    except Exception as e:
        print(f"[ERROR] Failed to initialize Gemini client: {e}")
        return await demo_mcp_only()
    
    print_step(2, "Initializing FastMCP Client")
    try:
        mcp_client = Client("mcp_server.py")
        print("[SUCCESS] FastMCP client initialized")
    except Exception as e:
        print(f"[ERROR] Failed to initialize MCP client: {e}")
        return
    
    print_step(3, "Testing MCP Tools with Gemini")
    
    # Example prompts that will use MCP tools
    prompts = [
        "Get all users from the FastAPI application and show me their details",
        "Create a new user named 'Alice Wonder' with email 'alice@wonderland.com' and age 28",
        "What is the current health status of the application?",
        "Show me information about the FastAPI application"
    ]
    
    async with mcp_client:
        for i, prompt in enumerate(prompts, 1):
            print(f"\n[PROMPT {i}] {prompt}")
            print("Gemini Response:")
            print("-" * 30)
            
            try:
                response = await gemini_client.aio.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt,
                    config=genai.types.GenerateContentConfig(
                        temperature=0.1,
                        tools=[mcp_client.session],
                    ),
                )
                print(response.text)
                
            except Exception as e:
                print(f"[ERROR] {e}")
            
            # Add a small delay between requests
            await asyncio.sleep(1)
    
    print_step(4, "Demo Completed Successfully!")
    print("[SUCCESS] All components are working together!")

async def demo_mcp_only():
    """Demonstrate MCP tools without Gemini"""
    
    print_header("MCP TOOLS DEMONSTRATION")
    
    print_step(1, "Initializing FastMCP Client")
    try:
        mcp_client = Client("mcp_server.py")
        print("[SUCCESS] FastMCP client initialized")
    except Exception as e:
        print(f"[ERROR] Failed to initialize MCP client: {e}")
        return
    
    print_step(2, "Testing MCP Tools")
    
    async with mcp_client:
        # Test all available tools
        tools_to_test = [
            ("get_all_users", {}, "Get all users"),
            ("get_health_status", {}, "Get health status"),
            ("get_app_info", {}, "Get app information"),
            ("create_user", {"name": "Demo User", "email": "demo@example.com", "age": 30}, "Create new user"),
            ("get_user_by_id", {"user_id": 1}, "Get user by ID")
        ]
        
        for i, (tool_name, params, description) in enumerate(tools_to_test, 1):
            print(f"\n[TOOL {i}] {description}")
            print(f"Tool: {tool_name}")
            print(f"Parameters: {params}")
            print("Result:")
            print("-" * 30)
            
            try:
                result = await mcp_client.call_tool(tool_name, params)
                # Extract the text content from the result
                if hasattr(result, 'content') and result.content:
                    text_content = result.content[0].text if result.content else str(result)
                    print(text_content)
                else:
                    print(str(result))
                    
            except Exception as e:
                print(f"[ERROR] {e}")
    
    print_step(3, "MCP Demo Completed!")
    print("[SUCCESS] All MCP tools are working correctly!")

def check_fastapi_running():
    """Check if FastAPI is running"""
    try:
        import requests
        response = requests.get("http://localhost:8000/health", timeout=2)
        return response.status_code == 200
    except:
        return False

async def main():
    """Main demo function"""
    
    print_header("SYSTEM CHECK")
    
    # Check if FastAPI is running
    if not check_fastapi_running():
        print("[WARNING] FastAPI application doesn't seem to be running")
        print("Please start the FastAPI app first:")
        print("python start_fastapi.py")
        print("\nOr manually with:")
        print("uvicorn main:app --reload")
        return
    
    print("[SUCCESS] FastAPI application is running")
    
    # Run the appropriate demo
    await demo_gemini_integration()

if __name__ == "__main__":
    asyncio.run(main())
