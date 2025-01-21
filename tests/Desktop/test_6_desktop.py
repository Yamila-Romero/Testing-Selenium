# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from dotenv import load_dotenv
# from page.home import configHome
# from utils.test_data_loader import load_test_data
# import time
# import os
# from selenium.webdriver.common.action_chains import ActionChains
# import test_1_desktop
# import test_2_desktop
# import test_3_desktop

# # Cargar variables de entorno
# load_dotenv()

# # Cargar los datos de prueba
# LANGUAGE_DATA = load_test_data("test_data.json")["language"]
# print(LANGUAGE_DATA)  
# DEVICE = load_test_data("test_data.json")["device"]

# # Función para cambiar el idioma de la página
# def change_language(driver, language):
#         # Configurar el home
#     configHome(driver, url="APP_URL", device=DEVICE["desktop"])
#     quickView = driver.find_element(By.XPATH, "//*[@id='_desktop_language_selector']")
#     hover= ActionChains(driver).move_to_element(quickView)
#     hover.perform()
#     quickView.click()
   
#     # Esperar a que las opciones estén disponibles y hacer clic en el idioma
#     time.sleep(2)

#     quickView2 = driver.find_element(By.XPATH,language)
#     hover2= ActionChains(driver).move_to_element(quickView2)
#     hover2.perform()
#     quickView2.click()
#     time.sleep(10)
#     # Ejecutar pruebas en diferentes páginas
   
#     test_1_desktop.test_user_registration(driver)  # Página de registro
#     time.sleep
#     navigate_through_sections(driver)

# @pytest.mark.parametrize("language", [LANGUAGE_DATA["spanish"], LANGUAGE_DATA["italian"]])
# def test_main6(driver, language):
   
#     # Cambiar el idioma
#     change_language(driver, language=LANGUAGE_DATA["spanish"])
#     time.sleep(10)
#     # Cambiar el idioma
#     change_language(driver, language=LANGUAGE_DATA["italian"])

# def navigate_through_sections(driver):
#     # Navegar al primer elemento
#     driver.switch_to.default_content()

#     configHome(driver, url="APP_URL", device=DEVICE["desktop"])
#     quickView = driver.find_element(By.XPATH, "//*[@id='category-3']/a")
#     hover = ActionChains(driver).move_to_element(quickView)
#     hover.perform()
#     quickView.click()
   
#     # Desplazar hacia abajo en la página
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")  # Ajusta el valor según lo necesario
#     time.sleep(2)
#     # Navegar al segundo elemento
#     quickView = driver.find_element(By.XPATH, "//*[@id='link-cms-page-1-2']")
#     hover = ActionChains(driver).move_to_element(quickView)
#     hover.perform()
#     quickView.click()
   
#     home_button = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH,"//*[@id='_desktop_logo']/a/img"))
#             )
#     home_button.click()
#     time.sleep(5)
#     driver.delete_all_cookies()
#     driver.refresh()
