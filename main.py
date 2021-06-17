from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://eldorado.ua/")
browser.implicitly_wait(3)

search_value = "телевизор"
browser.find_element_by_css_selector('[name="new-search"]').send_keys(search_value)
browser.find_element_by_css_selector('[name="new-search"]').send_keys(Keys.RETURN)
actual_result = browser.find_element_by_css_selector('.search-top h5 span').text.lower()
expected_result = search_value

assert actual_result == expected_result
