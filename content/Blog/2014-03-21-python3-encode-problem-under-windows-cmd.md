---
date: 2014-03-21 02:01 PM
title: Python3在Windows下f.write()方法编码问题
categories: ['python', 'tech', 'crawler']
tags: ['python3', 'windows', 'code error']
layout: post
location: BITlab
---
之前由于windows下的编码问题，转用unbutu系统。
今天由于必须使用windows server运行程序，又开始尝试解决编码问题。

报错提示：

	:::console
	UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 967: 
	illegal multibyte sequence
出错代码：

	#!python
	request = urllib.request.Request(urlstr)
	fp = urllib.request.urlopen(request)
	content = fp.read()
	c = content.decode('utf-8')
	f = open('test', 'w')
	f.write(c)

报错代码为第6行, 代码仅为示意

<!--break-->

###探索

**第一步：**

```python
c = content.decode('utf-8')
```
修改为
```python
c = content.decode('utf-8').encode('gbk')
```
仍然是相同的错误

失败

**第二步：**
添加'ignore'参数
```python
c = content.decode('utf-8')
```
修改为

```python
c = content.decode('utf-8').encode('gbk', 'ignore')
```
报错改变，提示：
```console
TypeError: must be str, not bytes
```
有进步，继续

**第三步：**

由于我的目的是写入文件

尝试修改代码

```python
f = open('test', 'w')
```
为
```python
f = open('test', 'wb')
```
ok，成功

**第四步：**

虽然成功了，但是仍然心存不解。想起w跟我说过他一般都直接读写bytes，于是新的尝试。
百度一下，才发现，原来str.encode()返回的是bytes，而bytes.decode()方法返回的是string
```python
str.encode(encoding="utf-8", errors="strict")
```
<pre>
Return an encoded version of the string as a bytes object. 
Default encoding is 'utf-8'.
</pre>
```python
bytes.decode(encoding="utf-8", errors="strict")
bytearray.decode(encoding="utf-8", errors="strict")
```
<pre>Return a string decoded from the given bytes. 
Default encoding is 'utf-8'. </pre>

###Finally 策略

不直接读写str，将所有读写内容都更改为bytes。

代码修改为：

	#!python
	request = urllib.request.Request(urlstr)
	fp = urllib.request.urlopen(request)
	content = fp.read() #content是bytes
	return_content = string_process_func(content.decode('utf-8'))	
	f = open('test', 'wb')
	f.write(return_content.encode('utf-8'))
	f.close()

又涨姿势鸟~

参考：

 1. [python3 document str.encode](http://docs.python.org/3.2/library/stdtypes.html#str.encode)
 2. [python3 document bytes.decode](http://docs.python.org/3.2/library/stdtypes.html#bytes.decode)
