from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kategoriya", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Maqola nomi")
    content = models.TextField(blank=True, null=True, verbose_name="Matni")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
        ordering = ('-pk',)



class UserProfile(models.Model):
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    status = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    sayt = models.URLField(null=True, blank=True)
    github = models.CharField(max_length=25, null=True, blank=True)
    telegram = models.CharField(max_length=25, null=True, blank=True)
    instagram = models.CharField(max_length=25, null=True, blank=True)
    facebook = models.CharField(max_length=25, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text