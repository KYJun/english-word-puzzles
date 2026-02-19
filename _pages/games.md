---
layout: single
title: "게임별 보기"
permalink: /games/
author_profile: true
toc: true
toc_label: "게임 목록"
toc_sticky: true
---

## 🧩 Bonza
테마별 영어 단어 조각을 맞추는 크로스워드 퍼즐

{% for post in site.posts %}{% if post.game == "Bonza" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}

---

## 🔀 Crossover
교차하는 단어를 찾아 완성하는 퍼즐

{% for post in site.posts %}{% if post.game == "Crossover" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}

---

## 🛤️ Waywords
연결된 단어 경로를 찾는 게임

{% for post in site.posts %}{% if post.game == "Waywords" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}

---

## ⌨️ Keysmash
뒤섞인 글자에서 단어를 찾아내는 게임

{% for post in site.posts %}{% if post.game == "Keysmash" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}

---

## 🎯 Pinpoint
단서를 보고 공통 주제를 추리하는 두뇌 게임

{% for post in site.posts %}{% if post.game == "Pinpoint" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}{% endraw %}

---

## 🟩 Wordle
6번의 기회 안에 5글자 단어를 맞히는 인기 단어 퍼즐

{% for post in site.posts %}{% if post.game == "Wordle" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}{% endraw %}

---

## 🧠 Connections
16개의 단어를 4개의 공통 그룹으로 묶는 추리형 퍼즐

{% for post in site.posts %}{% if post.game == "Connections" %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y.%m.%d" }}
{% endif %}{% endfor %}{% endraw %}