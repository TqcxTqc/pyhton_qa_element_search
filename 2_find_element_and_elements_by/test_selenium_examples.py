from locators import MainPage
from selenium.webdriver.common.action_chains import ActionChains


def test_element_by_class_name_selector(browser):
    browser.find_element_by_class_name("swiper-viewport").click()
    browser.find_element_by_class_name("breadcrumb")


def test_element_by_id(browser):
    browser.find_element_by_id("slideshow0").click()
    browser.find_element_by_class_name("breadcrumb")


def test_element_by_link_text(browser):
    desktops_link = browser.find_element_by_link_text("Desktops")
    ActionChains(browser).move_to_element(desktops_link).pause(2).perform()
    browser.find_element_by_link_text("Show All Desktops").click()
    browser.find_element_by_partial_link_text("Product Compare")


def test_elements_by_css_selector(browser):
    navbar_items = browser.find_elements_by_css_selector(MainPage.nav_links)
    for item in navbar_items:
        ActionChains(browser).move_to_element(item).pause(0.5).perform()


# def test_element_by_class_name_selector(parametrize_browser):
#     parametrize_browser.find_element_by_class_name("swiper-viewport").click()
#     parametrize_browser.find_element_by_class_name("breadcrumb")