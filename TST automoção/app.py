from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By

chrome_options=Options() 
chrome_options.add_experimental_option("detach",True) 
servico = Service(ChromeDriverManager().install()) 
navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get("https://cra-pe.implanta.net.br/portaltransparencia/#publico/inicio")

navegador.find_element('xpath', '/html/body/div[1]/nav/a').click() 
navegador.find_element('xpath', '/html/body/div[1]/nav/div/ul/li[5]/a').click() 
navegador.find_element('xpath', '/html/body/div[1]/nav/div/ul/li[5]/ul/li[6]/a').click() 
navegador.find_element('xpath', '//*[@id="btBuscar"]').click()