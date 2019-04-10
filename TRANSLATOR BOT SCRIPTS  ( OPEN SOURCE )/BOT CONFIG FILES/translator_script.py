from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


def text(lang1, lang2, string):
    #string = input("Enter text to translate :")
    url = r"https://translate.google.co.in/#view=home&op=translate&sl=%s&tl=%s&text=%s"%(lang1, lang2, string)
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(chrome_options  = options)
    driver.get(url)

    #SWAPPING CONTENTS SO TO RETRIEVE DATA
    rev_button = driver.find_element_by_class_name("swap-wrap").click()
        
    #ACCESSING DATA BOX AND RETRIEVING DATA
    translation_box = driver.find_element_by_class_name("text-dummy")
    translation = translation_box.get_attribute("textContent")
    driver.close()
        
    return translation