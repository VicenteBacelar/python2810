import requests
import pandas as pd
import time
import random
import sqlite3
import datetime
from bs4 import BeautifulSoup


# pip install beautifulsoup4
# headers para simular um navegador real (alguns sites bloqueiam 'bots' então fingimos ser um interpretador)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/114.0 Safari/537.36'}

baseURL = "https://www.adorocinema.com/filmes/melhores/"
filmes = [] 
data_hoje = datetime.date.today().strftime('%d-%m-%Y')   # Y é maiusculo
agora = datetime.datetime.now()
paginaLimite = 5
card_temp_min = 1
card_temp_max = 3
pag_temp_min = 3
pag_temp_max = 5
bancoDados = r'C:\Users\vicente.bacelar\Desktop\Python_EAD\filmes.db'
saidaCSV = f'C:/Users/vicente.bacelar/Desktop/Python_EAD/filmes_adorocinema_{data_hoje}.csv'

for pagina in range(1,paginaLimite + 1):
    # Resultado da primeira vez que executar: "https://www.adorocinema.com/filmes/melhores/?page=1"
    url = f'{baseURL}?page={pagina}' 
    print(f'Coletando dados da pagina {pagina}: {url}')
    resposta = requests.get(url, headers=headers) 
    soup = BeautifulSoup(resposta.text, 'html.parser') 

    if resposta.status_code != 200:
        print(f'Erro ao carregar a pagina {pagina}.\nCodigo do erro é: {resposta.status_code}')
        continue
    
    cards = soup.find_all("div", class_='card entity entity-card-list cf')
    for card in cards:
        try:
            # Capturar o titulo e link da pagina
            titulo_tag = card.find('a', class_='meta-title-link')
            titulo = titulo_tag.strip()   if titulo_tag else 'N/A'
            link = 'https://www.adorocinema.com' + titulo_tag['href'] if titulo_tag else None

            nota_tag = card.find('span', class_='stareval-note')
            nota = nota_tag.text.strip().replace(',','.') if nota_tag else "N/A"

            # Caso exista o link, acessar a pagina individual do filme para capturar os dados
            if link:
                filme_resposta = requests.get(link, headers=headers)
                filme_soup = BeautifulSoup(filme_resposta.text, 'html.parser')

                # Capturar diretor do filme
                diretor_tag = filme_soup.find('div', class_='meta-body-item meta-body-direction meta-body-oneline')
                if diretor_tag:
                    # Vamos higienizar o texto do diretor

                    diretor = diretor_tag.text.strip().replace('Direcao:','').replace(',','').replace('|','').strip()
                else:
                    diretor = 'N/A'
                diretor = diretor.replace('\n',' ').replace('\r','').strip

            # Captura dos generos
            genero_block = filme_soup.find('div', class_='meta-body-info')
            if genero_block :
                generos_links = genero_block.find_all('a')
                generos = [g.text.strip() for g in generos_links]
                categorias = ', '.join(generos[:5]) if generos else 'N/A'
            else:
                categoria ='N/A'

            # Captura o ano de lancamento do filme
            ano_tag = genero_block.find('span', class_='date') if genero_block else None
            ano = ano_tag.text.strip() if ano_tag else 'N/A'
            # Só adiciona o filme se todos os dados principais existirem
            if titulo != 'N/A' and link != 'N/A' and nota != 'N/A':
                filmes.append({
                    'Titulo': titulo,
                    'Direção': diretor,
                    'Nota': nota,
                    'Link': link,
                    'Ano': ano,
                    'Categoria': categoria
                })
            else:
                print(f'Filme incompleto ou erro na coleta de dados')
            # aguardar um tempo aleatorio entre cards para nao sobrecarregar o site nem
            # revelar que somos um script de webscrapping (vulgarmente conhecido como 'bot')

            tempo = random.uniform(card_temp_min, card_temp_max)
            time.sleep(tempo)
            print(f'Tempo de espera: {tempo}')


        except Exception as erro:
            print(f'Erro ao processar o filme. Erro: {erro}')
    # esperar um tempo entre uma pagina e outra
    tempo = random.uniform(pag_temp_min, pag_temp_max)
    time.sleep(tempo)

df = pd.DataFrame(filmes)
print(df.head())

# Salvar os dados em um arquivo CSV
df.to_csv(saidaCSV, index=False, encoding='utf-8-sig', quotechar="'", quoting=1)

# Conecta um banco de ados SQLite (cria se nao existir)
conn = sqlite3.connect(bancoDados)
cursor = conn.cursor()
cursor.execute('''
      CREATE TABLE IF NOT EXISTS filmes(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Titulo TEXT,
        Direcao TEXT,
        Nota REAL,
        Link TEXT,
        Ano TEXT,
        Categoria TEXT
               )
               ''')
for filme in filmes:
    try:
        cursor.execute('''
                INSERT INTO filmes
                       (Titulo, Direcao, Nota, Link, Ano, Categoria)
                       VALUES
                       (?, ?, ?, ?, ?. ?)

                       ''',( 
                           filme['Titulo'],
                           filme['Direção'],
                           float(filme['Nota']) if filme ['Nota'] != 'N/A' else None,
                           filme['Titulo'],
                           filme['LInk'],
                           filme['Ano'],
                           filme['Categoria']

                       ))
    except Exception as erro:
        print(f'Erro ao inserir o filme{filme['Titulo']}no banco de dados. Codigo de erro: {erro}'
              )
        conn.commit()
        conn.close

        print('----------------------------------')
        print('Dados raspados e salvos com sucesso')
        print('fArquivo salvo em: {saidaCSV}')
        print ('Obrigado por usar o script de Webscrapping feito por Vicente Bacelar')
        print(f'Finalizado em: {agora.strtime("%H:%M:%S")}')
        print('----------------------------------')
