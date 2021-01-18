import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Chrome = webdriver.Chrome(executable_path="D:\chromedriver_win32 (2)\chromedriver.exe") da-l in pl Chrome
Chrome = webdriver.Firefox(executable_path="D:\geckodriver-v0.28.0-win64\geckodriver.exe")  # pe asta copiez 3000 de pb

Profiles = []
OneMessage = []

def Login(Driver, username, parola):
    Driver.find_element_by_id("user").send_keys(username)
    Driver.find_element_by_id("parola").send_keys(parola)
    Driver.find_element_by_xpath("//*[@id=\"form-login\"]/div/div[2]/div[4]/button").click()
    time.sleep(2)

def IsProblem(Driver):
    if "problema nu exista" in Driver.page_source:
        return 0
    if "care au rezolvat complet" in Driver.page_source:
        return 1
    return 0

def FindProfiles(Driver, Sol):
    Chrome.get(Sol)
    PageSource = Driver.page_source
    PageSource = PageSource.split('\n')
    cnt = 0
    p = 0
    p = int(p)
    cnt = int(cnt)
    for line in PageSource:
        if line.find("<a href=\"/profil/") != -1 and cnt > 2:
            line = line[25:]
            line = line[:len(line) - 2]
            p += 1
            if not line in Profiles and line != "500_IQ" and line != "May_9th":
                Profiles.append(line)
        elif line.find("<a href=\"/profil/") != -1:
            cnt += 1

PbInfo = "https://www.pbinfo.ro/"
SolPbInfo = "https://www.pbinfo.ro/solutii/problema/"
username = "BandB"
password = "3000probleme"
FirstMessage = "Salut!Ma poti ajuta te rog cu rezolvarea la problema "
SecondMessage = ".Iti voi ramane recunoscator.Multumesc mult!!!"
Contact = "https://www.pbinfo.ro/?pagina=conversatii&partener="

Chrome.get(PbInfo)

PbInfo = "https://www.pbinfo.ro/?pagina=solutie-oficiala&id="

Login(Chrome, username, password)
time.sleep(3)
unu = "https://www.pbinfo.ro/solutii/user/"

for index in range (1, 3750):
    NewUrl = PbInfo + str(index)
    Chrome.get(NewUrl)
    if not "ID problema invalid." in Chrome.page_source:
        if IsProblem(Chrome):
             NumePb = Chrome.find_element_by_css_selector(".text-primary > a:nth-child(4)").text
             NumePb = NumePb[0:]
             Sol = SolPbInfo + str(index) + "/a"
             FindProfiles(Chrome,Sol)
             for i in Profiles:
                 if not "nu exist" in Chrome.page_source:
                     verific = unu + str(i) + "/problema/" + str(index) + "/" + NumePb
                     Chrome.get(verific)
                     while "SQL nu este disponibil." in Chrome.page_source:
                         Chrome.get(verific)
                         time.sleep(2)
                     Solutii = Chrome.page_source
                     if("BDFF7C" in Solutii):
                         Conv = Contact + str(i)
                         Chrome.get(Conv)
                         while "SQL nu este disponibil." in Chrome.page_source:
                             Chrome.get(Conv)
                             time.sleep(2)
                         if not "nu vrea s" in Chrome.page_source and not i in OneMessage:
                             OneMessage.append(i)
                             print (i)
                             Milogeala = Chrome.find_element_by_id("mesaj")
                             Milogeala.send_keys(FirstMessage + str(index) + SecondMessage)
                             time.sleep(2)
                             Chrome.find_element_by_css_selector("input.btn").click()
                             time.sleep(3)
             print index
             del Profiles[:]
