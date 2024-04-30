from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_citation_from_google_scholar(query):
    # 初始化 WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 打开谷歌学术
        driver.get('https://scholar.google.com')
        time.sleep(3)  # 让页面加载

        # 找到搜索框，输入查询内容，然后提交表单
        search_box = driver.find_element(By.NAME, 'q')
        time.sleep(3)
        search_box.send_keys(query)
        time.sleep(3)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # 等待搜索结果
        if "CAPTCHA" in driver.page_source:
            print("请解决网页中的 CAPTCHA，然后回到终端按 Enter 继续...")
            input()  # 等待用户在命令行敲击 Enter
        # 点击第一篇文章的引用链接
        cite_link = driver.find_element(By.XPATH, '//a[text(),"引用"]')
        time.sleep(5)
        cite_link.click()
        time.sleep(5)  # 等待引用信息加载
        if "CAPTCHA" in driver.page_source:
            print("请解决网页中的 CAPTCHA，然后回到终端按 Enter 继续...")
            input()  # 等待用户在命令行敲击 Enter

        # 选择并复制引用格式，例如 MLA
        citation = driver.find_element(By.XPATH, '//div[@id="gs_citi"]/a[text()="MLA"]')
        time.sleep(5)
        citation.click()
        time.sleep(5)

        # 获取引用文本
        citation_text = driver.find_element(By.TAG_NAME, 'pre').text
        time.sleep(5)
        print(citation_text)
    finally:
        # driver.quit()  # 关闭浏览器
        print("程序结束")

if __name__ == "__main__":
    article_title = "明末社会矛盾"
    get_citation_from_google_scholar(article_title)