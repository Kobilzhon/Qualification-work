from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import datetime


class Blog(models.Model):
    title = models.CharField(max_length=60, verbose_name="Тема поста")
    image = models.ImageField(upload_to='blog_photo', verbose_name="Фото поста",
                              validators=[FileExtensionValidator(['png', 'jpg'])])
    description = RichTextField(verbose_name="Описание")
    date = models.DateField(auto_now_add=True, auto_now=False)
    time = models.TimeField(auto_now_add=True, auto_now=False)
    # comment = FK

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('-date',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_blog = models.PositiveIntegerField()
    content = models.CharField(max_length=200, blank=False, default=None, null=False)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Пост комментирии"
        verbose_name_plural = "Пост комментирии"

    def __str__(self):
        return self.content


class CourseCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Категория курсов"
        verbose_name_plural = "Категория курсов"

    def __str__(self):
        return self.name


class Courses(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = RichTextField(verbose_name="Описание")
    show = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses_img', verbose_name="Фото курсов",
                              validators=[FileExtensionValidator(['png', 'jpg'])], null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class MasterClass(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateTimeField(default=datetime.datetime.now(), null=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False, null=True)
    time_created = models.TimeField(auto_now_add=True, auto_now=False, null=True)
    auditoria = models.PositiveIntegerField()
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='events_image', verbose_name="Фото",
                              validators=[FileExtensionValidator(['png', 'jpg'])])

    class Meta:
        verbose_name = "Мастер класс"
        verbose_name_plural = "Мастер классы"
        ordering = ('-date_created',)

    def __str__(self):
        return self.title


class Zayavka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    phone_num = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.message


class News(models.Model):
    image = models.ImageField(upload_to='news_photo', verbose_name="Фото для новости",
                              validators=[FileExtensionValidator(['png', 'jpg'])])
    title = models.CharField(max_length=100)
    description = RichTextField(verbose_name="Описание новости")
    date = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('-date',)

    def __str__(self):
        return self.title

    def news_comment_count(self):
        return self.newscomment_set.all().count()

    def news_comments(self):
        return self.newscomment_set.all()


class NewsComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, blank=False, default=None, null=False)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Новостное комментирии"
        verbose_name_plural = "Новостное комментирии"
        ordering = ('-time',)

    def __str__(self):
        return self.content
