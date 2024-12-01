from django.db import models

class Category(models.Model):
    name_category = models.CharField(max_length=500)

class Teg(models.Model):
    name_teg = models.CharField(max_length=1000)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    id_tegs = models.ManyToManyField(Teg, through='image_tegs')

class image_tegs(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.PROTECT)
    teg_id = models.ForeignKey(Teg, on_delete=models.PROTECT)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"