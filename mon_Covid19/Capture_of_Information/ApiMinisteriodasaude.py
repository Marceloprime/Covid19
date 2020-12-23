import requests

r = requests.get('https://elasticsearch-saps.saude.gov.br/desc-notificacoes-esusve-*/_search?pretty')

print(r)