from django.contrib import admin

from .models import Book, BorrowInfo, Tag, Log, BalanceChange, User
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'pub_date', 'num', 'borrowed_num', 'can_borrowed']


class BorrowInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'borrowed_time', 'return_ddl', 'is_timeout']


class LogAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'return_time', 'cost']


class BalanceChangeAdmin(admin.ModelAdmin):
    list_display = ['user', 'time', 'action', 'change_num', 'balance']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'balance']


admin.site.register(Tag)
admin.site.register(Book, BookAdmin)
admin.site.register(BorrowInfo, BorrowInfoAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(BalanceChange, BalanceChangeAdmin)
admin.site.register(User, UserAdmin)
