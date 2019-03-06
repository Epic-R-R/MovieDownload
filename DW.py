#==================================== Description ===============================
#Author :
 #   SaLaR[Epic_R_R]
#Script Details :
 #   search and choose randomly a movie from 250 top rate movies in IMDB and
 #   download .torrent file for you !!!!!;) to download that an Watch ;)[Enjoy That]
#How To Download:
 #   for download movie with .torrent file you must use special software. Example:  qbittorrent
 #                                                                                               ;)
 #Telegram Channel: T.me/allhak
#==================================== Library ==========================================
from selenium import webdriver
import random
import time
import pyscreenshot as ImageGrab
from os import  system
import wget
import os
from pySmartDL import SmartDL
#==================================== Main ======================================
driver = webdriver.Chrome("/home/epic_r_r/Desktop/Movie/chromedriver")

def browser(url):
    driver.maximize_window()
    driver.get(url)

urlIMDB = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

browser(urlIMDB)

list_movies = []
for i in range(1,251):
    element = driver.find_element_by_xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr['+str(i)+']/td[2]/a')
    list_movies.append(element.text)
    print(str(i)+": "+element.text)

print("================================")

movie = list_movies[random.randint(1,250)]
time.sleep(1)
print("I choose this movie for watch this time => {}".format(movie))

movie = movie.replace(" ", "+")

browser("https://rarbg.to/torrents.php?search="+str(movie)+"&order=leechers&by=DESC")
time.sleep(6)
driver.find_element_by_xpath("/html/body/div/div/a").click()
time.sleep(6)
im = ImageGrab.grab(bbox=(690,330,840,390))

im.save('/home/epic_r_r/Desktop/Movie/capcha.png')
print("================================")
time.sleep(3)
print("Attack Capcha: ")
system('tesseract /home/epic_r_r/Desktop/Movie/capcha.png /home/epic_r_r/Desktop/Movie/capcha')
time.sleep(2)
f = open("/home/epic_r_r/Desktop/Movie/capcha.txt")
lines = f.readlines()
capcha = lines[0]
print("================================")
print("Extract Capcha = {}".format(capcha))
driver.find_element_by_xpath('//*[@id="solve_string"]').send_keys(capcha)
print("ByPass Capcha Complated.")
print("================================")
time.sleep(1)
browser("https://rarbg.to/torrents.php?search="+str(movie)+"&order=leechers&by=DESC")
print("================================")
print("Search for movie")
driver.find_element_by_xpath('/html/body').click()
driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[2]/a[1]').click()
time.sleep(2)
urlTorrent = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/a[1]').get_attribute('href')
print("Get Torrent : {}".format(urlTorrent))
driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/a[1]').click()
print("Download Movie Torrent: ")
time.sleep(3)
dest = "/home/epic_r_r/Desktop/Movie/TorrentDownloads/"
obj = SmartDL(urlTorrent,dest)
driver.close()
obj.start()
path = obj.get_dest()
time.sleep(2)
time.sleep(1)
print("Epic_R_R")
time.sleep(0.5)
print("T.me/allhak")
time.sleep(0.5)
#-------------------------------------------------------------------Good Luck----------------------------------------------
