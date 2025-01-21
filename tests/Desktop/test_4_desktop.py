import page.home_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.product_interactions import wait_for_element_to_be_visible_and_clickable
from utils.product_interactions import wait_for_element
from utils.product_interactions import hover_and_add_to_cart
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from page.home import configHome
from page.checkout_page import CheckoutPage
from dotenv import load_dotenv

from utils.locators import CheckoutPageLocators

load_dotenv()

DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"


def test_main4(driver):

    CHECKOUT_BUTTON_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"
    #WAIT_TIME = 25
    PRODUCT_XPATH = "//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img"
    CART_CSS = "#_desktop_cart > div > div > a > span.hidden-sm-down"

    configHome(driver, url=APP_URL, device=DEVICE["desktop"])
    locators=CheckoutPageLocators()
    checkout_obj=CheckoutPage(driver)
    
   
    # Arrange
    wait_for_element(driver, By.XPATH, PRODUCT_XPATH)
    
    # Act
    hover_and_add_to_cart(driver,"//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[3]/article/div/div[1]/div/a")
    hover_and_add_to_cart(driver,"//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[6]/article/div/div[1]/div/a")
    hover_and_add_to_cart(driver,"//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/a/picture/img","//*[@id='content']/section[1]/div/div[7]/article/div/div[1]/div/a")   
    
    wait_for_element_to_be_visible_and_clickable(driver, By.CSS_SELECTOR, CART_CSS)
    gotoCart = driver.find_element(By.CSS_SELECTOR, CART_CSS)
    gotoCart.click()

    wait_for_element(driver, By.XPATH, CHECKOUT_BUTTON_XPATH)
    checkCartA = driver.find_element(By.XPATH, CHECKOUT_BUTTON_XPATH)
    checkCartA.click()
    
    checkout_obj.acc(*locators.CONFIRM_ADDRESS_NAME)
    checkout_obj.acc(*locators.CONFIRM_DELIVERY_NAME)
    checkout_obj.acc(*locators.CONDITIONS_TO_APPROVE_ID)

    
    # Assert
    cond_checkbox = driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]")
    assert cond_checkbox.is_selected(), "El botón no se seleccionó después del clic."
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)
