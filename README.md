# FastAPI + FastMCP + Gemini Integration

A complete demonstration of integrating FastAPI with Google's Gemini AI through the Model Context Protocol (MCP) using FastMCP.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Gemini API Key
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your-gemini-api-key-here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 3. Start FastAPI
```bash
python start_fastapi.py
```

### 4. Test the Integration
```bash
# Test MCP tools directly
python test_mcp_cli.py

# Test Gemini integration
python gemini_integration.py

# Run complete demo
python demo.py
```

## 📁 Project Structure

```
FASTMCP/
├── main.py                 # FastAPI application
├── mcp_server.py          # FastMCP server with tools
├── gemini_integration.py  # Gemini SDK integration
├── test_mcp_cli.py        # CLI testing script
├── demo.py                # Complete demonstration
├── start_fastapi.py       # FastAPI startup script
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## 🛠️ Core Components

### FastAPI Application (`main.py`)
- RESTful API with user management (CRUD operations)
- Health check endpoint
- Auto-generated documentation at `/docs`

### FastMCP Server (`mcp_server.py`)
Provides 7 MCP tools for API interaction:
- `get_all_users()` - Retrieve all users
- `get_user_by_id(user_id)` - Get specific user
- `create_user(name, email, age)` - Create new user
- `update_user(user_id, name, email, age)` - Update user
- `delete_user(user_id)` - Delete user
- `get_health_status()` - Check app health
- `get_app_info()` - Get app information

### Gemini Integration (`gemini_integration.py`)
- Direct integration with Google's Gemini API
- Natural language interface for MCP tools
- Automatic tool selection based on prompts

## 🤖 How It Works

1. **FastAPI** provides a RESTful API for user management
2. **FastMCP** creates an MCP server that exposes API functions as tools
3. **Gemini** can call these tools automatically based on natural language prompts

### Example Gemini Interactions

```
"Get all users from the FastAPI application"
→ Gemini calls get_all_users() and formats the response

"Create a new user named Alice with email alice@example.com and age 28"
→ Gemini calls create_user() with the specified parameters

"What is the health status of the application?"
→ Gemini calls get_health_status() and reports the status
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/users` | List all users |
| GET | `/users/{id}` | Get user by ID |
| POST | `/users` | Create user |
| PUT | `/users/{id}` | Update user |
| DELETE | `/users/{id}` | Delete user |
| GET | `/health` | Health check |

## 🧪 Testing

### Test FastAPI Endpoints
```bash
# Get all users
python -c "import requests; print(requests.get('http://localhost:8000/users').json())"

# Health check
python -c "import requests; print(requests.get('http://localhost:8000/health').json())"
```

### Test MCP Tools
```bash
python test_mcp_cli.py
```

### Test Gemini Integration
```bash
python gemini_integration.py
```

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | For Gemini integration |

## 📚 Key Features

- ✅ **Natural Language Interface** - Ask questions in plain English
- ✅ **Automatic Tool Selection** - Gemini chooses appropriate MCP tools
- ✅ **Real-time API Interaction** - Direct communication with FastAPI
- ✅ **Complete CRUD Operations** - Full user management capabilities
- ✅ **Error Handling** - Comprehensive error management
- ✅ **Cross-platform Support** - Works on Windows, macOS, Linux

## 🐛 Troubleshooting

### FastAPI Not Starting
- Check if port 8000 is available
- Ensure all dependencies are installed
- Run: `uvicorn main:app --reload`

### MCP Tools Not Working
- Verify FastAPI is running on http://localhost:8000
- Check MCP server script for errors

### Gemini Integration Issues
- Verify `GEMINI_API_KEY` is set correctly in `.env` file
- Check API quota and permissions
- Ensure google-genai package is installed

## 🔗 Learn More

- [FastMCP Documentation](https://fastmcp.dev/)
- [Google Gemini SDK](https://ai.google.dev/gemini-api/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)

## 📄 License

This project is open source and available under the MIT License.