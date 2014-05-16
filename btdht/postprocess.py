# -*- coding: utf-8 -*-
from urllib import urlopen
from lxml import etree


def fetch_name(info):
    url = "https://torrentz.eu/%s" % info
    response = urlopen(url)
    html = response.read()
    tree = etree.HTML(html)
    try:
        size = tree.xpath("//div[@class='files']/div")[0].text
        fold_name = tree.xpath("//div[@class='files']/ul/li[@class='t']")[0].text
        files = "|".join(tr.text.strip() for tr in tree.xpath("//div[@class='files']/ul//ul//li"))
    except (IndexError, AttributeError):
        return None
    else:
        return fold_name, size, files


if __name__ == "__main__":
    print fetch_name("0002d9461a5656233059dc48fb242b38ddb57dba")