#!/usr/bin/env python3
"""Quick test to see XDK response structure"""

import os
import json
from dotenv import load_dotenv
from xdk import Client

load_dotenv()

client = Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'))

try:
    response = client.posts.search_recent(
        query='PNKSTR',
        max_results=10
    )
except Exception as e:
    print(f"Error: {e}")
    import sys
    sys.exit(1)

print("Response type:", type(response))
print("\nResponse attributes:", [attr for attr in dir(response) if not attr.startswith('_')])

if hasattr(response, 'data'):
    print("\nFirst tweet type:", type(response.data[0]))
    print("First tweet:", response.data[0])

if hasattr(response, 'includes'):
    print("\nIncludes type:", type(response.includes))
    print("Includes:", response.includes)
