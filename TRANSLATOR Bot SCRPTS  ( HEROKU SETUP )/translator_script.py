from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

def text(lang1="en", lang2="hi", string="i love you"):
    url = "https://translate.google.co.in/#view=home&op=translate&sl=%s&tl=%s&text=%s"%(lang1, lang2, string)
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path="/app/.chromedriver/bin/chromedriver", chrome_options = options)
    driver.get(url)
    
    rev_button = driver.find_element_by_class_name("swap-wrap").click()
    
    translation_box = driver.find_element_by_class_name("text-dummy")
    translation = translation_box.get_attribute("textContent")
    driver.close()
    return translation

