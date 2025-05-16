# Criar um servidor OData com Flask, que exponha os dados de um arquivo CSV 
# como uma API OData simulada (estrutura JSON compatível com consumo por Microsoft Fabric, Power BI etc)

# ETAPA 1: ESTE PASSO É NUM TERMINAL/BASH Crie uma pasta para o projeto
# mkdir odata_server
# cd odata_server
# (Opcional) Crie ambiente virtual
# python -m venv venv
# venv\Scripts\activate       # No Windows
# source venv/bin/activate  # No Mac/Linux
# Instale Flask e pandas
# pip install flask pandas

# ETAPA 2: criar um csv, porém eu já tenho local
# ETAPA 3:

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/odata/Transaction', methods=['GET'])
def odata_table():
    df = pd.read_csv(r'C:/Users/taisa.silva/Downloads/PDI/Bank_Transaction_Fraud_Detection.csv')
    # Use r'...' (prefixo raw string) para evitar erros com \
    data = df.to_dict(orient='records')
    return jsonify({
        "@odata.context": "https://abc123.ngrok.io/odata/$metadata#Transaction",
        "value": data
    })

if __name__ == '__main__':
    app.run(debug=True)