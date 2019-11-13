# -- coding: utf-8 --
# 初识python

"""
优点：
简单和明确，做一件事只有一种方法。
学习曲线低，跟其他很多语言相比，Python更容易上手。
开放源代码，拥有强大的社区和生态圈。
解释型语言，天生具有平台可移植性。
对两种主流的编程范式（面向对象编程和函数式编程）都提供了支持。
可扩展性和可嵌入性，例如在Python中可以调用C/C++代码。
代码规范程度高，可读性强，适合有代码洁癖和强迫症的人群。

Python的缺点主要集中在以下几点。
执行效率稍低，因此计算密集型任务可以由C/C++编写。
代码无法加密，但是现在很多公司都不销售卖软件而是销售服务，这个问题会被弱化。
在开发时可以选择的框架太多（如Web框架就有100多个），有选择的地方就有错误。

应用领域：
Web应用开发、云基础设施、DevOps、网络数据采集（爬虫）、数据分析挖掘、机器学习等领域都有着广泛的应用，
因此也产生了Web后端开发、数据接口开发、自动化运维、自动化测试、科学计算和可视化、数据分析、量化交易、
机器人开发、自然语言处理、图像识别等一系列相关的职位
"""
# e2 学习使用turtle在屏幕上绘制图形
import turtle

turtle.pensize(4)
turtle.pencolor('red')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()