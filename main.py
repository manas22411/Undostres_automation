from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


##########  ALL Variable required #########
PHONE_NUMBER=8465433546
DOLLAR=10
OPERATOR='Mega Tel'
CARD_NUMBER=4111111111111111
MONTH=11
YEAR=25
CVV=111
EMAIL='test@test.com'
SAL_DRIVER_PATH='C:\selenium crome driver\chromedriver.exe'
WEB_URL='https://prueba.undostres.com.mx/'
USERNAME_SIGN='automationUDT1@gmail.com'
PASS_SIGN='automationUDT123'
TIMEOUT=30

dict_front_page={
    'phone_xpath':'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[1]/div/div/input',
    'operator_xpath':'/html/body/div[3]/div[2]/div[2]/div/div[1]/form/div/div[1]/div[1]/div[2]/ul/li[2]/div/div/input',
    'operator_sel_xpath':'/html/body/div[3]/div[2]/div[2]/div/div[1]/form/div/div[1]/div[1]/div[2]/ul/li[2]/div/div/div/ul/li[6]/a',
    'recharge_plan':'/html/body/div[3]/div[2]/div[2]/div/div[1]/form/div/div[1]/div[1]/div[2]/ul/li[3]/div/div/div/ul/li[1]/a',
    'follow_button':'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[3]/div/button'
}

dict_pay_page={
    'card_mode_xpath':'/html/body/div[35]/div[1]/div[3]/div/div[1]/div/div/div[2]/div[1]/div/a/div/div',
    'new_user_but_xpath':'//*[@id="radio-n"]/td/label/a',
    'card_number_xpath':'//*[@id="cardnumberunique"]',
    'pay_mon_xpath':'//*[@id="payment-form"]/div[3]/div[1]/div/div[1]/input',
    'pay_yr_xpath':'//*[@id="payment-form"]/div[3]/div[1]/div/div[3]/input',
    'pay_cvv_xpath':'//*[@id="payment-form"]/div[3]/div[2]/div/input',
    'email_xpath':'/html/body/div[35]/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/table/tbody/tr[2]/td/div/div/div[2]/form/div[4]/div/div/input',
    'payment_but':'/html/body/div[35]/div[1]/div[3]/div/div[2]/div/div/div[6]/div/button'

}


dict_reg_page={
    'username_xpath':'/html/body/div[5]/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[1]/form/div[1]/input',
    'pass_xpath':'/html/body/div[5]/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[1]/form/div[2]/input',
    'captch_xpath':'/html/body/div[5]/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[1]/form/div[4]',
    'acess_but-xpath':'/html/body/div[5]/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[1]/form/button'

}

def web_server_conn(url):
    ser = Service(SAL_DRIVER_PATH)
    browser = webdriver.Chrome(service=ser)
    browser.get(url)
    return browser


def find_element_xpath(url, browser):

    return browser.find_element(by=By.XPATH,value=url)

def find_element_id(ID,browser):

    return browser.find_element(by=By.ID,value=ID)


def main():
    try:
        browser=web_server_conn(WEB_URL)

        browser.implicitly_wait(10)

        #  ....  1st Page automation  .... #

        phone = find_element_xpath(dict_front_page['phone_xpath'],browser)
        phone.send_keys(PHONE_NUMBER)                                                        # inserting phone number


        click_oper= find_element_xpath(dict_front_page['operator_xpath'],browser)            # viewing the operator list
        click_oper.click()
        time.sleep(0.5)

        sel_oper= find_element_xpath(dict_front_page['operator_sel_xpath'],browser)           # selecting the operator
        sel_oper.click()
        time.sleep(0.5)

        plan=find_element_xpath(dict_front_page['recharge_plan'],browser)                     #selecting operator plan
        plan.click()

        submit =find_element_xpath(dict_front_page['follow_button'],browser)   #moving to Payment page
        submit.click()


        # .... Verify if the user is able to reach the next screen ....#

        #  ....  2st Page Payment automation  .... #

        card_mode= find_element_xpath(dict_pay_page['card_mode_xpath'],browser)                 #selecting payment mode
        card_mode.click()

        time.sleep(0.5)
        new_user= find_element_xpath(dict_pay_page['new_user_but_xpath'],browser)
        new_user.click()

        time.sleep(0.5)
        card_number= find_element_xpath(dict_pay_page['card_number_xpath'],browser)                #inserting CARD NUMBER
        card_number.send_keys(CARD_NUMBER)

        card_mon= find_element_xpath(dict_pay_page['pay_mon_xpath'],browser)
        card_mon.send_keys(MONTH)

        card_yr=find_element_xpath(dict_pay_page['pay_yr_xpath'],browser)
        card_yr.send_keys(YEAR)

        card_cvv=find_element_xpath(dict_pay_page['pay_cvv_xpath'],browser)
        card_cvv.send_keys(CVV)


        email=find_element_xpath(dict_pay_page['email_xpath'],browser)
        email.send_keys(EMAIL)

        pay_button=find_element_xpath(dict_pay_page['payment_but'],browser)
        pay_button.click()



        # ..... 3rd Sign In page automation .... #

        username_sign=find_element_xpath(dict_reg_page['username_xpath'],browser)
        username_sign.send_keys(USERNAME_SIGN)

        pass_sign= find_element_xpath(dict_reg_page['pass_xpath'],browser)
        pass_sign.send_keys(PASS_SIGN)

        captch=find_element_xpath(dict_reg_page['captch_xpath'],browser)
        captch.click()

        time.sleep(2)

        submit=find_element_xpath(dict_reg_page['acess_but-xpath'],browser)
        submit.click()

        time.sleep(20)
    except Exception as e:
        print('Exception had occur Please try again ',e)


if __name__ == "__main__":
    main()