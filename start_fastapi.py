#!/usr/bin/env python3
"""
Startup script for the FastAPI application
"""

import subprocess
import sys
import time
import requests
from pathlib import Path

def check_fastapi_running():
    """Check if FastAPI is already running"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=2)
        return response.status_code == 200
    except:
        return False

def start_fastapi():
    """Start the FastAPI application"""
    print("Starting FastAPI application...")
    
    if check_fastapi_running():
        print("FastAPI is already running on http://localhost:8000")
        return True
    
    try:
        # Start FastAPI with uvicorn
        process = subprocess.Popen([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--reload"
        ])
        
        # Wait a moment for the server to start
        time.sleep(3)
        
        # Check if it's running
        if check_fastapi_running():
            print("[SUCCESS] FastAPI started successfully on http://localhost:8000")
            print("[INFO] API Documentation available at: http://localhost:8000/docs")
            return True
        else:
            print("[ERROR] Failed to start FastAPI")
            return False
            
    except Exception as e:
        print(f"[ERROR] Error starting FastAPI: {e}")
        return False

if __name__ == "__main__":
    start_fastapi()
