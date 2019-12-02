import sys
import time

from pync import Notifier

import urllib
import urllib.request
import urllib.error
from selenium import webdriver


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        self.got_redirect = False

    def http_error_302(self, req, fp, code, msg, headers):
        info_url = urllib.request.addinfourl(fp, headers, req.get_full_url())
        info_url.status = code
        info_url.code = code
        self.got_redirect = True
        return info_url

    http_error_300 = http_error_302
    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302


def get_login_page_url_from_redirect():
    no_redirect_handler = NoRedirectHandler()
    handlers = [
        no_redirect_handler,
    ]
    opener = urllib.request.build_opener(*handlers)
    req = urllib.request.Request('http://www.apple.com')
    response = opener.open(req)
    return response.headers.get('Location')


Notifier.notify(
    'Starting login process...',
    title='Telekom Hotspot')

hotspot_login_page = get_login_page_url_from_redirect()

if hotspot_login_page == 'https://www.apple.com/':
    Notifier.notify(
        'Already have an internet connection!',
        title='Telekom Hotspot')
    time.sleep(1.5)
    Notifier.remove()
    sys.exit(0)

print('The hotspot login page is: ')
print(hotspot_login_page)

email = 'change@me.com'
pw = 'changeme'

d = webdriver.Chrome()
d.implicitly_wait(10)
d.get(hotspot_login_page)

time.sleep(2)

d.find_element_by_xpath('//*[@id="tab-container"]/div[1]/div/div/a[4]').click()
d.find_element_by_xpath(
    '//*[@id="tab-tab-login-hotspot"]/div[1]/div/form/div[1]/div[1]/input') \
    .send_keys(email)
d.find_element_by_xpath(
    '//*[@id="tab-tab-login-hotspot"]/div[1]/div/form/div[1]/div[2]/input') \
    .send_keys(pw)

# clicking the 'Eingeloggt bleiben' checkbox which does not seem to work but
# we try anyway!
d.find_element_by_xpath(
    '//*[@id="tab-tab-login-hotspot"]/'
    'div[1]/div/form/div[2]/div/div[1]/label').click()

# clicking the 'Online gehen' button
d.find_element_by_xpath(
    '//*[@id="tab-tab-login-hotspot"]/div[1]/div/form/button').click()

Notifier.notify('Logged in!', title='Telekom Hotspot')

time.sleep(1.5)
Notifier.remove()

d.quit()
