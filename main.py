import sys

import requests

url = sys.argv[1] if len(sys.argv) > 1 else "https://something.com"

r = requests.get(url)

print(r.status_code)
print(r.content)
