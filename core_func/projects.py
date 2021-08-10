from time import sleep
try:
    from core_func.config import PATH
    from core_func import open_site
except:
    from config import PATH
    import open_site


def exec(query: str='Projects'):
    global browser
    browser = open_site.exec()
    browser.find_element_by_id('projects').click()

    return browser


if __name__ == '__main__':
    browser = exec()
    sleep(5)
    browser.quit()