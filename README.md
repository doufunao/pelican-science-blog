# Requirement
python,pelican,markdown

    pip install pelican markdown
# How to generate
1.Build

    pelican content
2.Test on local

    cd {www-root}
    python -m http.server {port}
or

    python -m pelican.server {port}
3.Publish to server use rsync

	rsync -avc --delete output/ root@lilei.science:/var/www/pelican-blog/lilei_science_blog
# Reference
1. [Offical publishing guide](http://docs.getpelican.com/en/3.6.3/publish.html)
