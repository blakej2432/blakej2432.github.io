---
title: "Sql"
permalink: /categories/sql/
layout: archive
author_profile: true
taxonomy: sql
---

Oracle, Mysql, MariaDB 는 머릿말로 구분되어 있습니다.

{% assign posts = site.categories.sql %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
