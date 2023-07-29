from django.db import models


class Author(models.Model):   ####  1 new
    first_name=models.CharField(max_length=100, blank=False, null=False)    ####  2 new
    last_name = models.CharField(max_length=100, blank=False, null=False)
    age=models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.age}"


class Genre(models.Model):  ####  3 new
    name=models.CharField(max_length=100, blank=False, null=False)  ####  4 new

    def __str__(self):
        return self.name



class IpModel(models.Model):
    ip   = models.CharField(max_length=100)

    def __str__(self):
        return self.ip






class Book(models.Model):
    title=models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price=models.IntegerField(blank=False, null=False)
    views = models.ManyToManyField(IpModel, related_name="korishlars_soni", blank=True)
    author=models.ForeignKey(Author, blank=False, null=True, on_delete=models.SET_NULL)
    genre=models.ForeignKey(Genre, blank=False, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/" + str(self.id) + "/"

    def total_views(self):
        return self.views.count()

    class Meta:
        ordering = ['-id']

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='nomi')
    subject  = models.TextField()
    number = models.PositiveIntegerField()
    tg_name =  models.CharField(max_length=200, verbose_name='telegram nomi')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}  || {self.create_at}'

    class Meta:
        ordering = ['-id']




