---
title: Axure使用小体会及实现下拉菜单效果
layout: post
published: true
date: 2013-10-14 18:23
categories: ['Axure','Tech Study','Requirements analysis']
tags: ['Axure','Prototype']
---
目录
- [0 每次都要啰嗦一下]( #t0 )
- [1 Axure使用体会]( #t1 )
- [2 利用动态面板(Dynamic Panel)实现下拉菜单(Droplist)效果]( #t2 )
- [3 效果展示]( #t3 )
- [4 后记]( #t4 )

###0 每次都要啰嗦一下{ #t0 }
为了给boss完成任务，最近一直在用Axure做原型（虽然一直被一些骚年吐槽叫画界面233），两个月前一点没接触过，现在也算是有点小心得了，遂记之。

<!--break-->

###1 Axure使用体会{ #t1 }
在接触Axure本人没用过其它的原型设计软件，由于有过一点前端开发的经验。软件刚上手的时候，第一感觉就是，简洁、方便、清晰。对我而言，一些设计让我用得还是很自然舒服的。比如，控件(Widgets)和事件(Events)的名称跟html里是一样的，在拖拉控件的时候可以自动对齐，母板(Master)使得页面在设计的时候让我觉得条理清晰等等。还有，生成规格说明书的功能简直就是救星，哈哈。

至于不好的地方多在于对于现有功能的不满足：比如一些动态交互的实现比较纠结、一些html里只需要给属性赋值的功能在Axure里反而很麻烦。

Axure在原型设计领域里也算是有些名气的软件了~不多说了，用过你就知道~

###2 利用动态面板(Dynamic Panel)实现下拉菜单(Droplist)效果{ #t2 }
Droplist是个很常用的控件，而Axure在他的Widgets里也已经定义了这个控件，那么为什么我还要做这个呢？原因很简单。在Axure里，Droplist这个控件不能自定义样式。。。

####制作开始
1.在页面中拖入一个Heading 2(标题2)和一个Table(表格)的Widgets。这里Heading 2就相当于Droplist的选择部分，而Table相当于下拉列表的部分。

![图1](/assets/2013-10-17_Axure1.png)

2.把Table处理一下变为一列三行

![图2](/assets/2013-10-17_Axure2.png)

3.选中Heading 2和Table，将其转换为Dynamic Panel(动态面板)，为动态面板起个名字叫DP_下拉菜单。然后进入动态面板的state1(状态1)。

![图3](/assets/2013-10-17_Axure3.png)

![图4](/assets/2013-10-17_Axure4.png)

![图5](/assets/2013-10-17_Axure5.png)

4.先将Table转换为动态面板，为其起名为DP_下拉选项，然后回到DP_下拉菜单的state1，将DP_下拉选项的Visible(可见性)设置为不可见。不可见效果如下图所示。

![图6_1](/assets/2013-10-17_Axure9.png)

![图6_2](/assets/2013-10-17_Axure6.png)

5.回到DP_下拉菜单的State1，选择Heading 2，在屏幕最右侧的交互面板中双击OnMouseEnter(鼠标移入时)。在打开的Case Editor(用例编辑器)中，选择Show->DP_下拉选项，如图所示。

![图7_1](/assets/2013-10-17_Axure7.png)

![图7_2](/assets/2013-10-17_Axure11.png)

6.回到页面(Home)中，选择DP_下来菜单，在交互面板中点击More Events，找到OnMouseOut，单击。在Case Editor中，选择Hide->DP_下拉选项，如图所示。

![图8](/assets/2013-10-17_Axure12.png)

![图9](/assets/2013-10-17_Axure13.png)

![图10](/assets/2013-10-17_Axure14.png)

7.好了，完成！

###3 效果展示{ #t3 }
效果如下图所示

<video loop="loop" autoplay="autoplay" src="/assets/2013-10-17_Axure1.mp4">对不起，您的浏览器不支持Video标签</video>


稍微加点style和交互效果，感觉就不一样了

<video loop="loop" autoplay="autoplay" src="/assets/2013-10-17_Axure2.mp4">对不起，您的浏览器不支持Video标签</video>

###4 后记{ #t4 }
我用Axure的时间还是少了点，但是Axure确实是一款能提高原型设计效率的软件，对于页面多而杂的BS系统而言Axure非常合适。

PS.最后效果展示的部分利用了[Free Screen Video Recorder](http://www.dvdvideosoft.com/cn/products/dvd/Free-Screen-Video-Recorder.htm)和[Free HTML5 Video Player and Converter](http://www.dvdvideosoft.com/cn/products/dvd/Free-HTML5-Video-Player-and-Converter.htm)两款软件把录制好的视频文件转换成了浏览器适用的mp4文件,**简单粗暴的方法233**。然后直接在md里写上html代码，即可实现在md里插入视频：

	<video loop="loop" autoplay="autoplay" src="/assets/2013-10-17_Axure1.mp4">



大功告成，over。
