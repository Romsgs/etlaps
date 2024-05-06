import os

# Load environment variables from a .env file, if it exists
from dotenv import load_dotenv
load_dotenv()

# Environment Variables
APS_CLIENT_ID = os.getenv('APS_CLIENT_ID', '')
APS_CLIENT_SECRET = os.getenv('APS_CLIENT_SECRET', '')
SERVER_SESSION_SECRET = os.getenv('SERVER_SESSION_SECRET', '')
EXPRESS_SESSION_SECRET = os.getenv('EXPRESS_SESSION_SECRET', '')
APS_CALLBACK_URL = os.getenv('APS_CALLBACK_URL', '')
PORT = int(os.getenv('PORT', 3001))

# Scopes
FULL_SCOPE = os.getenv('FULL_SCOPE', '')
LOW_SCOPE = os.getenv('LOW_SCOPE', '')

# Static Scopes
INTERNAL_TOKEN_SCOPES = ["data:read"]
PUBLIC_TOKEN_SCOPES = ["viewables:read"]