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

## 🧠 注意事项

- 请确保 Chrome 浏览器已安装，并与 ChromeDriver 版本兼容
- 不建议与日常浏览器共享 user-data-dir，建议为自动化创建独立配置目录
- 若遇到元素点击失败，可截图上传至issue

---

## 📮 联系与反馈

如有问题或建议，欢迎在 GitHub Issues 中留言，或通过邮箱联系开发者。3200418862@qq.com

