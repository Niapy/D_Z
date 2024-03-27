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

def test_successfull_logg_phone(driver):
   # Вводим email
   driver.find_element("id", 'username').send_keys('9941095254')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('Colbaska201400001')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.CLASS_NAME, "user-name__last-name").text == "Сахаров"

def test_unsuccessfull_logg_phone_password(driver):
   # Вводим email
   driver.find_element("id", 'username').send_keys('9941095254')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('Colbaska2014')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"

def test_unsuccessfull_logg_phone_number(driver):
   # Вводим email
   driver.find_element("id", 'username').send_keys('phonenumber')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('Colbaska201400001')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"

def test_successfull_logg_email(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="t-btn-tab-mail"]').click()
   driver.find_element("id", 'username').send_keys('dru_dps_5k@yahoo.com')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('Colbaska201400001')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.CLASS_NAME, "user-name__last-name").text == "Сахаров"

def test_unsuccessfull_logg_email_password(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="t-btn-tab-mail"]').click()
   driver.find_element("id", 'username').send_keys('dru_dps_5k@yahoo.com')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('201400001')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"

def test_unsuccessfull_logg_email(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="t-btn-tab-mail"]').click()
   driver.find_element("id", 'username').send_keys('dru_5k@yahoo.com')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('Colbaska201400001')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"

def test_successfull_logg_by_login(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="t-btn-tab-login"]').click()
   driver.find_element("id", 'username').send_keys('rtkid_1711456651393')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('Colbaska201400001')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.CLASS_NAME, "user-name__last-name").text == "Сахаров"

def test_unsuccessfull_logg_by_login(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="t-btn-tab-login"]').click()
   driver.find_element("id", 'username').send_keys('1711456651393')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('Colbaska201400001')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"

def test_unsuccessfull_logg_by_login_password(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="t-btn-tab-login"]').click()
   driver.find_element("id", 'username').send_keys('rtkid_1711456651393')
   # Вводим пароль
   driver.find_element("id", 'password').send_keys('Colba0001')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="kc-login"]').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"

