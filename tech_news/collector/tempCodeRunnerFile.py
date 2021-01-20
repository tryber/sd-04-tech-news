import requests

response = requests.get("https://www.betrybe.com/")
print(response.status_code)  # código de status
print(response.headers["Content-Type"])
