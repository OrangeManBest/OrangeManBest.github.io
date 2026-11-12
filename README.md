# personal-site · Jasper Zhang 个人主页

Jasper Zhang（张智杰）的个人主页。纯 HTML / CSS / JS，零框架，手写风格。

**在线访问：https://orangemanbest.github.io**

## ⚠️ 重要：内容改这里

**不要直接改 `index.html`** —— 它是自动生成的。

改内容请编辑 **`content.md`**，然后运行：

```bash
python build.py
```

`index.html` 就会重新生成。

## content.md 格式说明

```markdown
# Jasper Zhang · 张智杰          <- 页面大标题（英文 · 中文）

> zh: 我把感知算法变成量产的芯片。
> en: I turn perception algorithms into shipping silicon.

## 简介 / Bio                  <- 区块标题（中文 / English 顺序不能反）
zh: 中文内容（支持 [链接](https://...)）
en: English content

## 经历 / Timeline
### 2026 · AI 芯片技术规划 / AI Chip Planning   <- 年份 · 中文名 / English
zh: 中文描述
en: English description
```

## 文件说明

| 文件 | 说明 |
|---|---|
| `content.md` | **内容源，改这个** |
| `build.py` | 构建脚本（content.md -> index.html） |
| `index.html` | 自动生成，勿手改 |
| `style.css` | 样式 |
| `main.js` | 中 / EN 切换 |
| `assets/avatar.jpg` | 头像（来源 jasper-2.JPG） |
| `assets/favicon.svg` | 页签图标 |

## 本地预览

```bash
python -m http.server 8000
```

打开 http://localhost:8000

## 部署

```bash
git add -A
git commit -m "Update content"
git push origin main
```

推送到 GitHub 后约 1 分钟自动生效。

