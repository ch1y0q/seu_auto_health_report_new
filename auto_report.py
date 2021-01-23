from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter.messagebox
import random
import sys
import string
import random
import base64

browser = webdriver.Chrome('./webdriver/chromedriver.exe')
browser.implicitly_wait(300)


# base64 decode your password in case you use a bat to run the script
# and are afraid of password being stored in plaintext
def decode(s):
    return base64.b64decode(s).decode('ascii')


try:
    # get username and password from arguments
    if len(sys.argv) < 3:
        print('Usage: python auto_report.py USERNAME PASSWORD')
        raise Exception('arguments less than 2')
    elif len(sys.argv) == 4:
        if sys.argv[3]:
            USERNAME = sys.argv[1]
            PASSWORD = decode(sys.argv[2])
        else:
            USERNAME = sys.argv[1]
            PASSWORD = sys.argv[2]
    else:
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]

    browser.get('http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/index.do')

    # browser.maximize_window()

    fields = browser.find_elements_by_class_name('auth_input')

    fields[0].send_keys(USERNAME)
    fields[1].send_keys(PASSWORD)
    time.sleep(1)

    login_btn = browser.find_elements_by_class_name('auth_login_btn')
    login_btn[0].click()
    time.sleep(5)

    # add
    submit_btn = browser.find_element_by_css_selector("div.bh-btn-primary")
    submit_btn.click()
    time.sleep(15)

    # random body temperature
    input_fields = browser.find_elements_by_tag_name('input')
    for i in input_fields:
        if i.get_attribute("name").find("DZ_JSDTCJTW") >= 0:
            # scroll down until body temperature textfield is visible
            browser.execute_script("arguments[0].scrollIntoView();", i)

            i.click()
            i.send_keys(str(random.randint(362, 370) / 10.0))
            break
    time.sleep(10)

    # save
    save_btn = browser.find_element_by_css_selector("div#save.bh-btn.bh-btn-primary")
    time.sleep(5)
    save_btn.click()
    time.sleep(5)

    # confirm
    confirm_btn = browser.find_element_by_css_selector("a.bh-dialog-btn.bh-bg-primary.bh-color-primary-5")
    confirm_btn.click()
    time.sleep(5)
    # tkinter.messagebox.showinfo("成功", "成功填报健康情况。")
    browser.quit()

except Exception as e:
    print(e)
    tkinter.messagebox.showerror("未能填报", "出现错误，未能自动填报。请手动操作。")
    browser.quit()
