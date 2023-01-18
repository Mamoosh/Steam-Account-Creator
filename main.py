import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from datetime import datetime
from PIL import Image
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from telethon import TelegramClient

chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
#chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works

from telethon import TelegramClient, events

def captcha_from_telegram(captcha_code):
    # Use my.telegram.org
    api_id = 
    api_hash = ''
    
    captcha = captcha_code
    with TelegramClient('anon', api_id, api_hash) as client:
        @client.on(events.NewMessage)
        async def my_event_handler(event):
            captcha = event.raw_text
            f = open("captcha.txt", "w")
            f.write(event.raw_text)
            f.close()
            if event.raw_text != None and event.raw_text != '' :
                captcha = event.raw_text
                client.disconnect()
        client.start()
        client.run_until_disconnected()
    f = open("captcha.txt", "r")
    captcha_code = f.read()
    return captcha_code


def get_mail(browser_1 , mail):
    tries = 50
    i = 0
    while tries > 0 :
        browser_1.get("https://tempmail.email/")
        browser_1.implicitly_wait(10)
        path = '/html/body/div[2]/div/div[1]/div[3]/div/div[2]'
        browser_1.implicitly_wait(10)
        element = browser_1.find_elements_by_xpath(path)
        browser_1.implicitly_wait(10)
        i += 1
        if element[0].text != "":
            mail = element[0].text
            tries = 0
            if re.search('gotgel', mail):
                print("gotgel again!")
                browser_1.close()
                browser_1 = webdriver.Chrome(executable_path=r"/home/admin-u3f/Desktop/pythonProject7/chromedriver",options=chrome_options)
                browser_1, mail = get_mail(browser_1, mail)
        tries -= 1
    return browser_1, mail


def signup_steam(browser_2 , mail):
    captcha_code = ""
    email_patch = '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[2]/div/input'
    confirm_email_patch = '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[3]/div/input'
    confirm_rules_patch = '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[6]/div[1]/label/input'
    browser_2.get("https://store.steampowered.com/join/")
    in1 = browser_2.find_element_by_xpath(email_patch)
    in1.send_keys(mail)
    in2 = browser_2.find_element_by_xpath(confirm_email_patch)
    in2.send_keys(mail)
    in3 = browser_2.find_element_by_xpath(confirm_rules_patch).click()
    browser_2.implicitly_wait(10)

    #browser_2 , captcha_code = captcha_accept(browser_2,captcha_code)
    next = input("waiting for enter!")
    #inter_captcha = browser_2.find_element_by_xpath("/html/body/div/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[5]/div/div[2]/div[1]/input")
    #inter_captcha.send_keys(captcha_code)
    next_con = browser_2.find_element_by_xpath("/html/body/div/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[6]/div[2]/button/span")
    next_con.click()
    return browser_2,mail


def email_confirm(browser_1):
    email_confirm_steam_path = '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[2]/div'
    steam_mail_path = '/html/body/div[2]/div/div[1]/div[4]/div[3]/div[4]/center[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a'
    in4 = browser_1.find_element_by_xpath(email_confirm_steam_path).click()
    browser_1.implicitly_wait(10)
    in5 = browser_1.find_element_by_xpath(steam_mail_path).click()
    browser_1.implicitly_wait(10)


def enter_info(browser_2):
    password = user = ""
    user , password = user_pass(user, password)
    save_user_pass(user, password)
    browser_2.implicitly_wait(10)
    in6 = browser_2.find_element_by_id('accountname')
    time.sleep(1)
    browser_2.implicitly_wait(10)
    in6.send_keys(user)
    browser_2.implicitly_wait(10)
    in7 = browser_2.find_element_by_id('password')
    time.sleep(1)
    browser_2.implicitly_wait(10)
    in7.send_keys(password)
    browser_2.implicitly_wait(10)
    in8 = browser_2.find_element_by_id('reenter_password')
    time.sleep(1)
    browser_2.implicitly_wait(10)
    in8.send_keys(password)
    browser_2.implicitly_wait(10)
    in9 = browser_2.find_element_by_id("createAccountButton").click()


def user_pass(user, password):
    file = open('user.txt', 'r')
    file_val = file.read()
    file.close()
    pre = 'csu3faccc23_'
    val = int(file_val.replace(pre, ''))
    new_val = str(val + 1)
    file = open('user.txt', 'w')
    res = pre + new_val
    file.write(res)
    user = res
    file = open('pass.txt', 'r')
    file_val = file.read()
    file.close()
    pre = 'acu3fpss_'
    last_pass_num = int(file_val.replace(pre, ''))
    val = str(last_pass_num + 1)
    file = open('pass.txt', 'w')
    res = pre + val
    file.write(res)
    password = res
    return user, password

def save_user_pass(user,password):
    file = open('accounts.txt', 'a')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    format = user + " " + password  + " " + current_time + "\n"
    file.write(format)
    file.close()
    file = open('login_format.txt', 'a')
    format = user + "\n" + password + "\n" + "\n"
    file.write(format)
    file.close()

def captcha_accept(browser_2 , captcha_code):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    img_add = "captcha_images/" + current_time + ".png"
    browser_2.implicitly_wait(10)

    browser_2.implicitly_wait(10)
    time.sleep(1)

    img = browser_2.find_element_by_xpath(
        '/html/body/div/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[5]/div/div[2]/div[1]/img')
    browser_2.implicitly_wait(10)
    with open(img_add, 'wb') as file:
        file.write(img.screenshot_as_png)
    with TelegramClient('anon', 8080176, 'cd6eb6fa338343201e3bd3da1e1c5e73') as client:
        client.loop.run_until_complete(client.send_file('@yourid', img_add))
    browser_2.implicitly_wait(10)

    captcha_code = captcha_from_telegram(captcha_code)

    print(captcha_code)
    os.remove(img_add)
    return browser_2 , captcha_code


def my_prog():
    mail = password = user = ""
    browser_1 = webdriver.Chrome(executable_path=r"/home/user/Desktop/pythonProject7/chromedriver",options=chrome_options)
    browser_1 , mail = get_mail(browser_1 , mail)
    print(mail)

    browser_2 = webdriver.Chrome(executable_path=r"/home/user/Desktop/pythonProject7/chromedriver",options=chrome_options)
    browser_2 , mail = signup_steam(browser_2 , mail)
    email_confirm(browser_1)
    browser_1.close()
    enter_info(browser_2)
    browser_2.close()
    print("ACCOUNT HAS CREATED!")

    api_id = 
    api_hash = ''
    with open('login_format.txt', 'r') as f:
        lines = f.read().splitlines()
        password_line = lines[-2]
        print(password_line)
        username_line = lines[-3]
        print(username_line)

    with TelegramClient('anon', api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message('@yourid', '----Account Created!----'))
        client.loop.run_until_complete(client.send_message('@yourid', username_line))
        client.loop.run_until_complete(client.send_message('@yourid', password_line))



while True:
    try: my_prog()
    except: print("ERROR")