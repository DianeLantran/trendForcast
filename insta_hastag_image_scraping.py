#!/usr/bin/env python
# coding: utf-8

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass
import wget
import os
import shutil

#dossier où stocker les images, remplacer le chemin par l'endroit où vous voulez stocker vos images sur votre machine
dest_loc = r'C:\Users\diane\Documents\documents\TSE\FISE2\Semestre2\trendForcast\instaPictures'

i = 0

#création d'un driver
PATH = "C:\Program Files\drivers\chromedriver_105.exe"
driver = webdriver.Chrome(PATH)

# #site1
# driver.get("https://www.istockphoto.com/fr/search/2/image?mediatype=&phrase=fashon&utm_source=pixabay&utm_medium=affiliate&utm_campaign=SRP_image_sponsored&utm_content=https%3A%2F%2Fpixabay.com%2Ffr%2Fimages%2Fsearch%2Ffashon%2F&utm_term=fashon/")
# driver.maximize_window()
# sleep(3)

# #accepte les cookies
# acceptCookiesbutton = driver.find_element(By.XPATH,"//button[@id='onetrust-accept-btn-handler']")
# acceptCookiesbutton.click()

# #detection des images affichées sur la page
# sleep(4)
# images = driver.find_elements(By.XPATH,"//img[@class='klD9EcerqfLV_08xYBJi']")

# #création du tableau où on va enregistrer les images
# my_images = set()

# #on descend petit a petit dans la page et on enregistre toutes les images qu'on voit
# while True:
#     for image in images:
#         source = image.get_attribute('src')
#         my_images.add(source)
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#     sleep(3)
#     images = driver.find_elements(By.XPATH,"//img[@class='klD9EcerqfLV_08xYBJi']")
#     if len(my_images)>50:
#         break

# print(len(my_images))

	
# for image in my_images:
#     wget.download(image,dest_loc)


#site 2
driver.get("https://www.stocklib.fr/search?keyword=trend+clothes&media_type=0")
driver.maximize_window()
sleep(3)


images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")


my_images = set()

while True:
    for image in images:
        source = image.get_attribute('src')
        my_images.add(source)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")
    if len(my_images)>50:
        break

print(len(my_images))


for image in my_images:
    wget.download(image,dest_loc)


#site 3
driver.get("https://www.stocklib.fr/search?keyword=mode&media_type=0&page=2")
driver.maximize_window()
sleep(3)


images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")
my_images = set()

while True:
    for image in images:
        source = image.get_attribute('src')
        my_images.add(source)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")
    if len(my_images)>50:
        break

print(len(my_images))


for image in my_images:
    wget.download(image,dest_loc)

#site 4
driver.get("https://www.stocklib.fr/search?keyword=fashion+week&media_type=0")
driver.maximize_window()
sleep(3)


images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")


my_images = set()

while True:
    for image in images:
        source = image.get_attribute('src')
        my_images.add(source)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")
    if len(my_images)>50:
        break

print(len(my_images))

for image in my_images:
    wget.download(image,dest_loc)

#site 5
driver.get("https://www.stocklib.fr/search?keyword=mode&media_type=0&page=4")
driver.maximize_window()
sleep(3)


images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")


my_images = set()

while True:
    for image in images:
        source = image.get_attribute('src')
        my_images.add(source)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")
    if len(my_images)>50:
        break

print(len(my_images))

for image in my_images:
    wget.download(image,dest_loc)

#site 6
driver.get("https://www.stocklib.fr/search?keyword=mode&media_type=0&page=9")
driver.maximize_window()
sleep(3)


images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")


my_images = set()

while True:
    for image in images:
        source = image.get_attribute('src')
        my_images.add(source)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")
    if len(my_images)>50:
        break

print(len(my_images))

for image in my_images:
    wget.download(image,dest_loc)


#site 7
driver.get("https://www.stocklib.fr/search?keyword=model+fashion&media_type=0")
driver.maximize_window()
sleep(3)


images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")


my_images = set()

while True:
    for image in images:
        source = image.get_attribute('src')
        my_images.add(source)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    images = driver.find_elements(By.XPATH,"//img[@class='lazy-content']")
    if len(my_images)>50:
        break

print(len(my_images))

for image in my_images:
    wget.download(image,dest_loc)

