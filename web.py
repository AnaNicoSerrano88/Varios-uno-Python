import requests

r = requests.get("https://support.lenovo.com/th/es/downloads/ds502226")
with open("index.html", "wb") as f:
    f.write(r.content)
r.close()