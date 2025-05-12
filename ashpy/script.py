import requests # type: ignore

response = requests.get("https://api.github.com")
print("Estado de la respuesta:", response.status_code)