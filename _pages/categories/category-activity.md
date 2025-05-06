---
title: "개발 관련 활동"
permalink: /categories/activity/
layout: archive
author_profile: true
taxonomy: blog
---

세미나, 코딩테스트 등 개발 관련 활동에 대한 기록입니다.

{% assign posts = site.categories.activity %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
