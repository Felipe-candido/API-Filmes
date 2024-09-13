import requests
URL= "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2UzNGExMjdhZDc4MzcwMWFiNjliYmFlOTI2MzczZSIsIm5iZiI6MTcyNjE5NjI0MC44MDU4LCJzdWIiOiI2NmUzYTg0NGM4MWIyNGIzZmUyM2RkMTEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.4wPYynDZKZA4Xr8SBZouPhBm7ZBFkW-WHxAXePUPzNA"
}

req = requests.get(URL, headers=headers)
dados = req.json()

print(dados)
