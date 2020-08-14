# 图书馆借阅书籍管理
## 功能
一个图书馆借阅书籍的 django 项目。实现用户登录、注册、查看借阅图书信息、借阅书籍、归还书籍、余额充值、扣费等功能。
## 实现模块
分为用户和业务处理两个模块。

用户模块负责用户的注册和登录信息，需要先登录再进入服务。

业务处理模块分为页面处理部分和数据处理部分。页面处理模块(handle)用来返回模板，数据处理部分(api)实现返回数据和对用户输入的数据处理，对用户的借书行为和余额变动情况记录。


基于 python 3.5.2 和 Django 2.2.13 实现。