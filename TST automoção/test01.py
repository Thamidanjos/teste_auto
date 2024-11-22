from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get("https://cra-pe.implanta.net.br/portaltransparencia/#publico/inicio")

try:
   
    primeiro_elemento = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/a'))
    )
    primeiro_elemento.click()

    
    segundo_elemento = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/div/ul/li[5]/a'))
    )
    segundo_elemento.click()

   
    terceiro_elemento = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/div/ul/li[5]/ul/li[6]/a'))
    )
    terceiro_elemento.click()

    
    botao_buscar = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btBuscar"]'))
    )
    botao_buscar.click()

    quarto_elemento= WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/a'))
    )
    quarto_elemento.click()

except Exception as e:
    print(f"Ocorreu um erro: {e}")


