from selenium import webdriver
from time import sleep



browser = webdriver.Chrome()

browser.get('https://australiapopulation.com/naruto-subtitle/')



download_dir = r"C:\Users\makow\OneDrive\Documents\narutosubtitles"
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
browser.execute("send_command", params)


element = browser.find_element('xpath','/html/body/div[3]/div[2]/div[1]/div[1]/button/i')
element.click()


for i in range(1,151):
    if i < 51:
        element_path = '/html/body/div[2]/div[3]/main/article/div/div[2]/ul/li['+str(i)+']/h4/a/span/strong'
    else:
        element_path = '/html/body/div[2]/div[3]/main/article/div/div[2]/ul/li['+str(i)+']/h4/span/a/strong'
    
    element = browser.find_element('xpath',element_path)
    element.click()
    sleep(1)
                                   






                                   
                                   


