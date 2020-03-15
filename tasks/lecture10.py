import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')
        self.drv.get('https://www.google.com')

    def test_search(self):
        assert 'Google' in self.drv.title
        elm = self.drv.find_element_by_name('q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        time.sleep(5)
        text = self.drv.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a')
        print (text[0].get_attribute('href'))

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
