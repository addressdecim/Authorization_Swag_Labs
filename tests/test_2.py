from base import action
from locators import locator
from url import check_url
from date import data_text, eror

act = action.EnterTheSite()
rtrn = action.ReturnPath()


def authorization_test_2(browser):
    print("authorization_test_2 start")
    browser.refresh()
    assert browser.current_url == check_url.url_start
    rtrn.get_path_wait(browser, locator.button_login).click()
    print("Click button Login")
    assert rtrn.get_path_wait(browser, locator.txt_eror).text == eror.eror_login
    print(rtrn.get_path_wait(browser, locator.txt_eror).text)
    rtrn.get_path_wait(browser, locator.button_eror).click()
    print("Error remove")
    print("authorization_test_2 end \n")
 
