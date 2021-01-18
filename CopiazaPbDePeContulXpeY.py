import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Chrome = webdriver.Chrome(executable_path="D:\chromedriver_win32 (2)\chromedriver.exe") #plm stie ce i ala da asa zic baietii de la selenium
Firefox = webdriver.Firefox(executable_path="D:\geckodriver-v0.28.0-win64\geckodriver.exe") #pe asta copiez 3000 de pb
#InternetExplorer = webdriver.Ie(executable_path="D:\IEDriverServer_x64_3.150.1\IEDriverServer.exe") #mai incet ca bunica

PbInfo = "https://www.pbinfo.ro/" #unde imi fac eu veacul
InfoArena = "https://infoarena.ro/"
""""
Chrome.get(PbInfo)
Firefox.get(InfoArena)

print(Chrome.title) #titlu bro
print(Firefox.title) #alt titlu bro

Chrome.close()
Firefox.close()

astea le las asa ca na
"""

Chrome.get(PbInfo)
Firefox.get(PbInfo)

usernameA = "Borod"
parolaA = "abcde"
usernameB = "BB"
parolaB = "probleme"

def Login(Driver, username, parola):
    Driver.find_element_by_id("user").send_keys(username)
    Driver.find_element_by_id("parola").send_keys(parola)
    Driver.find_element_by_xpath("//*[@id=\"form-login\"]/div/div[2]/div[4]/button").click()
    time.sleep(2)

def CautPb(Driver, NrProblema):
    Driver.get("https://www.pbinfo.ro/probleme/" + str(NrProblema))

"""
for index in range (1, 3570):
    CautPb(Chrome,index)
    CautPb(Firefox,index)
"""


def SolMea(Driver):
    Sol = Driver.find_element_by_css_selector("table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > label:nth-child(1) > kbd:nth-child(1)").text
    Sol = Sol.replace("#", "")
    NewUrl = "https://www.pbinfo.ro/detalii-evaluare/" + Sol
    Driver.get(NewUrl)

def CopyProblem(driver) :
    SolvedProblem = driver.find_element_by_css_selector(".code_cpp")
    SolvedProblem.send_keys(Keys.CONTROL, 'a')
    time.sleep(1)
    SolvedProblem.send_keys(Keys.CONTROL, 'c')

def WriteProblem(driver) :
    message = driver.find_element_by_xpath("//*[@id=\"form-incarcare-solutie\"]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div/pre")
    message.click()
    message.send_keys(Keys.CONTROL, 'v')
    driver.find_element_by_id("btn-submit").click()
    time.sleep(1)

def isproblem(driver) :
    if driver.title == "www.pbinfo.ro" :
        return 0
    else :
        return 1

Login(Firefox, usernameA, parolaA)
Login(Chrome, usernameB, parolaB)

x = 0
x = int(x)

for index in range (3460, 3750):
    CautPb(Firefox,index)
    if(isproblem(Firefox)):
        if("Soluția oficială" in Firefox.page_source):
            CautPb(Chrome, index)
            SolMea(Firefox)
            CopyProblem(Firefox)
            time.sleep(1.5)
            WriteProblem(Chrome)
            time.sleep(2.5)
