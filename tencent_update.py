import time
import random
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 配置
HEADLESS = False
LOGIN_TIMEOUT = 180  # 登录超时时间（秒）
PAGE_URL = "https://join.qq.com/progress.html"
USER_DATA_DIR = r"C:\Users\shen3\AppData\Local\Google\Chrome\JoinQQProfile"  # 独立目录复用登录态

def create_driver(headless: bool):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
        opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--ignore-certificate-errors")
    opts.add_argument("--ignore-ssl-errors")
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    opts.add_argument(f"--user-data-dir={USER_DATA_DIR}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    driver.implicitly_wait(6)
    return driver

def ensure_login_once(driver, timeout=LOGIN_TIMEOUT):
    driver.get(PAGE_URL)
    print("如首次运行，请在浏览器中完成登录（扫码/输入账号密码）...")
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//button[span[text()='更新简历']]"))
        )
        print("登录成功，登录态将被复用。")
        return True
    except Exception:
        print("等待登录超时或未检测到按钮。当前 URL:", driver.current_url)
        return False

def click_update_submit_confirm(driver):
    try:
        # 1. 打开进度页
        driver.get(PAGE_URL)

        # 2. 点击“更新简历”
        update_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[span[text()='更新简历']]"))
        )
        update_btn.click()
        print("已点击：更新简历")

        # 3. 勾选“无实习经历”复选框
        try:
            no_exp_label = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "label.el-checkbox.no_experience"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", no_exp_label)
            no_exp_label.click()
            print("已点击：无实习经历复选框")
        except Exception as e:
            print("未找到或无法点击“无实习经历”复选框：", e)

        # 4. 点击“提交简历”
        submit_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".send_bottom .button_box .el-button.el-button--primary"))
        )
        submit_btn.click()
        print("已点击：提交简历")

        # 5. 弹窗确认“保存简历”
        confirm_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".m-modal__footer .m-modal-button.m-modal--primary"))
        )
        confirm_btn.click()
        print("已点击：确认（保存简历）")

        # 6. 返回“应聘进度”页
        try:
            progress_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/progress.html')]"))
            )
            progress_link.click()
            print("已点击：应聘进度链接，返回进度页")
        except Exception:
            driver.get(PAGE_URL)
            print("已跳转：应聘进度页")

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 本轮完成。\n")

    except Exception as e:
        print("本轮流程失败：", e)

def main():
    driver = create_driver(HEADLESS)
    try:
        if not ensure_login_once(driver):
            return
        while True:
            click_update_submit_confirm(driver)
            interval_seconds = random.randint(300, 720)
            minutes = interval_seconds / 60
            print(f"下一轮将在 {interval_seconds} 秒后运行（约 {minutes:.2f} 分钟）。")
            time.sleep(interval_seconds)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
