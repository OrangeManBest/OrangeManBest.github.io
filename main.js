/* Jasper Zhang · bilingual toggle (ZH ⇄ EN) */
(function () {
  "use strict";
  var btn = document.getElementById("lang-toggle");
  var items = Array.prototype.slice.call(document.querySelectorAll("[data-en]"));

  // remember the original (Chinese) content of every translatable element
  items.forEach(function (el) {
    el.dataset.zh = el.innerHTML;
  });

  var isEn = false;

  function apply() {
    document.documentElement.lang = isEn ? "en" : "zh-CN";
    items.forEach(function (el) {
      el.innerHTML = isEn ? el.dataset.en : el.dataset.zh;
    });
    btn.textContent = isEn ? "中文" : "EN";
    btn.title = isEn ? "切换到中文" : "Switch to English";
    document.title = isEn
      ? "Jasper Zhang · AI Chip Technology Planning Manager"
      : "Jasper Zhang · 张智杰";
  }

  btn.addEventListener("click", function () {
    isEn = !isEn;
    apply();
  });

  apply();
})();
