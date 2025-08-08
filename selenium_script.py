from selenium import webdriver  # Importa a biblioteca Selenium para manipular o navegador automaticamente.
from selenium.webdriver.common.by import By  # Importa o módulo para localizar elementos na página de diferentes maneiras.
from selenium.webdriver.support.ui import WebDriverWait  # Importa a classe para esperar até que elementos estejam disponíveis.
from selenium.webdriver.support import expected_conditions as EC  # Importa condições esperadas, que facilitam o trabalho de espera por elementos.
from selenium.webdriver.chrome.service import Service  # Importa a classe Service para facilitar a instalação do driver.
from webdriver_manager.chrome import ChromeDriverManager  # Gerenciador que baixa automaticamente o driver do Chrome.

from dotenv import load_dotenv  # Importa a biblioteca para carregar variáveis de ambiente a partir de um arquivo .env.
import os  # Importa o módulo para trabalhar com variáveis de ambiente.

import time  # Importa a biblioteca de tempo, usada para definir intervalos de espera.

load_dotenv()  # Carrega as variáveis do arquivo .env para o ambiente.

# Obtém as credenciais de login do arquivo .env.
login_email = os.getenv("EMAIL")  # Carrega o email de login a partir das variáveis de ambiente.
login_password = os.getenv("PASSWORD")  # Carrega a senha de login a partir das variáveis de ambiente.

# Configura as opções do navegador Chrome.
chrome_options = webdriver.ChromeOptions()  # Cria um objeto de opções para configurar o Chrome.
chrome_options.add_argument('--start-maximized')  # (Comentado) Inicia o navegador em tela cheia.
#chrome_options.add_argument('--window-size=700,1080')  # (Comentado) Define o tamanho da janela do navegador.
chrome_options.add_argument('--headless')  # Executa o navegador em modo headless, sem interface gráfica.

# Define o serviço do ChromeDriver usando o ChromeDriverManager para instalar automaticamente o driver.
service = Service(ChromeDriverManager().install())

# Inicializa o driver do Chrome com as opções e serviço definidos.
driver = webdriver.Chrome(service=service, options=chrome_options)
# Define uma espera explícita de 30 segundos, que será usada ao procurar elementos na página.
wait = WebDriverWait(driver, 30)

# URL da página do Power BI que será acessada.
url="https://app.powerbi.com/groups/a81161c5-3a80-4f12-bd87-177f52f58a52/datasets/7b7c51f4-4a24-4748-b278-6a321add552f/details?experience=power-bi"
# Imprime uma mensagem indicando que está acessando o Power BI.
print("Acessando o Power BI")
# Acessa a URL do Power BI.
driver.get(url)

time.sleep(5)  # Aguarda 5 segundos para garantir que a página carregue.

# Seletores XPath dos elementos da página.
email='//*[@id="email"]'  # Caminho XPath do campo de email.
botao_enviar ='//*[@id="submitBtn"]'  # Caminho XPath do botão enviar.
senha='//*[@id="i0118"]'  # Caminho XPath do campo de senha.
botao_entrar='//*[@id="idSIButton9"]'  # Caminho XPath do botão de entrar.
botao_sim='//*[@id="idSIButton9"]'  # Caminho XPath do botão de confirmação ("Sim").
botao_atualizar='//*[@id="content"]/tri-shell/tri-item-renderer/tri-extension-page-outlet/div[2]/dataset-details-container/dataset-action-bar/action-bar/action-button[2]/button'  # Caminho XPath do botão de atualizar.
botao_atualizar_agora='//*[@id="mat-menu-panel-1"]/div/span[1]/button'  # Caminho XPath do botão "Atualizar agora".

# Interação com o formulário de login.
print("Preenchendo o email")
campo_email = wait.until(EC.presence_of_element_located((By.XPATH, email)))  # Aguarda até que o campo de email esteja presente na página.
campo_email.clear()  # Limpa o campo de email.
campo_email.send_keys(login_email)  # Preenche o campo de email com o email obtido do .env.
time.sleep(3)  # Aguarda 3 segundos para garantir que a ação foi realizada.

# Clicar no botão enviar.
print("Clicando no botão enviar")
campo_botao_enviar = wait.until(EC.element_to_be_clickable((By.XPATH, botao_enviar)))  # Aguarda até que o botão de enviar esteja clicável.
campo_botao_enviar.click()  # Clica no botão enviar.
time.sleep(3)  # Aguarda 3 segundos.

# Preencher a senha.
print("Preenchendo a senha")
campo_senha = wait.until(EC.presence_of_element_located((By.XPATH, senha)))  # Aguarda até que o campo de senha esteja presente.
campo_senha.clear()  # Limpa o campo de senha.
campo_senha.send_keys(login_password)  # Preenche o campo de senha com a senha do .env.
time.sleep(3)  # Aguarda 3 segundos.

# Clicar no botão entrar.
print("Clicando no botão entrar")
campo_botao_entrar = wait.until(EC.element_to_be_clickable((By.XPATH, botao_entrar)))  # Aguarda até que o botão de entrar esteja clicável.
campo_botao_entrar.click()  # Clica no botão entrar.
time.sleep(3)  # Aguarda 3 segundos.

# Confirmar a permanência logado.
print("Clicando no botão sim")
campo_botao_sim = wait.until(EC.element_to_be_clickable((By.XPATH, botao_sim)))  # Aguarda até que o botão de confirmação esteja clicável.
campo_botao_sim.click()  # Clica no botão de confirmação.
time.sleep(10)  # Aguarda 5 segundos.

# Clicar no botão atualizar.
print("Clicando no botão atualizar")
campo_botao_atualizar = wait.until(EC.element_to_be_clickable((By.XPATH, botao_atualizar)))  # Aguarda até que o botão atualizar esteja clicável.
campo_botao_atualizar.click()  # Clica no botão atualizar.
time.sleep(3)  # Aguarda 3 segundos.

# Clicar no botão atualizar agora.
print("Clicando no botão atualizar agora")
campo_botao_atualizar_agora = wait.until(EC.element_to_be_clickable((By.XPATH, botao_atualizar_agora)))  # Aguarda até que o botão "Atualizar agora" esteja clicável.
campo_botao_atualizar_agora.click()  # Clica no botão "Atualizar agora".
time.sleep(3)  # Aguarda 3 segundos.

# Mensagem indicando que a atualização foi realizada com sucesso.
print("Atualização realizada com sucesso")
# Fecha o navegador.
driver.quit()  # Encerra o driver e fecha o navegador.
