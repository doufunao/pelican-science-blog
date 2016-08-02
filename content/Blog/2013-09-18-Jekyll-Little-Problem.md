---
layout: post
title: Jekyll本地配置小问题
tags: ['ruby','gem','jekyll','gem sources']
date: 2013-09-18 0:23
published: true
---
晚上重装系统到win8，然后果断把Jekyll又配置一遍。
有一步需要将默认的source替换成淘宝的镜像

输入
	
	gem sources --remove https://rubygems.org

结果提示我
	
	source https://rubygems.org not present in cache

搜了半天网上也有人出现这个问题，不过解决办法基本上都不靠谱。无意中看到一篇文档记录才发现，原来是少打了一个`/`。。。泪奔

输入
	
	gem sources --remove https://rubygems.org/

搞定

综上所述：粗心神马的不可取
