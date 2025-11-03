# 📄 Tencent_update

这是一个基于 Selenium 的自动化脚本，用于定时更新腾讯招聘平台上的简历状态。

---

## 🚀 功能说明

- 启动Google浏览器
- 自动打开腾讯招聘进度页
需要手动登录
- 自动点击“更新简历”按钮
- 自动勾选“无实习经历”复选框
- 自动点击“提交简历”并确认保存 
- 每轮操作后自动跳转回进度页
- 每轮间隔时间为 5–12 分钟，随机生成 （不要设定更新频率太快会被踹 别问我怎么知道的）
- 支持无头模式运行（可配置）

---

## ⚙️ 使用方法

### 1. 安装依赖环境

如果你想保护本地包，建议使用虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
如果你电脑没有安装过任何环境，请先配置python语言环境。

如若没有安装ChromeDriver，则需要匹配和谷歌浏览器同一版本的ChromeDriver。在代码中自动下载匹配 ChromeDriver
```bash
pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

### 2. 运行脚本

```bash
python tencent_update.py
```

脚本将自动循环执行简历更新流程，每轮间隔 5–12 分钟。

---

## 📦 requirements.txt

```txt
selenium>=4.12.0
webdriver-manager>=4.0.0
```

---

## 📁 项目结构

```
tencent_update/
├── tencent_update.py       # 主脚本
├── requirements.txt        # 依赖列表
└── README.md               # 项目说明

```


---

## ⚙️ 配置参数说明

以下是脚本参数列表

### 📦 全局配置参数

| 参数名            | 类型     | 默认值 | 说明 |
|------------------|----------|--------|------|
| `HEADLESS`       | `bool`   | `False` | 是否启用无头模式（隐藏浏览器界面）。设为 `True` 可后台运行，不显示浏览器窗口。 |
| `LOGIN_TIMEOUT`  | `int`    | `180`   | 登录等待超时时间（秒）。首次运行时用于等待用户扫码或输入账号密码。 |
| `PAGE_URL`       | `str`    | `"https://join.qq.com/progress.html"` | 腾讯招聘进度页的入口地址。 |
| `USER_DATA_DIR`  | `str`    | `r"C:\Users\shen3\AppData\Local\Google\Chrome\JoinQQProfile"` | Chrome 用户数据目录，用于复用登录态。建议为自动化创建独立配置目录。 |

---

### 🧠 函数参数与行为说明

#### `create_driver(headless: bool) → WebDriver`
- 创建并返回一个配置好的 Chrome 浏览器实例。
- 参数：
  - `headless`: 是否启用无头模式。
- 行为：
  - 使用 `webdriver-manager` 自动下载匹配的 ChromeDriver。
  - 设置浏览器选项，包括禁用日志、复用登录态等。

#### `ensure_login_once(driver, timeout=LOGIN_TIMEOUT) → bool`
- 检查是否已登录腾讯招聘页面。
- 参数：
  - `driver`: Selenium 浏览器实例。
  - `timeout`: 等待登录成功的最大时间（秒）。
- 行为：
  - 打开进度页并等待“更新简历”按钮出现。
  - 首次运行时需手动扫码或登录。
  - 返回 `True` 表示已登录，`False` 表示超时或失败。

#### `click_update_submit_confirm(driver)`
- 执行一次完整的简历更新流程。
- 参数：
  - `driver`: Selenium 浏览器实例。
- 步骤：
  1. 打开进度页
  2. 点击“更新简历”按钮
  3. 勾选“无实习经历”复选框（如果存在）
  4. 点击“提交简历”按钮
  5. 点击弹窗中的“确认”按钮
  6. 返回“应聘进度”页

#### `main()`
- 主入口函数，控制整体流程。
- 行为：
  - 创建浏览器实例
  - 检查登录状态
  - 进入无限循环，每轮执行一次 `click_update_submit_confirm`
  - 每轮间隔时间为 5–12 分钟，随机生成

---

### 🔁 每轮执行间隔

| 参数名             | 类型   | 范围     | 说明 |
|------------------|--------|----------|------|
| `interval_seconds` | `int` | `300–720` | 每轮执行后的等待时间（秒），随机生成，约 5–12 分钟 |
| `minutes`          | `float` | `5.0–12.0` | 将秒数转换为分钟，仅用于日志输出 |

---


---

## 🧠 注意事项

- 请确保 Chrome 浏览器已安装，并与 ChromeDriver 版本兼容
- 不建议与日常浏览器共享 user-data-dir，建议为自动化创建独立配置目录
- 若遇到元素点击失败，可截图上传至issue

---

## 📮 联系与反馈

如有问题或建议，欢迎在 GitHub Issues 中留言，或通过邮箱联系开发者。3200418862@qq.com

