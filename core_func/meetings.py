from time import sleep
try:
    from core_func import open_site
except:
    import open_site


def exec(query: str='Meetings'):
    global browser
    browser = open_site.exec()
    browser.find_element_by_id('meetings').click()

    return browser


if __name__ == '__main__':
    browser = exec()
    sleep(5)
    browser.quit()