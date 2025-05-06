---
title: "Jpa"
permalink: /categories/jpa/
layout: archive
author_profile: true
taxonomy: jpa
---

Jpa 학습 내용을 기록합니다.

{% assign posts = site.categories.jpa %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
