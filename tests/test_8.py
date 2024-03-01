from base import action
from locators import locator
from url import check_url
from date import data_text, eror

act = action.EnterTheSite()
rtrn = action.ReturnPath()


def authorization_test_8(browser):
    print("authorization_test_8 start")
    browser.refresh()
    assert browser.current_url == check_url.url_start
    rtrn.get_path_wait(browser, locator.user_name).send_keys(data_text.login_standard_user)
    print("Username: Input login")
    rtrn.get_path_wait(browser, locator.password).send_keys(data_text.password[:-2])
    print("Password: Input partial password")
    rtrn.get_path_wait(browser, locator.button_login).click()
    print("Click button Login")
    assert rtrn.get_path_wait(browser, locator.txt_eror).text == eror.incorrect_login_password
    print(rtrn.get_path_wait(browser, locator.txt_eror).text)
    rtrn.get_path_wait(browser, locator.button_eror).click()
    print("Error remove")
    print("authorization_test_8 end \n")
