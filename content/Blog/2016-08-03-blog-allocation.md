title: 真是不能愉快地码字了
date: 2016-08-03 00:46
summary: 博客搬迁小记

晚上心血来潮，把笔记本上之前的博文都搬运到了新站。然后又心血来潮，把某篇博文里的不兼容问题想办法解决了。真心没想到markdown的坑也这么多。在不同的解析器上，一些trick无法避免。

1. code highlight部分从原来的手工加line number改成自动加。Pelican的markdown解析器，或者说python的markdown解析器其实自带code highlight功能。google python markdown会有一些解释。
1. 参照[在本地安装Jekyll时遇到的几点问题]({filename}2013-08-23-Question-in-Install-Jekyll.markdown)把**首页显示摘要**和**段落首行空两格**这两个问题解决了。因为Jekyll和Pelican的实现方式还是略有不同，虽然原理是一样的，还是花了些时间，有空的时候把解决方案也写上来。

搬家一次体会更深，Pelican通过theme和plugin几乎能涵盖80%的需求。而对于Jekyll最大的卖点之一，Github直接托管原生代码，通过ghp-import也被弱化了。不过换个思路，估计现在成熟的framework基本上都有对应策略。

只需config，弱化码，很pythonic，很酷。

对于博客而言，还有很多可以完善的地方，比如字体，颜色，layout，行间距，文章的字段。这个主题实在快忍不了了。。。
文章虽然都搬过来了，但是md的语法好多都没align。。。还要想办法解决一下。。。

**TBD**