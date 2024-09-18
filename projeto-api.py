import requests

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2UzNGExMjdhZDc4MzcwMWFiNjliYmFlOTI2MzczZSIsIm5iZiI6MTcyNjE5NjI0MC44MDU4LCJzdWIiOiI2NmUzYTg0NGM4MWIyNGIzZmUyM2RkMTEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.4wPYynDZKZA4Xr8SBZouPhBm7ZBFkW-WHxAXePUPzNA"
# }



def lista_filmes():
    # 957 FILMES
    max_filmes = 957

    for i in range(max_filmes):

        api_key = "f3e34a127ad783701ab69bbae926373e"
        url = f"https://api.themoviedb.org/3/movie/{i}?api_key={api_key}&language=pt-BR"

        req = requests.get(url)
        req.encoding = 'utf-8'
        filme = req.json()

        nome = filme.get('title')
        
        if(nome):
            print (f"nome: {nome}")

            x = 1
            for genre in filme['genres']:
                genero = genre['name']
                print(f"genero {x}: {genre['name']}")
                x = x+1

            nota = filme.get('vote_average')
            print(f'Nota media: {nota}')

            duracao = filme.get('runtime')
            print(f'Duração: {duracao} minutos')

            descricao = filme.get('overview')
            print(f'Sinopse: {descricao}')
            print ("============================")
        


lista_filmes()


