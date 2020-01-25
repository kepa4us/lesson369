import time

def test_find_card_button(browser):
    browser.implicitly_wait(12)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button > 0, 'No button'