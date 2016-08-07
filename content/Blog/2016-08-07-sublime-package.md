title: Sublime Plugins and Themes
date: 2016-08-07 12:20
summary: Sublime常用的plugin和theme

今天把Mac上的sublime重新打扮了一番. 仅以此贴留作记录

**Plugins**

1. Package Control
1. Advanced CSV // Sublime 看CSV的利器 主要是拿来做高亮CSV的
1. Auto Hide Sidebar
1. AutoFileName
1. BracketHighlighter
1. DocBlockr_Python // Python Doc 辅助
1. Markdown Preview
1. MarkdownEditing
1. SideBarEnhancements
2. SublimeLinter
1. SublimeLinter-pylint
1. SublimeLinter-pyyaml
4. SublimeREPL

**Theme**

- [Material Theme](https://github.com/equinusocio/material-theme)

**Resources**

- [Package Control Installation](https://packagecontrol.io/installation)
- [Color Sublime](http://colorsublime.com/) // sublime主题网站
- [推荐！Sublime Text 最佳插件列表](http://blog.jobbole.com/79326/) // 伯乐在线的一篇文章,有点老,不过相对实用
- [Sublime Text 有哪些使用技巧？](http://www.zhihu.com/question/24896283) // 知乎一个问题,学习
- [Color Schemes](http://daylerees.github.io/) // scheme 大全...

**Package Control Installation**
贴过来备用.
``ctrl+ ` ``打开console,执行如下代码安装Package Control
```python
import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```