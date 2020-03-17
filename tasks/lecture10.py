# coding=utf-8
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
        time.sleep(2)
        # Поиск ссылок по xpath
        search1 = self.drv.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a')
        # Проверка что нашелся хотя бы один элемент
        assert len(search1) > 0
        # проверка что первая (1-й элемент search1 - search1[0] ) ведёт на selenide.org
        assert 'selenide.org' in search1[0].get_attribute('href')
        description1 = self.drv.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3')[0].get_attribute(
            'textContent')
        # Поиск кнопки "картинки" по xpath
        pic = self.drv.find_elements_by_xpath('//*[@id="hdtb-msb-vis"]/div[4]/a')
        # Проверка что она нашлась
        assert len(pic) > 0
        # Переход в картинки
        pic[0].click()
        time.sleep(2)
        # Поиск картинок по xpath
        picture = self.drv.find_elements_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]')
        # Проверка что нашлась хотя бы одна
        assert len(picture) > 0
        # проверка что первая картинка с сайта selenide.org
        assert 'selenide.org' in picture[0].get_attribute('href')
        # Поиск кнопки "все результаты" по xpath
        all_search = self.drv.find_elements_by_xpath(
            '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
        # Проверка что кнопка нашлась
        assert len(all_search) > 0
        # Возврат на поиск
        all_search[0].click()
        time.sleep(2)
        # Аналогичная проверка первой ссылки
        search2 = self.drv.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a')
        assert len(search2) > 0
        assert 'selenide.org' in search2[0].get_attribute('href')
        description2 = self.drv.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3')[0].get_attribute(
            'textContent')
        # Проверка что описания совпадают (описание - Selenide: лаконичные и стабильные UI тесты на Java)
        assert description2 == description1

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
