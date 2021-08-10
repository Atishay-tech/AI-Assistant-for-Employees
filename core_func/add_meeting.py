from time import sleep
from core_func import open_site
from speech import VoiceEngine

def exec(query: str='Projects'):
    engine = VoiceEngine()

    details = dict()
    print('Enter the following details:')
    engine.speak('Enter the following details:')
    details['date'] = input('Date: ')
    details['time'] = input('Time: ')
    details['info'] = input('Info: ')
    details['employees'] = input('Employees: ')
    
    global browser
    browser = open_site.exec()

    for key, value in details.items():
        browser.find_element_by_xpath("//form[@id='addmeeting']//input[@name='{}']".format(key)).send_keys(value)
    browser.find_element_by_xpath("//form[@id='addmeeting']//input[@type='submit']").click()

    return browser


if __name__ == '__main__':
    browser = exec()
    sleep(5)
    browser.quit()