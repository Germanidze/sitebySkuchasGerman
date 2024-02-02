from django.db import models
class Timetabl(models.Model):
    title = models.CharField("день",max_length=50)
    clas = models.CharField("класс", max_length=50)
    uroki = models.CharField("уроки",max_length=200)

    def __str__(self):
        return f'уроки на: {self.title}'

