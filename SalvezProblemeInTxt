import time
from selenium import webdriver
import pyautogui as pe
import  os
import  subprocess
from selenium.webdriver.common.keys import Keys

Chrome = webdriver.Firefox(executable_path="D:\geckodriver-v0.28.0-win64\geckodriver.exe")
username = "BandB"
password = "3000probleme"
PbInfo = "https://www.pbinfo.ro/"
Solutie = "https://www.pbinfo.ro/?pagina=solutie-oficiala&id="

def Login(Driver, username, parola):
    Driver.find_element_by_id("user").send_keys(username)
    Driver.find_element_by_id("parola").send_keys(parola)
    Driver.find_element_by_xpath("//*[@id=\"form-login\"]/div/div[2]/div[4]/button").click()
    time.sleep(2)

def Valid(driver):
    if  "numai de utilizatorii care au rezolvat complet " in driver.page_source:
        return 0
    return 1
def SaveProblem(name):
    pe.moveTo(920, 800, 0.2)
    pe.rightClick();
    pe.hotkey('w', 't')
    pe.typewrite(name)
    pe.press('enter')
    pe.press('enter')
    time.sleep(0.2)
    pe.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pe.hotkey('ctrl', 'w')
    pe.press('enter')
    
Chrome.get(PbInfo)
time.sleep(2)
Login(Chrome, username, password)

os.startfile("D:\Websites\EuSuntBob\Probleme")

for index in range (3541, 3750):
    Chrome.get(Solutie + str(index))
    time.sleep(1)
    if Valid(Chrome):
        if not ("Problema nu exista.." in Chrome.page_source  or " problema invalid" in Chrome.page_source):
            while("unknown error" in Chrome.page_source):
                Chrome.get(Solutie + str(index))

            text = Chrome.find_element_by_css_selector(".nav-stacked").text

            cuv = '';

            for i in text:
                cuv = cuv + i
                if '\n' in i:
                    if "Python" in cuv:
                        x = Chrome.find_element_by_css_selector(".code_python")
                    if "Pascal" in cuv:
                        x = Chrome.find_element_by_css_selector(".code_pascal")
                        break
                    elif "C++" in cuv:
                        x = Chrome.find_element_by_css_selector(".code_cpp")
                        break
                    elif 'C' in cuv:
                        x = Chrome.find_element_by_css_selector(".code_c")
                        break
                    else:
                        cuv = ''

            x.click()
            x.send_keys(Keys.CONTROL, 'a')
            x.send_keys(Keys.CONTROL, 'c')
            time.sleep(0.5)
            SaveProblem(str(index))
            time.sleep(0.5)
