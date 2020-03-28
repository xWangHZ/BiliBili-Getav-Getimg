import re
import requests

url = "https://www.bilibili.com/video/"

def get_html(bv):
    htmlurl = url+bv
    
    html = requests.get(htmlurl)
    html = html.text

    img = re.findall(r'<meta data-vue-meta="true" itemprop="image" content="(.*?)">', html, re.S)
    av = re.findall(r'<meta data-vue-meta="true" itemprop="url" content="https://www.bilibili.com/video/(.*?)/">', html, re.S)

    return av[0], img[0]