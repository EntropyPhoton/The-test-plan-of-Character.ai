from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver=webdriver.Chrome()
url="https://beta.character.ai/"
driver.get(url)
driver.maximize_window()
#time.sleep(999)
#如果加载时间过短，浏览器未加载出控件，会使后面的语句报错
driver.find_element(By.XPATH,'//*[@id="header-row"]/div[2]/div[1]/button').click#点击Character.ai的登录按钮，如果找不到控件，可能嵌套在一个子页面当中
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div[5]/div/div[1]/div/div/div[2]/div/div[1]/button[1]').click#出现登录按钮后，点击“Log in with Google”
#如果上述显示正确，控件可用，说明该网站的主界面可以正确的显示，登录也可以正确进行。
driver.quit()
