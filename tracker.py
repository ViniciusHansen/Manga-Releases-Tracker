from selenium import webdriver


def reset_settings():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    global driver
    driver = webdriver.Chrome(options=chrome_options)


def main():
    print('\nBuscando Dados...\n')
    reset_settings()
    for manga in mangas:
        driver.get(manga)
        data_ultimo_cap = driver.find_element_by_xpath(
            '//*[@id="chapter-list"]/div[2]/ul/li[1]/a/div[1]/span')
        numero_ultimo_cap = driver.find_element_by_xpath(
            '//*[@id="chapter-list"]/div[2]/ul/li[1]/a/div[2]/div/span[1]')
        link = driver.find_element_by_xpath(
            '//*[@id="chapter-list"]/div[2]/ul/li[1]/a').get_attribute("href")
        print(driver.title[:-27])
        print(
            f'Último capítulo: {numero_ultimo_cap.text[-3::]}, publicado em: {data_ultimo_cap.text} \n{link}\n\n')
        driver.close()
        reset_settings()
    driver.quit()


mangas = (
    'https://mangalivre.net/manga/black-clover/1751',
    'https://mangalivre.net/manga/solo-leveling/7702',
    'https://mangalivre.net/manga/boku-no-hero-academia/1319'
)

if __name__ == '__main__':
    main()
