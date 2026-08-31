import requests

r = requests.get("https://something.com")

print(r.status_code)
print(r.content)
