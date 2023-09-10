from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


##########################################################


cookie_id = "cookie"
cursor_id = "buyCursor"
cursor_xpath = '//*[@id="buyCursor"]/b/text()[2]'
grandma_id = "buyGrandma"
grandma_xpath = '//*[@id="buyGrandma"]/b/text()[2]'
factory_id = "buyFactory"
factory_xpath = '//*[@id="buyFactory"]/b/text()[2]'
mine_id = "buyMine"
mine_xpath = '//*[@id="buyMine"]/b/text()[2]'
shipment_id = "buyShipment"
shipment_xpath = '//*[@id="buyShipment"]/b/text()[2]'
alchemy_id = "buyAlchemy lab"
alchemy_path = '//*[@id="buyAlchemy lab"]/b/text()[2]'
portal_id = "buyPortal"
portal_xpath = '//*[@id="buyPortal"]/b/text()[2]'
time_machine_id = "buyTime machine"
time_machine_xpath = '//*[@id="buyTime machine"]/b/text()[2]'
cookie_amount_id = "money"
cps_id = "cps"




##########################################################


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

CHROME_DRIVER_PATH = "/Users/bruce/Dev/chromedriver"
s=Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


##########################################################


cookie = driver.find_element(By.ID, cookie_id)




cursor= driver.find_element(By.ID, cursor_id)

grandma = driver.find_element(By.ID, grandma_id)

factory = driver.find_element(By.ID, factory_id)

mine = driver.find_element(By.ID, mine_id)

shipment = driver.find_element(By.ID, shipment_id)

alchemy = driver.find_element(By.ID, alchemy_id)


portal = driver.find_element(By.ID, portal_id)

time_machine = driver.find_element(By.ID, time_machine_id)


# print(time_machine_price)


##########################################################


#LOOP

# timeout variable can be omitted, if you use specific value in the while condition
timeout = time.time() + 5   # [seconds]
one_min= time.time() + 60

timeout_start = time.time()
play = True
times = 0

cps = driver.find_element(By.ID, cps_id)
item_ids = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab",
            "buyPortal", "buyTime machine"]

#############################################
while True:
    cookie.click()

    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []


        for price in all_prices:
            element_text = price.text
            print(element_text)
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)


        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        print(cookie_upgrades)

        cookie_money = driver.find_element(By.ID, cookie_amount_id).text
        if "," in cookie_money:
            cookie_money = cookie_money.replace(",", "")
        cookie_count = int(cookie_money)
        print(cookie_count)

        affordable_upgrades = {}
        for key, value in cookie_upgrades.items():
            if cookie_count > key:
                affordable_upgrades[key] = value
        print(cookie_upgrades.items())
        print(affordable_upgrades)


        highest_price_affordable_upgrade = max(affordable_upgrades)

        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()


        timeout = time.time() + 5


    if time.time() >one_min:
        print(cps)
        break

        # if cookie_money > time_machine_price:
        #     time_machine.click()
        # elif cookie_money > portal_price:
        #     portal.click()
        # elif cookie_money > alchemy_price:
        #     alchemy.click()
        # elif cookie_money > shipment_price:
        #     shipment.click()
        # elif cookie_money > mine_price:
        #     mine.click()
        # elif cookie_money > factory_price:
        #     factory.click()
        # elif cookie_money > grandma_price:
        #     grandma.click()
        # elif cookie_money > cursor_price:
        #     cursor.click()
        # else:
        #     cookie.click()




##########################################################
##########################################################


# search1 = driver.find_element(By.NAME, "fName")
# search1.send_keys("Bruce")
# search4 = driver.find_element(By.CSS_SELECTOR, "form button")
# search4.click()

# time.sleep(5)
