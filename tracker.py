from selenium import webdriver
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)

mangas = {
    'Black Clover': 'https://mangalivre.net/manga/black-clover/1751',
    'Solo Leveling': 'https://mangalivre.net/manga/solo-leveling/7702',
    'Boku no Hero': 'https://mangalivre.net/manga/boku-no-hero-academia/1319'
}

print('\n')
print('Buscando Dados...')
print('\n')

for manga in mangas:
    driver.get(mangas[manga])
    time.sleep(1.5)
    data_ultimo_cap = driver.find_element_by_xpath(
        '//*[@id="chapter-list"]/div[2]/ul/li[1]/a/div[1]/span')
    numero_ultimo_cap = driver.find_element_by_xpath(
        '//*[@id="chapter-list"]/div[2]/ul/li[1]/a/div[2]/div/span[1]')
    link = driver.find_element_by_xpath(
        '//*[@id="chapter-list"]/div[2]/ul/li[1]/a').get_attribute("href")

    print(driver.title)
    print('-' * 48)
    print('Último capítulo: {}, publicado em: {} \n{}'.format(
        numero_ultimo_cap.text[-3::], data_ultimo_cap.text, link))
    print('\n')

driver.quit()
