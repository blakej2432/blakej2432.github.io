---
title: "Python"
permalink: /categories/python/
layout: archive
author_profile: true
taxonomy: python
---

Python 학습 내용을 기록합니다.

{% assign posts = site.categories.python %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
