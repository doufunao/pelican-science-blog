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
3.Push output folder to server
