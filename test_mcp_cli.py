#!/usr/bin/env python3
"""
CLI script to test MCP tools directly
This script demonstrates how to call MCP tools from the command line
"""

import asyncio
import json
import sys
from fastmcp import Client

async def test_mcp_tools():
    """Test MCP tools directly"""
    
    print("Testing MCP Tools Directly")
    print("=" * 40)
    
    # Initialize FastMCP client
    try:
        mcp_client = Client("mcp_server.py")
        print("[SUCCESS] MCP client initialized")
    except Exception as e:
        print(f"[ERROR] Error initializing MCP client: {e}")
        return
    
    async with mcp_client:
        # Test 1: Get all users
        print("\n1. Testing get_all_users()")
        try:
            result = await mcp_client.call_tool("get_all_users", {})
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
        
        # Test 2: Get health status
        print("\n2. Testing get_health_status()")
        try:
            result = await mcp_client.call_tool("get_health_status", {})
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
        
        # Test 3: Create a new user
        print("\n3. Testing create_user()")
        try:
            result = await mcp_client.call_tool("create_user", {
                "name": "Test User",
                "email": "test@example.com",
                "age": 25
            })
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
        
        # Test 4: Get user by ID
        print("\n4. Testing get_user_by_id()")
        try:
            result = await mcp_client.call_tool("get_user_by_id", {"user_id": 1})
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
        
        # Test 5: Get app info
        print("\n5. Testing get_app_info()")
        try:
            result = await mcp_client.call_tool("get_app_info", {})
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n[SUCCESS] MCP tools testing completed!")

if __name__ == "__main__":
    asyncio.run(test_mcp_tools())
