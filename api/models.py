import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# from user.models import User


class Tag(models.Model):
    """
    书籍分类标签
    """
    tag = models.CharField('标签名', max_length=10)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.tag


class Book(models.Model):
    """
    书籍表
    """
    id = models.CharField(verbose_name='编号', primary_key=True, max_length=8)
    title = models.CharField(verbose_name='书名', max_length=50)
    num = models.IntegerField(verbose_name='数量')
    borrowed_num = models.IntegerField(verbose_name='已借数量', default=0)
    author = models.CharField(verbose_name='作者', max_length=20)
    pub_date = models.DateField(verbose_name='出版日期')
    intro = models.TextField(verbose_name='简介', null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(verbose_name='价格', default=30)

    def can_borrowed(self):
        return self.num > self.borrowed_num

    class Meta:
        verbose_name = '书目'
        verbose_name_plural = verbose_name
        ordering = ['id']
        db_table = 'books'

    def __str__(self):
        return self.title


class User(models.Model):
    """
    用户表
    """
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    name = models.CharField(verbose_name='姓名', max_length=30)
    password = models.CharField(verbose_name='密码', max_length=64)
    borrowed_books = models.ManyToManyField(Book, verbose_name='借阅书籍', through='BorrowInfo')
    tel = models.CharField(verbose_name='电话号码', max_length=11)
    id_card = models.CharField(verbose_name='身份证号', max_length=18, unique=True)
    balance = models.FloatField(verbose_name='余额', default=50)
    sex = models.CharField(max_length=30, choices=gender, default='男')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.id) + " " + self.name


class BorrowInfo(models.Model):
    """
    借阅关系表
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='书籍')
    borrowed_time = models.DateTimeField(verbose_name='借阅时间', default=timezone.now)
    return_ddl = models.DateTimeField(verbose_name='最晚归还时间',
                                      default=timezone.now() + datetime.timedelta(days=30))

    def is_timeout(self):
        return datetime.datetime.now() > self.return_ddl

    class Meta:
        verbose_name = '借阅关系'
        verbose_name_plural = verbose_name
        ordering = ['-return_ddl']
        db_table = 'borrow_info'

    def __str__(self):
        return '{} borrowed {} at {}'.format(self.user, self.book, self.borrowed_time)


class Log(models.Model):
    """
    借阅日志
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='书籍')
    borrowed_time = models.DateTimeField(verbose_name='借阅时间')
    return_time = models.DateTimeField(verbose_name='归还时间', default=timezone.now)
    cost = models.FloatField(verbose_name='消费', default=0)
    balance = models.FloatField(verbose_name='账户余额')

    class Meta:
        verbose_name = '借阅日志'
        verbose_name_plural = verbose_name
        ordering = ['borrowed_time']
        db_table = 'log'

    def __str__(self):
        return '[{}] {} {} {}'.format(self.borrowed_time, self.user, self.book, self.cost)


class BalanceChange(models.Model):
    """
    账户余额变化情况
    """
    all_action = (
        ('recharge', "充值"),
        ('cost', "借书扣费"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    time = models.DateTimeField(verbose_name='时间', default=timezone.now)
    action = models.CharField(verbose_name='金额变化类型', choices=all_action, default='cost', max_length=10)
    change_num = models.FloatField(verbose_name='金额变化数量')
    balance = models.FloatField(verbose_name='余额')

    class Meta:
        verbose_name = '账户余额变化日志'
        verbose_name_plural = verbose_name
        ordering = ['-time']
        db_table = 'balance_change'

    def __str__(self):
        return '[{}] {} {} {}'.format(self.time, self.user, self.action, self.change_num)








