from selenium import webdriver
import time
import os
import win32clipboard
project_name=input('your project name:  ') 
os.mkdir(f'D:\\{project_name}')
uname=''
pwd=''
driver=webdriver.Chrome()
driver.get('https://github.com')
login_btn=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
login_btn.click()
time.sleep(1)
username= driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[2]')
username.send_keys(uname)
password=driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[3]')
password.send_keys(pwd)
finallogin=driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[14]')
finallogin.click()
newrepobtn=driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a')
newrepobtn.click()
reponame=driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input')
reponame.send_keys(project_name)
time.sleep(5)
create=driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
create.click()
time.sleep(3)
gitkey=driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/git-clone-help/div[1]/div/div[4]/div/span/span/clipboard-copy')
gitkey.click()
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
#print (data)
proj='#'+project_name
os.chdir(f"D:\\{project_name}")
os.system(f'echo {project_name} >> README.md')
os.system('git init')
os.system('git add README.md')
os.system('git commit -m "first commit"')
os.system('git branch -M main')
os.system(f'git remote add origin {data}')
os.system('git push -u origin main')
driver.quit()
