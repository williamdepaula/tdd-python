from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:4000')

assert 'Django' in browser.title