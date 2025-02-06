#!/usr/bin/env python
import argparse
import pygame
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(args):
    cart_button_text = "addToCartButtonOrTextIdFor"
    item_id = "88897904"
    if args.id:
        item_id = args.id
    item_url = "https://www.target.com/p/pokemon-scarlet-violet-s3-5-booster-bundle-box/-/A-88897904"
    if args.url:
        item_url = args.url

    driver = webdriver.Chrome()

    username = ""
    password = ""

    # login lol
    driver.get("https://www.target.com/account")
    wait = WebDriverWait(driver, 30)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
    login_button.click()

    driver.get(item_url)
    
    buy_button = None
    while not buy_button:
        try:
            buy_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, f"{cart_button_text}{item_id}"))
            )
            buy_button.click()
            print("add to cart button clicked :3")
        except:
            print("not in stock, refreshing")
            driver.refresh()

    added_to_cart = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Added to cart']"))
    )
    print("item added to cart, navigating to checkout") 

    driver.get("https://target.com/checkout")

    pygame.mixer.init()
    pygame.mixer.music.load('tada.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, help='item id from url')
    parser.add_argument('--url', type=str, help='url to the item')
    args = parser.parse_args()

    main(args)
