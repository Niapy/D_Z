import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   driver.implicitly_wait(5)
   # Переходим на страницу авторизации
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=945c546c-feca-4408-bf51-65d15238c5dd&theme&auth_type')

   driver.maximize_window()
   yield driver

   driver.quit()

def test_password_recovery(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="forgot_password"]').click()
   assert driver.find_element(By.TAG_NAME, 'H1').text == "Восстановление пароля"

def test_region_check(driver):
   # Вводим email
   driver.find_element("id", 'username').send_keys('9941095254')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('Colbaska201400001')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element("xpath", '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[4]/div/span[2]/span').text == "Приморский край"