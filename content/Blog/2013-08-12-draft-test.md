---
layout: default
title: draft test
published: false
categories: ['test', 'it']
tags: ['test', 'tagtest']
---
#Tags and Categories Test




{{ site.tags.TAG }}

{% for post in page.tags %}
{{ post }}<br/>
{% endfor %}

{{ site.categories.CATEGORY }}