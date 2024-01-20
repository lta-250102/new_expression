import uvicorn
from app import app
from core.config import api_config

if __name__ == "__main__":
    uvicorn.run(app, host=api_config['host'], port=api_config['port'])