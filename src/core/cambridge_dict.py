from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from core.entities import Word
import translators as ts
import eng_to_ipa as p 

options = ChromeOptions()
# options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get('https://dictionary.cambridge.org/dictionary/english/')

def get_element(xpath: str, default):
    try:
        return browser.find_element(by=By.XPATH, value=xpath).text
    except:
        return default

def search_word(word: str):
    try:
        search_box = browser.find_element(by=By.XPATH, value='//*[@id="searchword"]')
        search_box.clear()
        search_box.send_keys(word)
        try:
            search_btn = browser.find_element(by=By.XPATH, value='//*[@id="searchForm"]/div[1]/div[2]/span/button[3]')
        except:
            search_btn = browser.find_element(by=By.XPATH, value='//*[@id="searchForm"]/div[1]/div[1]/span/button[3]')
        search_btn.click()
        # get content
        vietnamese = ts.translate_text(word, from_language='en', to_language='vi')
        type = get_element('//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div[2]/span', 'unknown')
        # phonetic = get_element('//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/span[2]/span[3]', '')
        phonetic = p.convert(word)
        mean = get_element('//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div', '').split('\n')[0]
        example = get_element('//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[3]/div', '')
        return Word(english=word, type=type, vietnamese=vietnamese, pronunciation=phonetic, meaning=mean, examples=[example])
    except Exception as e:
        raise e