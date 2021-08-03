# plota o gráfico dos projetos python mais avaliados do git hub
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import pprint

nomes, estrelas, links = [], [], []

# requisição à API do GIT HUB
print('Solicitando dados à API...')
req = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars')
resposta = req.json()  # faz um dicionário com as informações recebidas
# pprint.pprint(f"Dados solicitados pela API: \n{resposta}") 
print(f"Quantidade de repositórios encontrados: {resposta['total_count']}")
itensAPI = resposta['items']
for item in itensAPI:
    nomes.append(item['name']) # nomes dos projetos
    estrelas.append(item['stargazers_count']) # total de estrelas
    links.append(item['html_url'])

# plotagem dos dados
style = LS('#5cffff', base_style=LCS)
grafico = pygal.Bar(style=style, x_label_rotation=45)  # gráfico de barras
grafico.title = 'Projetos python mais avaliados do GitHub'
grafico.x_labels = nomes    # abscissas
grafico.y_title = 'Avaliações (por quantidade de estrelas)'
grafico.add("Avaliações", estrelas)  # define as dicas de contexto(inseridos na barra) e o eixo das ordenadas
grafico.render_to_file('Grafico_for_git.svg')
print('Gráfico gerado!')

# links
for link in links:
    print(link)