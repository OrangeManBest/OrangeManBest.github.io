# personal-site · Jasper Zhang 个人主页

Jasper Zhang（张智杰）的个人主页 —— 中英双语、纯 HTML/CSS/JS、零框架，仿科技领域引领者极简风格。

**在线访问：<https://orangemanbest.github.io>**

## 项目结构

```
personal-site/
├── index.html        # 主页面（中英双语，文本存在 data-en 属性中）
├── style.css         # 样式（自动跟随系统浅色/深色模式）
├── main.js           # 中 / EN 一键切换
├── assets/
│   ├── avatar.jpg    # 头像（提取自简历 PDF）
│   └── favicon.svg   # 页签图标
└── README.md         # 本文件
```

## 本地预览

在项目目录下运行：

```bash
python -m http.server 8000
```

然后浏览器访问 <http://localhost:8000>

## 部署到 GitHub Pages

```bash
# 1. 安装并登录 GitHub CLI（已安装时跳过）
gh auth login

# 2. 初始化并提交
git init
git add .
git commit -m "Initial personal homepage"

# 3. 创建个人主页仓库并推送（username.github.io 是 GitHub 约定的个人主页仓库）
gh repo create OrangeManBest.github.io --public --source . --remote origin --push

# 4. 启用 Pages（也可网页端 Settings → Pages → Deploy from a branch → main / root）
gh api repos/OrangeManBest/OrangeManBest.github.io/pages -X POST \
  -f "source[branch]=main" -f "source[path]=/"
```

等待一两分钟，访问 <https://orangemanbest.github.io> 即可看到主页。

## 自定义指南

| 想改什么 | 改哪里 |
|---|---|
| 联系方式（邮箱等） | `index.html` 的 `#contact` 区块 |
| 经历 / 教育 / 荣誉内容 | `index.html` 对应 `section` |
| 英文翻译 | 对应标签的 `data-en` 属性 |
| 头像 | 替换 `assets/avatar.jpg` |
| 配色 / 字体 | `style.css` 顶部的 CSS 变量 |