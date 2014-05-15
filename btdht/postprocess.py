# -*- coding: utf-8 -*-
from urllib import urlopen
from lxml import etree


def fetch_name(info_hash):
    url = "https://torrentz.eu/%s" % info_hash
    response = urlopen(url)
    html = response.read()
    tree = etree.HTML(html)
    for tr in tree.xpath("//div[@class='files']/ul//ul/li"):
        return tr.text


if __name__ == "__main__":
    print fetch_name("0002d9461a5656233059dc48fb242b38ddb57dba")