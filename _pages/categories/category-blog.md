---
title: "Blog"
permalink: /categories/blog/
layout: archive
author_profile: true
taxonomy: blog
---

Jekyll Minimal-mistakes 로 만든 블로그를 커스터마이징한 기록입니다.

{% assign posts = site.categories.blog %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
