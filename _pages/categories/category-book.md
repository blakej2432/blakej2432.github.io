---
title: "Book"
permalink: /categories/book/
layout: archive
author_profile: true
taxonomy: book
---

개발서적을 읽고 정리한 기록입니다.

{% assign posts = site.categories.book %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
