import requests, time

#def animes(rAnime, rEpisodios):
#    requisicaoAnime = requests.get(rAnime)
#    requisicaoEp = requests.get(rEpisodios)
#
#    conteudoAnime = requisicaoAnime.json()
#    conteudoEp = requisicaoEp.json()

page = 1
page_url = "https://kitsu.io/api/edge/anime?page%5Blimit%5D=10\u0026page%5Boffset%5D="

requisicao_anime = requests.get(page_url+str(page))
animes = requisicao_anime.json()

#requisicao_anime = requests.get("https://kitsu.io/api/edge/anime")
#animes = requisicao_anime.json()

#print(conteudo["data"][0]["attributes"]["canonicalTitle"])

for anime in animes["data"]:
    atributosA = anime["attributes"]
    print("Anime: " + atributosA["canonicalTitle"],
        "\nNota: " + atributosA["averageRating"],
        "\nSinopse: " + atributosA["synopsis"])

    episodios_url = anime["relationships"]["episodes"]["links"]["related"]
    requisicao_episodios = requests.get(episodios_url)
    episodios = requisicao_episodios.json()

    for episodio in episodios["data"]:
        atributosE = episodio["attributes"]
        print("Nome do Episódio: " + str(atributosE["canonicalTitle"]),
              "\nEp: " + str(atributosE["number"]),
              "\nTemp: " + str(atributosE["seasonNumber"]))
#        time.sleep(1)
        print("-"*100)
#    time.sleep(3)
    print("="*100)

