---
layout: page
title: "게임별 보기"
permalink: /games/
---

## 🎮 게임별 퍼즐 정답 모아보기

### 🧩 Bonza
테마별 영어 단어 조각을 맞추는 크로스워드 퍼즐

{% for post in site.posts %}{% if post.game == "Bonza" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}

---

### 🔀 Crossover
교차하는 단어를 찾아 완성하는 퍼즐

{% for post in site.posts %}{% if post.game == "Crossover" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}

---

### 🛤️ Waywords
연결된 단어 경로를 찾는 게임

{% for post in site.posts %}{% if post.game == "Waywords" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}

---

### ⌨️ Keysmash
뒤섞인 글자에서 단어를 찾아내는 게임

{% for post in site.posts %}{% if post.game == "Keysmash" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}
