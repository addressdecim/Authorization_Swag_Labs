from selenium import webdriver
from tests import test_1, test_2, test_3, test_4, test_5, test_6, test_7, test_8, test_9


def authorization(browser):
    print("Start authorization tests")
    test_1.authorization_test_1(browser)
    test_2.authorization_test_2(browser)
    test_3.authorization_test_3(browser)
    test_4.authorization_test_4(browser)
    test_5.authorization_test_5(browser)
    test_6.authorization_test_6(browser)
    test_7.authorization_test_7(browser)
    test_8.authorization_test_8(browser)
    test_9.authorization_test_9(browser) 
    print("End authorization tests")
auth = authorization(webdriver.Chrome())