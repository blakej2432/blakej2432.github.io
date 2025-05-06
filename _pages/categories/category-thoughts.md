---
title: "Thoughts"
permalink: /categories/thoughts/
layout: archive
author_profile: true
taxonomy: thoughts
---

회고, 이런저런 생각들, 시험후기, 다짐 등을 정리하고 기록합니다.

{% assign posts = site.categories.thoughts %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
