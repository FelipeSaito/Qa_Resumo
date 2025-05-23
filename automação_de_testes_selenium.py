# Automação de testes com Selenium permite simular ações humanas em navegadores, como clicar, preencher formulários e validar elementos. É ideal para testar interfaces web
# automaticamente, garantindo que funcionalidades importantes, como login, buscas ou compras, funcionem corretamente. Usar Selenium reduz erros manuais, economiza tempo e melhora
# a eficiência nos testes.

!pip install selenium
!apt-get update
!apt-get install -y chromium-chromedriver chromium-browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1200')

driver = webdriver.Chrome(service=Service(), options=chrome_options)

driver.get("https://www.python.org/")

assert "Python" in driver.title
print("Página carregada com sucesso!")

search_box = driver.find_element(By.ID, "id-search-field")
search_box.send_keys("selenium")
search_box.submit()

time.sleep(2)

results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
assert len(results) > 0
print(f"Encontrados {len(results)} resultados para 'selenium'.")

driver.quit()
