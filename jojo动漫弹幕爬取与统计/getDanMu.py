import requests
import re
from bs4 import BeautifulSoup


def getAnimateHtml(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def getCid(animatehtml):
    cids = re.findall(r'"cid":\d{8}', animatehtml)
    return cids


def getDanMu(cid):
    url = 'http://comment.bilibili.com/' + str(cid[6:]) + '.xml'
    req = requests.get(url)
    html = req.content
    html_doc = str(html, 'utf-8')
    soup = BeautifulSoup(html_doc, "lxml")
    results = soup.find_all('d')
    contents = [x.text for x in results]
    return contents


def writeFile(filename, s):
    f = open(filename, "a", encoding='gb18030')
    f.writelines(s)
    f.close()


def main():
    url = 'https://www.bilibili.com/bangumi/media/md135652/?spm_id_from=666.10.b_62616e67756d695f64657461696c.2'
    filename = 'E:/DanMu.txt'
    animatehtml = getAnimateHtml(url)
    cids = getCid(animatehtml)
    count = 0

    for cid in cids:
        count = count + 1
        contents = getDanMu(cid)
        writeFile(filename, contents)
        counts = count * 100 / len(cids)
        print('\r弹幕收集进度:{:3}%'.format(counts))


main()