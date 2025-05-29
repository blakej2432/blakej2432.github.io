---
title: "Django"
permalink: /categories/django/
layout: archive
author_profile: true
taxonomy: django
---

Django 학습 내용을 기록합니다.

{% assign posts = site.categories.django %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
