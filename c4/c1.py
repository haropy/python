# -- coding: utf-8 --
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('index.html'), 'html.parser')
# print soup.prettify()
# 1)Tag
print soup.title
print soup.head
print soup.a
print soup.p

print type(soup.a)

# soup对象本身比较特殊，它的name即为[document],对于其他的内部标签，输出的值便为标签本身的名称。
print soup.name
print soup.head.name

print soup.p.attrs  # 打印出所有属性，得到的类型是一个字典。
print soup.p['class']  # 单独获取某个属性。还可以利用get
print soup.p.get('class')

# 修改属性和内容
soup.p['class'] = 'newClass'
print soup.p

# 删除属性
del soup.p['class']
print soup.p

# 2)NavigableString 可以遍历的字符串
print soup.p.string
print type(soup.p.string)
# 3)BeautifulSoup 特殊Tag，获取类型，名称以及属性
print type(soup.name)
print soup.name
print soup.attrs  # 空字典
# 4）Comment 特殊类型的 NavigableString 对象
print soup.a
print soup.a.string
print type(soup.a.string)

# 发现它是一个 Comment 类型，所以，我们在使用前最好做一下判断
import bs4

if type(soup.a.string) == bs4.element.Comment:
    print soup.a.string

# 遍历文档树
# 1）直接子节点
# .contents 属性可以将tag的子节点以列表的方式输出
print soup.head.contents
print type(soup.head.contents)
print soup.head.contents[0]

# .children 返回的不是一个list，不过我们可以通过遍历获取所有子节点
print soup.head.children
for child in soup.body.children:
    print child

# 2)所有子节点
# .descendants 可以对所有tag的子孙节点进行递归循环，和children类似，我们也要遍历获取其中的内容。
for child in soup.descendants:
    print child

# 3）节点内容
# 如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容
print soup.head.string
print soup.title.string
# 如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
print soup.html.string

# 4)多个内容
# .strings
# 获取多个内容，不过需要遍历获取
for string in soup.strings:
    print (repr(string))

# stripped_strings
# 去除输出的字符串中可能包含了很多空格或空行
for string in soup.stripped_strings:
    print (repr(string))

# 5）父节点 .parent
p = soup.p
print p.parent.name

content = soup.head.title.string
print content.parent.name

# 6)全部父节点 .parents
content = soup.head.title.string
for parent in content.parents:
    print parent.name

# 7)兄弟节点 next_sibling prev_sibling
print soup.p.next_sibling  # 实际该处为空白
print soup.p.prev_sibling  # 没有前一个兄弟节点，返回None
print soup.p.next_sibling.next_sibling

# 8)全部兄弟节点
for sibling in soup.a.next_siblings:
    print (repr(sibling))

# 9)前后节点
print soup.head.next_element

# 10)所有前后节点
# for element in last_a_tag.next_elements:
#     print (repr(element))

# 搜索文档树
# 1）find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)
# A.传字符串
soup.find_all('b')
print soup.find_all('a')
# B.传正则表达式
import re

for tag in soup.find_all(re.compile("^b")):
    print (tag.name)
# C.传列表
soup.find_all(["a", "b"])

# D.传True 可以匹配任何值
for tag in soup.find_all(True):
    print (tag.name)


# E.传方法
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


print soup.find_all(has_class_but_no_id)

# 2)keyword 参数
print soup.find_all(id='link2')

# 如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性
print soup.find_all(href=re.compile("elsie"))

# 使用多个指定名字的参数可以同时过滤tag的多个属性
print soup.find_all(href=re.compile("elsie"), id='link1')

# python关键字过滤
print soup.find_all("a", class_="sister")

# 有些tag属性在搜索不能使用，比如HTML5中的data-*属性
data_soup = BeautifulSoup('div data-foo = "value">foo!</div>', 'html.parser')
print data_soup.find_all(data_foo="value")
print data_soup.find_all(attrs={"data-foo": "value"})

# 3)text参数
# 通过text参数可以搜索文档中的字符串内容，与name参数的可选值一样，text参数接受字符串，正则表达式，列表，True
print soup.find_all(text="Elsie")
print soup.find_all(text=["Title", "Elsie", "Lacie"])
print soup.find_all(text=re.compile("Dormouse"))

# 4)limit参数
print soup.find_all("a", limit=2)

# 5)recursive参数
# 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
print soup.html.find_all("title")
print soup.html.find_all("title", recursive=False)

# CSS选择器
# 1）通过标签名查找
print soup.select('title')
print soup.select('a')

# 2)通过类名查找
print soup.select('.sister')

# 3)通过id名查找
print soup.select('#link1')

# 4)组合查找
print soup.select('p #link1')
# 直接子标签查找
print soup.select("head > title")

# 5)属性查找
print soup.select('a[class="sister"]')
print soup.select('a[href="http://example.com/elsie]')
print soup.select('p a[href="http://example.com/elsie]')

soup = BeautifulSoup(html, 'lxml')
print type(soup.select('title'))
print soup.select('title')[0].get_text()

for title in soup.select('title'):
    print title.get_text()
