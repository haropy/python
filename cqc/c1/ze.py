# -- coding: utf-8 --
# 1)re.match


# 2)re.search
import re

pattern = re.compile(r'world')
match = re.search(pattern, 'hello world!')
if match:
    print match.group()

    # 3)re.split()
import re

pattern = re.compile(r'\d+')
print re.split(pattern, 'one1two2three3four4')
