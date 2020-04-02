from selenium import webdriver
import time
import excelmod
from os import *

driver = webdriver.Chrome()
# system("touch Proj.xlsx")
driver.get("https://summerofcode.withgoogle.com/archive/2019/projects/")


path = "./Abcd.xlsx"
excelmod.write(path,'Sheet1',1,1,"Name")
excelmod.write(path,'Sheet1',1,2,"Organisation")
excelmod.write(path,'Sheet1',1,3,"Project")
r=3
for k in range(12):
    a=driver.find_element_by_tag_name("main")
    m=a.find_elements_by_tag_name("li")
    for i in m:
        b=i.find_element_by_tag_name("div")
        excelmod.write(path,'Sheet1',r,1,b.find_element_by_tag_name("a").text)
        excelmod.write(path,'Sheet1',r,2,b.find_elements_by_tag_name("div")[1].text)
        excelmod.write(path,'Sheet1',r,3,b.find_elements_by_tag_name("div")[0].text)
        r=r+1
    print("Page No. of the page Scrapped is ",k+1)
    if k<11:        
        nextbtn = driver.find_element_by_xpath("//a[text()='Next']")
        nextbtn.click()