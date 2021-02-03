from django.db import models


class Accounts(models.Model):
    login = models.CharField('Логин', max_length=20, primary_key=True)
    pswd = models.TextField('Пароль')

    class Meta:
        db_table = "accounts"

    def __str__(self):
        return self.login
