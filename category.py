import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def input_category(driver):
    flag = True
    while flag:
        print("КАТЕГОРИИ\n1 - Мы рекомендуем\n2 - Популярное\n3 - Японская кухня\n4 - Итальянская кухня\n"
              "5 - Морепродукты\n6 - Лапша\n7 - Бенто ланчи\n8 -  Салаты\n9 - Супы\n10 - Брускеты\n"
              "11 - Ингредиенты\n12 - Канапе\n13 - Десерты\n14 - Напитки\n0 - Оформить заказ\n")
        op = input("Введите категорию для заказа\n")
        match op.lower():
            case "1":
                category("recommendrecommend", driver)
            case "2":
                category("popularpopular", driver)
            case "3":
                flag_case = True
                while flag_case:
                    print("1 - Роллы\n2 - Запеченные суши и ролы\n3 - Суши\n4 - Вернуться назад\n")
                    op_category = input("Выберите подкатегорию\n")
                    match op_category.lower():
                        case "1":
                            category("rolly518854", driver)
                        case "2":
                            category("zapechyonnye-sushi-i-rolly518853", driver)
                        case "3":
                            category("sushi518861", driver)
                        case _:
                            flag_case = ending()
                    print("\n")
            case "4":
                flag_case = True
                while flag_case:
                    print("1 - Пицца\n2 - Паста\n3 - Вернуться назад\n")
                    op_category = input("Выберите подкатегорию\n")
                    match op_category.lower():
                        case "1":
                            category("pizza518874", driver)
                        case "2":
                            category("pasta518875", driver)
                        case "3":
                            flag_case = False
                        case _:
                            flag_case = ending()
                    print("\n")
            case "5":
                category("moreprodukty518862", driver)
            case "6":
                category("lapsha518869", driver)
            case "7":
                category("bento-lanchi518868", driver)
            case "8":
                category("salaty518855", driver)
            case "9":
                category("supy518866", driver)
            case "10":
                category("brusketty518867", driver)
            case "11":
                flag_case = True
                while flag_case:
                    print("1 - Соус\n2 - Бакалея\n3 - Морепродукты и икра\n4 - Вернуться назад\n")
                    print("Для выхода нажмите n")
                    op_category = input("Выберите подкатегорию\n")
                    match op_category.lower():
                        case "1":
                            category("sousy518860", driver)
                        case "2":
                            category("bakaleya518859", driver)
                        case "3":
                            category("moreprodukty-i-ikra518858", driver)
                        case _:
                            flag_case = ending()
                    print("\n")
            case "12":
                category("kanape518863", driver)
            case "13":
                category("deserty518864", driver)
            case "14":
                category("napitki518865", driver)
            case "0":
                chek(driver)
                break
            case _:
                flag = ending()


def category(name, driver):
    action_Chains = ActionChains(driver)
    wait = WebDriverWait(driver, 3)
    products = driver.find_elements(By.XPATH, f"//div[@id='{name}']/div/div/div/div/div/h4/label")
    id_products = 0
    for product in products:
        id_products += 1
        print(f"{id_products} = {product.text}")
    choise_product = input("Введите номер продукта\n")
    button = driver.find_element(By.XPATH, f'//div[@id="{name}"]/div/div[{choise_product}]/div[2]/div[1]/div')
    action_Chains.click(button).perform()
    time.sleep(5)

    button = wait.until(ec.element_to_be_clickable((By.XPATH, f'//div[@id="{name}"]/div/div[{choise_product}]/div[2]/div[1]/div')))
    action_Chains.click(button).perform()
    print("Кнопка уже нажата")

    while True:
        print("Вы хотите увеличить количество на 1?\n")
        col = input("Если да нажмите +, если нет -\n")
        if col == "+":
            dop = driver.find_element(By.XPATH, '//div[@class = "options__wrapper"]/div[2]/div/button[2]')
            action_Chains.click(dop).perform()
        else:
            break
    end = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div[2]/button/div')
    action_Chains.double_click(end).perform()


def ending():
    print("Хотите продолжить заказ?")
    end = input("Если нет - нажмите n, если да - нажмите y: ")
    if end.lower() == "n":
        return False


def chek(driver):
    action_Chains = ActionChains(driver)
    basket = driver.find_element(By.XPATH, '//div[@class="popover__relative"]/button[@type="button"]/div[2]')
    action_Chains.click(basket).perform()
    time.sleep(3)
    driver.save_screenshot("cheking.png")
    time.sleep(3)
    order = driver.find_element(By.XPATH, '//div[@class = "cart-wrapper"]/button')
    action_Chains.click(order).perform()
    telephone = driver.find_element(By.ID, '//input[@placeholder = "Телефон"]')
    input_telephone = int(input("Введите номер телефона\n+7-"))
    telephone.send_keys(input_telephone)
    input_chek = driver.find_element(By.XPATH, '//*[@id="topBar"]/div/div/div[2]/div/div/div[2]/form/div[2]/div/button[1]')
    action_Chains.click(input_chek).perform()

