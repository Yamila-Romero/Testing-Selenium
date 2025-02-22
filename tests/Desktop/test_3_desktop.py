from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from utils.product_interactions import wait_for_element
from utils.product_interactions import wait_for_element_to_be_visible_and_clickable
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from page.home import configHome
from dotenv import load_dotenv

load_dotenv()

CHECKOUT_DATA = load_test_data("test_data.json")["checkout"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
WAIT_TIME = 20
PRODUCT_XPATH = "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a"
ADD_TO_CART_XPATH = "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button"
CHECKOUT_BUTTON_LINK = "Proceed to checkout" 
CHECKOUT_BUTTON_XPATH = "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a"
CHECKOUT_BUTTON2_XPATH = "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a"
ADDRESS_ID = "field-address1"
FIELD_ID = "field-postcode"
CITY_ID = "field-city"
STATE_ID = "field-id_state"
CONFIRM_DELIVERY_NAME = "confirmDeliveryOption"
CONFIRM_ADDRESS_NAME = "confirm-addresses"
CONDITIONS_TO_APPROVE_ID = "conditions_to_approve[terms-and-conditions]"

def test_main3(driver):
    configHome(driver,url=APP_URL, device = DEVICE["desktop"])

    # Arrange
    wait_for_element(driver, By.XPATH, PRODUCT_XPATH)

    # Act
    product1 = driver.find_element(By.XPATH, PRODUCT_XPATH)
    product1.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.XPATH, ADD_TO_CART_XPATH)
    addtocartButton = driver.find_element(By.XPATH, ADD_TO_CART_XPATH)
    addtocartButton.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.XPATH, CHECKOUT_BUTTON_XPATH)
    checkoutButton = driver.find_element(By.XPATH, CHECKOUT_BUTTON_XPATH)
    checkoutButton.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.XPATH, CHECKOUT_BUTTON2_XPATH)
    checkoutButton2 = driver.find_element(By.XPATH, CHECKOUT_BUTTON2_XPATH)
    checkoutButton2.click()

    wait_for_element(driver, By.ID, ADDRESS_ID)
    
    addressBox = driver.find_element(By.ID, ADDRESS_ID)
    postcodeBox = driver.find_element(By.ID, FIELD_ID)
    cityBox = driver.find_element(By.ID, CITY_ID)

    addressBox.send_keys(CHECKOUT_DATA["address"])
    postcodeBox.send_keys(CHECKOUT_DATA["postcode"])
    cityBox.send_keys(CHECKOUT_DATA["city"])

    wait_for_element(driver, By.ID, STATE_ID)
    stateBox = driver.find_element(By.ID, STATE_ID)
    select = Select(stateBox)
    select.select_by_value(CHECKOUT_DATA["state_value"])

    deliveryButton = driver.find_element(By.NAME, CONFIRM_ADDRESS_NAME)
    deliveryButton.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.NAME, CONFIRM_DELIVERY_NAME)
    continueButton2 = driver.find_element(By.NAME, CONFIRM_DELIVERY_NAME)
    continueButton2.click()

    wait_for_element_to_be_visible_and_clickable(driver, By.ID, "conditions-to-approve")
    payment1Button = driver.find_element(By.ID, CONDITIONS_TO_APPROVE_ID)
    payment1Button.click()

    # Assert
    assert payment1Button.is_selected(), "El botón no se seleccionó después del clic."
    
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

