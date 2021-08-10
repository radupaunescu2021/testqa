from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging


@given('open browser')
def launch_browser(context):
    context.driver=webdriver.Chrome('/home/radu/Downloads/chromedriver')
    context.driver.get("https://www.demoblaze.com/index.html")


    context.placeOrderLocator='/html/body/div[6]/div/div[2]/button'
    context.finishedTransactionLocator='/html/body/div[10]/p'
    context.submitFormLocator='/ html / body / div[3] / div / div / div[3] / button[2]'



@when('go to homepage')
def launch_browser(context):
    context.driver.get("https://www.demoblaze.com/index.html")



@when('navigate through product "{category}"')
def search_products(context,category):
    phoneElement =context.driver.find_element_by_link_text(category)
    phoneElement.click()

@when('add laptop "{laptop}"')
def add_laptop_cart(context,laptop):

    WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.LINK_TEXT, laptop))).click()

    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Add to cart'))).click()

    WebDriverWait(context.driver, 20).until(EC.alert_is_present())
    alert=context.driver.switch_to.alert
    alert.accept()

    context.driver.switch_to.default_content


@when('go to cart')
def go_to_cart(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, 'cartur'))).click()



@when('delete laptop "{laptop}"')
def delete_laptop(context,laptop):
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//td[.='"+laptop+"']")))
    laptopELem=context.driver.find_element_by_xpath("//td[.='"+laptop+"']")

    deleteButton=laptopELem.find_element_by_xpath('..').find_element_by_link_text('Delete')
    deleteButton.click()
    sleep(2)
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID,"totalp")))
    context.total=context.driver.find_element_by_id("totalp").text

@when('place order')
def place_order(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, context.placeOrderLocator))).click()

    nameElement=WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, 'name')))
    nameElement.send_keys(context.table.rows[0]["name"])
    countryElem=WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, 'country')))
    countryElem.send_keys(context.table.rows[0]["country"])
    cityElem=WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, 'city')))
    cityElem.send_keys(context.table.rows[0]["city"])
    cardElem=WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, 'card')))
    cardElem.send_keys(context.table.rows[0]["card"])
    monthElem=WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, 'month')))
    monthElem.send_keys(context.table.rows[0]["month"])
    yearElem=WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, 'year')))
    yearElem.send_keys(context.table.rows[0]["month"])

    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,context.submitFormLocator))).click()



@then('verify amount')
def check_results(context):
   result=WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, context.finishedTransactionLocator)))
   id=result.text.splitlines()[0]
   amount=result.text.splitlines()[0]
   logging.info(result.text.splitlines()[0] + " "+result.text.splitlines()[1])
   logging.info("")
   assert context.total in result.text.splitlines()[1]


