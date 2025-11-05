from flask import Flask, request, jsonify, Response
import requests
import io
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# instalar libs:
# pip install pandas
# pip install matplotlib


app = Flask(__name__)

@app.route('/consultar_ibge/<string:nome>', methods=['GET'])
def consultar_ibge(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?nome={nome}"
    r = requests.get(url, timeout=15)

    # Verificacoes basicas
    if r.status_code != 200:
        return jsonify({"erro":"Falha ao consultar IBGE", "status_code":r.status_code}), 502
    
    try:
        data = r.json()
    except ValueError:
        return jsonify({"erro":"Resposta do IBGE não é um json válido"}), 502
    
    if not isinstance(data, list) or len(data) == 0:
        return jsonify({"erro":"Nenhum dado retornado para esse nome"}), 404
    
    # O Formato esperado: data[0] contem 'localidade' (ex: 'BR') e 'res' (lista com periodo/frequencia)
    bloco = data[0]
    localidade = bloco.get("localidade","BR")
    res = bloco.get("res", [])

    if not res:
        return jsonify({"erro":" Sem resultados em 'res' para esse nome"}), 404
    
    
    # Monta o dataframe com as colunas disponveis (normalmente 'periodo' e 'frequencia')
    df = pd.DataFrame(res)   # transforma em uma tabela

    # Se o usuario pediu PNG (?formato=png), retorna o grafico
    if request.args.get("formato") == "png" :
        fig, ax = plt.subplots()
        # Ordena por periodo, se existir
        if "periodo" in df.columns:
        # Converte periodo para string para ordenar consistentemente
            df = df.sort_values(by='periodo')
            x = df["periodo"]
        else :
            x = range(len(df))
        y = df["frequencia"]

        # Cria o Gráfico
        ax.bar(x,y)
        ax.set_title(f"Frequencia do nome {nome}")   # Titulo do eixo x
        ax.set_xlabel("Periodo")   # Titulo do eixo X
        ax.set_ylabel("Frequencia") # Titulo do eixo Y
        plt.xticks(rotation=45, ha="right")

        # Gera uma imagem temporariamente em um buffer de memoria para evitar ter de salvar em disco
        buf = io.BytesIO()
        FigureCanvas(fig).print_png(buf)
        plt.close(fig)
        buf.seek(0)

        return Response(buf.getvalue(), mimetype="image/png")
        
    # Retorna JSON com um resumo dos dados
    return jsonify({
        "nome" : bloco.get("nome", nome),
        "localidade" : localidade,
        "dados": df.to_dict(orient="records")
        })

if __name__ == "__main__":
    app.run(debug=True)
