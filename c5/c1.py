# -- coding: utf-8 --
from lxml import etree

text = '''
<div>
    <url>
        <li class="item-0"><a href="lik1.html">first item</a></li>
        <li class="item-1"><a href="lik2.html">second item</a></li>
        <li class="item-inactive"><a href="lik3.html">third item</a></li>
        <li class="item-1"><a href="lik4.html">forth item</a></li>
        <li class="item-0"><a href="lik5.html">fifth item</a></li>
    </url>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print (result)

# 文件读取
from lxml import etree

html = etree.parse('hello.html')
print type(html)
result = html.xpath('//li/@class')
print result
print len(result)
print type(result)
print type(result[0])
# result = etree.tostring(html, pretty_print=True)
# print (result)
