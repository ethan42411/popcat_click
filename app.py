from selenium import webdriver
import time
import sys
import os
import signal

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DRIVER = os.path.join(ROOT_DIR, "msedgedriver.exe")

browser = webdriver.Edge(executable_path=DRIVER)
# browser = webdriver.Firefox(executable_path="geckodriver.exe")

browser.get("https://popcat.click")
div = browser.find_element_by_id("app")

def stop_all(*args):
    browser.switch_to.window(browser.window_handles[1])
    browser.close()
    sys.exit(0)

if __name__ == "__main__":

    signal.signal(signal.SIGTERM, stop_all)
    signal.signal(signal.SIGINT,  stop_all)  # Ctrl-C

    while True:
        div.click()
        time.sleep(0.01)