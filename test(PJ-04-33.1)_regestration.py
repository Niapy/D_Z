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

def test_wrong_first_name(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="kc-register"]').click()
   driver.find_element("name", 'firstName').send_keys('125')
   # Вводим пароль
     # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span'). text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_wrong_last_name(driver):
    # Вводим email
    driver.find_element("xpath", '//*[@id="kc-register"]').click()
    driver.find_element("name", 'lastName').send_keys('125')
    # Вводим пароль
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element("xpath",
                               '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_wrong_email(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="kc-register"]').click()
   driver.find_element("id", 'address').send_keys('dru_dps_5kyahoo.com')
   # Вводим пароль
     # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span'). text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

def test_wrong_phone_number(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="kc-register"]').click()
   driver.find_element("id", 'address').send_keys('91475898')
   # Вводим пароль
     # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span'). text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

def test_wrong_password(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="kc-register"]').click()
   driver.find_element("name", 'password').send_keys('914')
   # Вводим пароль
     # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'). text == "Длина пароля должна быть не менее 8 символов"

def test_wrong_password(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="kc-register"]').click()
   driver.find_element("name", 'password').send_keys('914002548ффф')
   # Вводим пароль
     # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'). text == "Пароль должен содержать только латинские буквы"

def test_wrong_password(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="kc-register"]').click()
   driver.find_element("name", 'password').send_keys('colbaska00002050')
   # Вводим пароль
     # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'). text == "Пароль должен содержать хотя бы одну заглавную букву"

def test_wrong_password_conformation(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="kc-register"]').click()
   driver.find_element("name", 'firstName').send_keys('Дмитрий')
   driver.find_element("name", 'lastName').send_keys('Сахаров')
   driver.find_element("id", 'address').send_keys('dru_dps_5k@yahoo.com')
   driver.find_element("name", 'password').send_keys('Colbaska00002050')
   # Вводим пароль
   driver.find_element("name", 'password-confirm').send_keys('Colbaska000')
     # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/button').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span'). text == "Пароли не совпадают"

def test_wrong_password(driver):
   # Вводим email
   driver.find_element("xpath", '//*[@id="kc-register"]').click()
   driver.find_element("name", 'firstName').send_keys('Дмитрий')
   driver.find_element("name", 'lastName').send_keys('Сахаров')
   driver.find_element("id", 'address').send_keys('dru_dps_5k@yahoo.com')
   driver.find_element("name", 'password').send_keys('Colbaska00002050')
   # Вводим пароль
   driver.find_element("name", 'password-confirm').send_keys('Colbaska00002050')
     # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '//*[@id="page-right"]/div/div[1]/div/form/button').click()
      # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.TAG_NAME, 'H2').text == "Учётная запись уже существует"



