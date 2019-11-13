# -- coding: utf-8 --
import re

a = '<img src="https://s-media-cache-ak0.pinimg.com/originals/a8/c4/9e/a8c49ef606e0e1f3ee39a7b219b5c05e.jpg">'
# 使用re.search
search = re.search('<img src="(.*)">', a)
print(search.group(0))
print(search.group(1))

# 使用re.findall
findall = re.findall('<img src="(.*)">', a)
print(findall)

# 多个分组的使用（比如我们需要提取 img字段和图片地址字段）
re_search = re.search('<(.*) src="(.*)">', a)
print(re_search.group(0))
# 打印img
print(re_search.group(1))
# 打印地址
print(re_search.group(2))
# 打印img和地址，以元组的形式
print(re_search.group(1, 2))
# 或者使用groups
print(re_search.groups())
