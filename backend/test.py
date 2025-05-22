import requests

url = "https://studious-space-system-xg6w5v7x5jrh6qxq-8000.app.github.dev/attendance/logs/now/"
data = {
}
headers = {
    "Content-Type": "application/json",
}

response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)
