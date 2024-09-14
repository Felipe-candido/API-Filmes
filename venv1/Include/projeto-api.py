import requests

URL = "https://api.themoviedb.org/3/authentication/token/new"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2UzNGExMjdhZDc4MzcwMWFiNjliYmFlOTI2MzczZSIsIm5iZiI6MTcyNjE5NjI0MC44MDU4LCJzdWIiOiI2NmUzYTg0NGM4MWIyNGIzZmUyM2RkMTEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.4wPYynDZKZA4Xr8SBZouPhBm7ZBFkW-WHxAXePUPzNA"
}

req = requests.get(URL, headers=headers)
dados = req.json()




movie_id = 550
URL2 = f"https://api.themoviedb.org/3/movie/{movie_id}"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2UzNGExMjdhZDc4MzcwMWFiNjliYmFlOTI2MzczZSIsIm5iZiI6MTcyNjE5NjI0MC44MDU4LCJzdWIiOiI2NmUzYTg0NGM4MWIyNGIzZmUyM2RkMTEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.4wPYynDZKZA4Xr8SBZouPhBm7ZBFkW-WHxAXePUPzNA"
}

req2 = requests.get(URL2, headers=headers)
dados2 = req2.json()

print({dados2.get('title')})

