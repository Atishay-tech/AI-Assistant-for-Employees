import json
from time import sleep
from selenium import webdriver
try:
    from core_func import update_info
    from core_func.config import PATH
except:
    import update_info
    from cofig import PATH


#PATH = 'C:\\Users\\Atishay\\Desktop\\Final year project\\env\\chromedriver.exe'
URL = 'http://127.0.0.1:5000/login/'
INFO_PATH = 'config.json'


def get_info(path: str) -> dict:
    try:
        file = open(path)

    except FileNotFoundError:
        update_info.exec()
        file = open(path)

    details = json.load(file)
    file.close()

    return details

def exec(query: str='Open site'):
    details = get_info(INFO_PATH)

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    global browser
    browser = webdriver.Chrome(executable_path=PATH, options=options)
    browser.maximize_window()
    browser.get(URL)

    browser.find_element_by_name('id').send_keys(details['id'])
    browser.find_element_by_name('password').send_keys(details['password'])
    browser.find_element_by_id(details['category']).click()

    return browser

if __name__ == '__main__':
    browser = exec()
    sleep(10)
    browser.quit()