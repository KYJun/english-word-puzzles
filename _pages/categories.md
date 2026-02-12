---
layout: single
title: "날짜별 보기"
permalink: /archive/
author_profile: true
toc: true
toc_label: "날짜"
toc_sticky: true
---

{% assign postsByYear = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in postsByYear %}

## {{ year.name }}년

{% assign postsByMonth = year.items | group_by_exp: "post", "post.date | date: '%m'" %}
{% for month in postsByMonth %}

### {{ year.name }}년 {{ month.name }}월

{% for post in month.items %}
- **{{ post.date | date: "%d일" }}** [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

{% endfor %}
{% endfor %}
