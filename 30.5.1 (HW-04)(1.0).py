import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   driver.implicitly_wait(5)
   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   driver.maximize_window()
   yield driver

   driver.quit()

def test_show_all_pets(driver):
   # Вводим email
   driver.find_element("id", 'email').send_keys('dru_dps_5k@yahoo.com')
   # Вводим пароль
   driver.find_element("id", 'pass').send_keys('colbaska2014')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element("xpath", '/html/body/div[1]/div/form/div[3]/button').click()
      # Проверяем, что мы оказались на главной странице пользователя
   driver.find_element("xpath", '//*[@id="navbarNav"]/ul/li[1]/a').click()
   assert driver.find_element(By.TAG_NAME, 'H2').text == "niapy"

   images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   for i in range(len(names)):
       image_source = images[i].get_attribute('src')
       name_text = names[i].text
       assert image_source != ''
       assert names[i].text != ''
       assert descriptions[i].text != ''


