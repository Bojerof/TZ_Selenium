from selenium.webdriver.common.by import By
import commands
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Web_site:
    def __init__(self, driver):
        self.driver = driver

    def open_website(self):
        url = "https://shop.foodsoul.pro/"
        command = commands.Commands(self.driver)
        try:
            self.driver.maximize_window()

            self.driver.get(url=url)
            input_pickup = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located
                            ((By.XPATH, "//*[contains(text(), 'Самовывоз')]")))
            input_pickup.click()
            input_place = self.driver.find_element(By.XPATH, '//div[@class = "simplebar-offset"]/div/div/ul/li[2]')
            input_place.click()
            command.input_category()

        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()
