from selenium import webdriver
from selenium.webdriver.common.by import By
import category
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def open_website():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    url = "https://shop.foodsoul.pro/"
    driver = webdriver.Chrome(options=options)
    try:
        driver.maximize_window()

        driver.get(url=url)
        input_pickup = WebDriverWait(driver, 20).until(ec.presence_of_element_located
                                                      ((By.XPATH, "//*[contains(text(), 'Самовывоз')]")))
        input_pickup.click()
        input_place = driver.find_element(By.XPATH, '//div[@class = "simplebar-offset"]/div/div/ul/li[2]')
        input_place.click()
        category.input_category(driver)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
