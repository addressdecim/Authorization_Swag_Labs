from base import action
from locators import locator
from url import check_url
from date import data_text, eror

act = action.EnterTheSite()
rtrn = action.ReturnPath()


def authorization_test_1(browser):
    print("authorization_test_1 start")
    act.enter_the_site(browser, check_url.url_start)
    assert browser.current_url == check_url.url_start
    rtrn.get_path_wait(browser, locator.user_name).send_keys(data_text.login_standard_user)
    print("Username: Input login")
    rtrn.get_path_wait(browser, locator.password).send_keys(data_text.password)
    print("Password: Input password")
    rtrn.get_path_wait(browser, locator.button_login).click()
    print("Click button Login")
    assert browser.current_url == check_url.url_main
    print(f"URL Главной страницы {check_url.url_main} \n")
    rtrn.get_path_wait(browser, locator.button_burger).click()
    rtrn.get_path_wait(browser, locator.button_logout).click()
    print("Logout")
    assert browser.current_url == check_url.url_start
    print("authorization_test_1 end")
    

