import requests


def listar_filmes():

    api_key = "f3e34a127ad783701ab69bbae926373e"
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR"

    url_generos = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
    response_generos = requests.get(url_generos)
    generos_data = response_generos.json()

    # COMO A PRIMEIRA URL LISTA OS FILMES MAS NÃO POSSUI O NOME DOS GENEROS, USEI UM DICIONÁRIO QUE LIGA O ID DO GENERO AO SEU NOME
    genero_dict = {genre['id']: genre['name'] for genre in generos_data['genres']}

    all_movies = []
    page = 1
    max_pages = 10 # A API POSSUI MILHARES DE PAGINAS COM 20 FILMES EM CADA, ENTÃO PEGUE APENAS 10 PARA NÃO DEMORAR AS REQUISIÇÕES 
    total = 1  

    # ESSA API POSSUI OS FILMES ORDENADOS EM PÁGINAS, ENTÃO PARA PUXAR ESSES FILMES TEMOS QUE PASSAR POR TODAS AS PÁGINAS E ARMAZENAS OS FILMES EM UMA LISTA
    while page <= max_pages and page <= total:
        response = requests.get(f"{url}&page={page}")
        
        if response.status_code == 200:
            filme = response.json()
            total = filme['total_pages'] 
            
            
            all_movies.extend(filme['results'])
            
            page += 1
        else:
            print(f"Erro ao acessar a API: {response.status_code}")
            break


    for filme in all_movies[:100]:
        
        id = filme['id']
        print(f"Id: {id}")

        nome = filme['title']
        print (f"nome: {nome}")
        
        x = 1
        for genero_id in filme['genre_ids']:
            genero = genero_dict.get(genero_id, "Gênero desconhecido")
            print(f"genero {x}: {genero}")
            x = x+1

        nota = filme.get('vote_average')
        print(f'Nota media: {nota}')

        descricao = filme.get('overview')
        print(f'Sinopse: {descricao}')
        print ("============================")

def filtrar_genero():
    api_key = "f3e34a127ad783701ab69bbae926373e"
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR"

    url_generos = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
    response_generos = requests.get(url_generos)
    generos_data = response_generos.json()

    genero_dict = {genre['id']: genre['name'] for genre in generos_data['genres']}

    all_movies = []
    page = 1
    max_pages = 10  
    total = 1
    
    while page <= max_pages and page <= total:
        response = requests.get(f"{url}&page={page}")
        
        if response.status_code == 200:
            filme = response.json()
            total = filme['total_pages'] 
            
            
            all_movies.extend(filme['results'])
            
            page += 1
        else:
            print(f"Erro ao acessar a API: {response.status_code}")
            break

    buscar = input('Digite o gênero que deseja filtrar: ')

    for filme in all_movies[:100]:

        for genero_id in filme['genre_ids']:
            genero = genero_dict.get(genero_id)
            
            if genero.lower() == buscar.lower():
                print(filme['title'])

def buscar_filme():
    api_key = "f3e34a127ad783701ab69bbae926373e"
    buscar = input("Digite o nome do filme que deseja procurar: ")

    # ENDPOINT DA URL PARA PESQUISAR FILMES 
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=pt-BR&query={buscar}"

    url_generos = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
    response_generos = requests.get(url_generos)
    generos_data = response_generos.json()
    genero_dict = {genre['id']: genre['name'] for genre in generos_data['genres']}

    response = requests.get(url)
    
    if response.status_code == 200:
        filmes = response.json()['results']
        
        if filmes:
            for filme in filmes:
                id = filme['id']
                print(f"Id: {id}")

                nome = filme['title']
                print(f"Nome: {nome}")
                
                x = 1
                for genero_id in filme['genre_ids']:
                    genero = genero_dict.get(genero_id, "Gênero desconhecido")
                    print(f"genero {x}: {genero}")
                    x = x+1

                nota = filme.get('vote_average')
                print(f"Nota média: {nota}")

                descricao = filme.get('overview')
                print(f"Sinopse: {descricao}")
                print("==========================")
        else:
            print("Nenhum filme encontrado.")
    
    else:
        print(f"Erro ao acessar a API: {response.status_code}")

while True:
    
    print("=========== MENU ==========")
    print("Selecione o numero da opção de deseja")
    print("1 - Listar todos os filmes(coloquei apenas 100 pois a API é muito grande)")
    print("2 - Filtrar por gênero(filtra apenas os 100 listados acima)")
    print("3 - Pesquisar pelo nome(esse busca na API inteira)")
    opcao = input()

    if opcao == '1':
        listar_filmes()

    elif opcao == '2':
        filtrar_genero()

    elif opcao == '3':
        buscar_filme()

    else:
        print("Opção inválida, tente novamente ou feche o programa")
    # Condição de saída
    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break