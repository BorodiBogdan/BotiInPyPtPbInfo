import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#srh
UrlZeceLaInfo = "https://www.zecelainfo.com/2972/"

def LogIn(driver, username, pasword) :
    driver.find_element_by_id("user").send_keys(username)
    driver.find_element_by_id("parola").send_keys(pasword)
    driver.find_element_by_xpath("//*[@id=\"form-login\"]/div/div[2]/div[4]/button").click()
    time.sleep(3)

def isproblem(driver) :
    if driver.title == "www.pbinfo.ro":
        return 0
    else :
        return 1

def GetPbId(driver) :
    CurString = str(driverChrome.title)
    NumberOfProblem = 0
    for i in range (0, len(CurString)) :
        if CurString[i].isdigit() == False :
            break
        else :
            NumberOfProblem = NumberOfProblem * 10 + int(CurString[i])
    return NumberOfProblem

driverFirefox = webdriver.Firefox(executable_path="D:\geckodriver-v0.28.0-win64\geckodriver.exe")
driverFirefox.get("https://www.pbinfo.ro/")
LogIn(driverFirefox, "BB", "probleme")

driverChrome = webdriver.Firefox(executable_path="D:\geckodriver-v0.28.0-win64\geckodriver.exe")
driverChrome.get(UrlZeceLaInfo)

for NrOfProblem in range (1, 4001) :

    CurrUrl = driverChrome.current_url

    if "vignette" in CurrUrl: #pt reclama
        CurrUrl = CurrUrl[:-16]
        driverChrome.get(CurrUrl)


    PbId = GetPbId(driverChrome) #am aflat id pb

    UrlSolOf = "https://www.pbinfo.ro/probleme/" + str(PbId)
    driverFirefox.get(UrlSolOf) #intru cont
    if(isproblem(driverFirefox)):
        if not "Soluția oficială" in driverFirefox.page_source: #daca nu am pb
            copiedText = driverChrome.find_element_by_css_selector(".wp-block-preformatted").text
            message = driverFirefox.find_element_by_css_selector(".CodeMirror > div:nth-child(1) > textarea:nth-child(1)")
            copiedText = re.sub(' +', ' ', copiedText)
            message.send_keys(copiedText)
            driverFirefox.find_element_by_xpath("//*[@id=\"btn-submit\"]").click()
            time.sleep(13)

    driverChrome.find_element_by_css_selector(".nav-arrow").click()

    time.sleep(1)
