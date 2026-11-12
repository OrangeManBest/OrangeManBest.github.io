# -*- coding: utf-8 -*-
# Build index.html from content.md.
# Usage:  python build.py
# Edit content.md, then run this script -- never edit index.html by hand.
import re

SRC = "content.md"
OUT = "index.html"
DQ = chr(34)

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace(DQ, "&quot;")

def links(t):
    out = []
    pos = 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", t):
        out.append(esc(t[pos:m.start()]))
        out.append("<a href=" + DQ + m.group(2) + DQ + ">" + esc(m.group(1)) + "</a>")
        pos = m.end()
    out.append(esc(t[pos:]))
    return "".join(out)

raw = open(SRC, encoding="utf-8-sig").read().replace("\r\n", "\n")
lines = raw.split("\n")

title = ""
tagline = {"zh": "", "en": ""}
sections = []
cur_sec = None
cur_item = None

for ln in lines:
    s = ln.strip()
    if not s:
        continue
    if s.startswith("### "):
        t = s[4:].strip()
        year, sep, rest = t.partition(" · ")
        if " / " in rest:
            z, _, e = rest.partition(" / ")
        else:
            z = rest
            e = rest
        cur_item = {"year": year, "zh_t": z.strip(), "en_t": e.strip(), "zh": "", "en": ""}
        if cur_sec is not None:
            cur_sec["items"].append(cur_item)
    elif s.startswith("## "):
        t = s[3:].strip()
        if " / " in t:
            z, _, e = t.partition(" / ")
        else:
            z = t
            e = t
        cur_sec = {"zh_t": z.strip(), "en_t": e.strip(), "items": [], "zh": "", "en": ""}
        sections.append(cur_sec)
        cur_item = None
    elif s.startswith("# "):
        title = s[2:].strip()
    elif s.startswith("> "):
        body = s[2:].strip()
        if body.startswith("zh:"):
            tagline["zh"] = (tagline["zh"] + " " + body[3:].strip()).strip()
        elif body.startswith("en:"):
            tagline["en"] = (tagline["en"] + " " + body[3:].strip()).strip()
    elif s.startswith("zh:") or s.startswith("en:"):
        k = s[:2]
        txt = s[3:].strip()
        tgt = cur_item if cur_item is not None else cur_sec
        if tgt is not None:
            tgt[k] = (tgt[k] + " " + txt).strip()

name_en = title
name_zh = ""
if " · " in title:
    a, _, b = title.partition(" · ")
    name_en = a.strip()
    name_zh = b.strip()

p = []
add = p.append
add("<!DOCTYPE html>")
add("<html lang=" + DQ + "zh-CN" + DQ + ">")
add("<head>")
add("<meta charset=" + DQ + "utf-8" + DQ + ">")
add("<meta name=" + DQ + "viewport" + DQ + " content=" + DQ + "width=device-width, initial-scale=1" + DQ + ">")
add("<title>" + esc(title) + "</title>")
add("<meta name=" + DQ + "description" + DQ + " content=" + DQ + "Jasper Zhang (张智杰) - AI chip technology planning manager. Former autonomous driving system and perception tech lead." + DQ + ">")
add("<link rel=" + DQ + "icon" + DQ + " type=" + DQ + "image/svg+xml" + DQ + " href=" + DQ + "assets/favicon.svg" + DQ + ">")
add("<link rel=" + DQ + "stylesheet" + DQ + " href=" + DQ + "style.css" + DQ + ">")
add("</head>")
add("<body>")
add("<nav class=" + DQ + "top" + DQ + ">")
add("  <span class=" + DQ + "brand" + DQ + ">" + esc(name_en) + "</span>")
add("  <button id=" + DQ + "lang-toggle" + DQ + " class=" + DQ + "lang-btn" + DQ + " type=" + DQ + "button" + DQ + ">EN</button>")
add("</nav>")
add("<main>")
add("  <img class=" + DQ + "avatar" + DQ + " src=" + DQ + "assets/avatar.jpg" + DQ + " alt=" + DQ + esc(name_en) + DQ + ">")
add("  <h1>" + esc(name_en) + "</h1>")
if name_zh:
    add("  <p class=" + DQ + "subname" + DQ + ">" + esc(name_zh) + "</p>")
if tagline["zh"]:
    add("  <p class=" + DQ + "tagline" + DQ + " data-en=" + DQ + esc(tagline["en"]) + DQ + ">" + links(tagline["zh"]) + "</p>")

footer_zh = ""
footer_en = ""
for sec in sections:
    z = sec["zh_t"]
    e = sec["en_t"]
    if z == "简介":
        add("  <p class=" + DQ + "lead" + DQ + " data-en=" + DQ + esc(sec["en"]) + DQ + ">" + links(sec["zh"]) + "</p>")
        continue
    if z == "联系":
        add("  <h2 data-en=" + DQ + esc(e) + DQ + ">" + esc(z) + "</h2>")
        add("  <p><span class=" + DQ + "i18n-zh" + DQ + ">" + links(sec["zh"]) + "</span><span class=" + DQ + "i18n-en" + DQ + ">" + links(sec["en"]) + "</span></p>")
        continue
    if z == "页脚":
        footer_zh = sec["zh"]
        footer_en = sec["en"]
        continue
    add("  <h2 data-en=" + DQ + esc(e) + DQ + ">" + esc(z) + "</h2>")
    if sec["items"]:
        for it in sec["items"]:
            add("  <p class=" + DQ + "tl" + DQ + "><b>" + esc(it["year"]) + "</b> · <em data-en=" + DQ + esc(it["en_t"]) + DQ + ">" + esc(it["zh_t"]) + "</em><br><span data-en=" + DQ + esc(it["en"]) + DQ + ">" + links(it["zh"]) + "</span></p>")
    else:
        add("  <p data-en=" + DQ + esc(sec["en"]) + DQ + ">" + links(sec["zh"]) + "</p>")

add("</main>")
add("<footer>")
add("  <p>" + chr(0xA9) + " 2026 " + esc(name_en) + " · <span data-en=" + DQ + esc(footer_en) + DQ + ">" + links(footer_zh) + "</span></p>")
add("</footer>")
add("<script src=" + DQ + "main.js" + DQ + "></script>")
add("</body>")
add("</html>")

out = "\n".join(p) + "\n"
open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print("built " + OUT + ": " + str(len(out)) + " chars, " + str(len(sections)) + " sections")

