from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)
CORS (app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    state_code = data['stateCode']
    month = data['month']

 
    resultados = analisar_sites(state_code, month)

    return jsonify(resultados)

def analisar_sites(state_code, month):
    urls = [
      
        "https://cra-pe.implanta.net.br/portaltransparencia/#publico/inicio",

    ]

    resultados = []


    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    for url in urls:
        navegador.get(url)

        try:
           
            estado_elemento = WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, 'xpath_do_elemento_estado'))
            )
            estado_elemento.send_keys(state_code)

            mes_elemento = WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, 'xpath_do_elemento_mes'))
            )
            mes_elemento.send_keys(month)

            # Clique no botão de buscar
            botao_buscar = WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, 'xpath_do_botao_buscar'))
            )
            botao_buscar.click()

            # Aguarde e processe os resultados
            # Aqui você pode adicionar a lógica para verificar os dados atualizados
            # Exemplo fictício:
            dados = "dados_processados"  # Substitua pela lógica real de extração de dados
            if "atualizado" in dados:
                resultados.append({'keyword': url, 'status': 2})  
            else:
                resultados.append({'keyword': url, 'status': 1}) 

        except Exception as e:
            resultados.append({'keyword': url, 'status': 0})  

    navegador.quit()
    return resultados

if __name__ == '__main__':
    app.run(debug=True)