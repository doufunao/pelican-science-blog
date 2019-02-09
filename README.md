# Requirement
1. python,pelican,markdown
```bash
pip install pelican markdown
```
2. retrive pelican-plugins from github into ./pelican-plugins
```bash
git clone --recursive https://github.com/getpelican/pelican-plugins
```
# How to generate
1.Build
```bash
pelican content
```
2.Test on local
```bash
cd {www-root}
python -m http.server {port}
```
or
```bash
python -m pelican.server {port}
```
3.Publish to server use rsync
```bash
rsync -avc --delete output/ root@lilei.science:/var/www/pelican-blog/lilei_science_blog
```

# Setup new server
#### 1.拷贝网站文件到新机器目录 /var/www/lilei_science_blog

#### 2.修改documentroot
```bash
sudo vi /etc/apache2/sites-enabled/000-default.conf
DocumentRoot /var/www/lilei_science_blog
```
#### 3.加载环境变量
```bash
#cat /etc/apache2/envvars
source /etc/apache2/envvars
/usr/sbin/apache2 -V
```
[参考](https://serverfault.com/questions/558283/apache2-config-variable-is-not-defined)

#### 4.重启apache2服务
```bash
sudo /etc/init.d/apache2 restart
```

# Reference
1. [Offical publishing guide](http://docs.getpelican.com/en/3.6.3/publish.html)
