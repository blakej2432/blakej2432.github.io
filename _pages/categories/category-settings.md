---
title: "Settings"
permalink: /categories/settings/
layout: archive
author_profile: true
taxonomy: settings
---

개발환경 및 IDE 등 설정에 대한 기록입니다.

{% assign posts = site.categories.settings %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
