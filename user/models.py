from django.db import models

# from api.models import Book


# Create your models here.
# class User(models.Model):
#     """
#     用户表
#     """
#     gender = (
#         ('male', "男"),
#         ('female', "女"),
#     )
#     id = models.CharField(verbose_name='用户名', max_length=8, primary_key=True)
#     name = models.CharField(verbose_name='姓名', max_length=30)
#     password = models.CharField(verbose_name='密码', max_length=64)
#     borrowed_books = models.ManyToManyField(Book, verbose_name='借阅书籍', through='BorrowInfo')
#     tel = models.CharField(verbose_name='电话号码', max_length=11)
#     id_card = models.CharField(verbose_name='身份证号', max_length=18, unique=True)
#     balance = models.FloatField(verbose_name='余额', default=50)
#     sex = models.CharField(max_length=30, choices=gender, default='男')
#
#     class Meta:
#         db_table = 'user'
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name
#         ordering = ['id']
#
#     def __str__(self):
#         return str(self.id) + " " + self.name
