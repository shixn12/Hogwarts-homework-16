import pytest
import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWork3:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_getcookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        print(driver.get_cookies())
        cookie = driver.get_cookies()
        with open("test_cookie.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)

    def test_add_member(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        driver.implicitly_wait(5)
        yaml_data = yaml.safe_load(open("test_cookie.yaml", encoding="UTF-8"))
        for cookie in yaml_data:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.implicitly_wait(5)
        driver.find_element(By.ID,"menu_contacts").click()
        time.sleep(5)
        driver.find_element_by_link_text('添加成员').click()
        driver.find_element_by_id("username").send_keys("wbffff")
        driver.find_element_by_id('memberAdd_acctid').send_keys("123456")
        driver.find_element_by_id('memberAdd_phone').send_keys("19210918800")
        driver.find_element_by_link_text('保存').click()
        time.sleep(5)
        assert driver.find_element_by_xpath('//span[text()="wbffff"]').is_displayed()
