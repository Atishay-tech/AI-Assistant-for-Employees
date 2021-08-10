from time import sleep
from core_func import open_site
from speech import VoiceEngine

def exec(query: str='Projects'):
    engine = VoiceEngine()

    details = dict()
    print('Enter the following details:')
    engine.speak('Enter the following details:')
    details['id'] = input('Project ID: ')
    details['name'] = input('Project Name: ')
    details['date'] = input('Deadline: ')
    details['info'] = input('Description: ')
    details['employees'] = input('Employee ID\'s: ')
    
    global browser
    browser = open_site.exec()

    for key, value in details.items():
        browser.find_element_by_xpath("//form[@id='addproject']//input[@name='{}']".format(key)).send_keys(value)
    browser.find_element_by_xpath("//form[@id='addproject']//input[@type='submit']").click()

    return browser


if __name__ == '__main__':
    browser = exec()
    sleep(5)
    browser.quit()