from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Commands:
    def __init__(self, driver):
        self.driver = driver

    def input_category(self):
        flag = True
        while flag:
            print("КАТЕГОРИИ\n1 - Мы рекомендуем\n2 - Популярное\n3 - Японская кухня\n4 - Итальянская кухня\n"
                  "5 - Морепродукты\n6 - Лапша\n7 - Бенто ланчи\n8 -  Салаты\n9 - Супы\n10 - Брускеты\n"
                  "11 - Ингредиенты\n12 - Канапе\n13 - Десерты\n14 - Напитки\n0 - Оформить заказ\n")
            op = input("Введите категорию для заказа\n")
            match op.lower():
                case "1":
                    self.category("recommendrecommend")
                case "2":
                    self.category("popularpopular")
                case "3":
                    flag_case = True
                    while flag_case:
                        print("1 - Роллы\n2 - Запеченные суши и ролы\n3 - Суши\n4 - Вернуться назад\n")
                        op_category = input("Выберите подкатегорию\n")
                        match op_category.lower():
                            case "1":
                                self.category("rolly518854")
                            case "2":
                                self.category("zapechyonnye-sushi-i-rolly518853")
                            case "3":
                                self.category("sushi518861")
                            case _:
                                flag_case = self.ending()
                        print("\n")
                case "4":
                    flag_case = True
                    while flag_case:
                        print("1 - Пицца\n2 - Паста\n3 - Вернуться назад\n")
                        op_category = input("Выберите подкатегорию\n")
                        match op_category.lower():
                            case "1":
                                self.category("pizza518874")
                            case "2":
                                self.category("pasta518875")
                            case "3":
                                flag_case = False
                            case _:
                                flag_case = ending()
                        print("\n")
                case "5":
                    self.category("moreprodukty518862")
                case "6":
                    self.category("lapsha518869")
                case "7":
                    self.category("bento-lanchi518868")
                case "8":
                    self.category("salaty518855")
                case "9":
                    self.category("supy518866")
                case "10":
                    self.category("brusketty518867")
                case "11":
                    flag_case = True
                    while flag_case:
                        print("1 - Соус\n2 - Бакалея\n3 - Морепродукты и икра\n4 - Вернуться назад\n")
                        print("Для выхода нажмите n")
                        op_category = input("Выберите подкатегорию\n")
                        match op_category.lower():
                            case "1":
                                self.category("sousy518860")
                            case "2":
                                self.category("bakaleya518859")
                            case "3":
                                self.category("moreprodukty-i-ikra518858")
                            case _:
                                flag_case = self.ending()
                        print("\n")
                case "12":
                    self.category("kanape518863")
                case "13":
                    self.category("deserty518864")
                case "14":
                    self.category("napitki518865")
                case "0":
                    self.check()
                    break
                case _:
                    flag = self.ending()

    def category(self, name):
        action_Chains = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 3)
        products = self.driver.find_elements(By.XPATH, f"//div[@id='{name}']/div/div/div/div/div/h4/label")
        id_products = 0
        for product in products:
            id_products += 1
            print(f"{id_products} = {product.text}")
        choise_product = input("Введите номер продукта\n")
        button = self.driver.find_element(By.XPATH, f'//div[@id="{name}"]/div/div[{choise_product}]/div[2]/div[1]/div')
        action_Chains.click(button).perform()
    
        button = wait.until(ec.element_to_be_clickable((By.XPATH, f'//div[@id="{name}"]/div/div[{choise_product}]/div[2]/div[1]/div')))
        action_Chains.click(button).perform()
        print("Кнопка уже нажата")
    
        while True:
            print("Вы хотите увеличить количество на 1?\n")
            col = input("Если да нажмите +, если нет -\n")
            if col == "+":
                dop = self.driver.find_element(By.XPATH, '//div[@class = "options__wrapper"]/div[2]/div/button[2]')
                action_Chains.click(dop).perform()
            else:
                break
        end = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div[2]/button/div')
        action_Chains.double_click(end).perform()

    @staticmethod
    def ending():
        print("Хотите продолжить заказ?")
        end = input("Если нет - нажмите n, если да - нажмите y: ")
        if end.lower() == "n":
            return False
        else:
            return True

    def check(self):
        wait = WebDriverWait(self.driver, 4)
        action_Chains = ActionChains(self.driver)
        basket = wait.until(ec.element_to_be_clickable((By.XPATH, '//div[@class="popover__relative"]/button[@type="button"]/div[2]')))
        action_Chains.click(basket).perform()
        self.driver.save_screenshot("checking.png")
        order = self.driver.find_element(By.XPATH, '//div[@class = "cart-wrapper"]/button')
        action_Chains.click(order).perform()
        telephone = wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@placeholder = "Телефон"]')))
        input_telephone = input("Введите номер телефона\n+7-")
        telephone.send_keys(input_telephone)
        input_check = self.driver.find_element(By.XPATH, '//*[@id="topBar"]/div/div/div[2]/div/div/div[2]/form/div[2]/div/button[1]')
        action_Chains.click(input_check).perform()
