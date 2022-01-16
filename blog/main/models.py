from ctypes.wintypes import tagSIZE
import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from unidecode import unidecode
from datetime import datetime


def get_user_suffix(user_id):
        result = User.objects.get(pk=user_id)
        return "_".join([result.username, str(result.pk)])
    

def post_img_dir(instance, filename):
    ext = filename.split('.')[-1]
    if instance.created_at:
        date_suffix = instance.created_at.strftime("%Y")
    else: date_suffix = datetime.now().strftime("%Y")
    
    filename = "%s.%s" % (str(uuid.uuid4())[:13], ext)
    return '{0}/images/posts/{1}/{2}'.format(get_user_suffix(instance.user.id), date_suffix, filename)


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name = 'Название')
    slug = models.SlugField(
        max_length=100, 
        verbose_name='Url', 
        unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name = 'Название')
    slug = models.SlugField(
        max_length=50, 
        verbose_name='Url',
        unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('title',)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    STATUS_CHOICES = (
        ('черновик', 'Черновик'),
        ('опубликовано', 'Опубликовано'),
    )
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='posts',)
    profile = models.ForeignKey(
        'users.Profile', 
        on_delete=models.PROTECT)
    
    is_draft = models.BooleanField(default=True)
    # publish = models.DateTimeField(default=timezone.now)
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    views = models.PositiveIntegerField(
        default=0,
        verbose_name='Просмотры',)
    post_sourse = models.CharField(
        max_length=255,
        verbose_name = 'Источник',
        blank=True)
    
    category = models.ManyToManyField(
        Category,
        verbose_name='Категория',
        blank=True)
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True)
    image = models.ImageField(
        # upload_to='posts/images',
        upload_to=post_img_dir,
        blank=True,
        verbose_name='Изображение',
        validators=[FileExtensionValidator(['jpeg', 'jpg','png', 'webp'])],)
    title = models.CharField(
        max_length=255,
        verbose_name = 'Название')
    slug = models.SlugField(
        max_length=255,
        verbose_name='Url', 
        unique=True)
    desc = RichTextUploadingField(
        verbose_name='Описание',
        blank=True)
    content = RichTextUploadingField(
        verbose_name='Содержание',
        blank=True)
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',)
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата внесения изменений',)
    

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-created_at',)
        
    def __str__(self):
        # return self.title
        
        """Return title and username"""
        return '{} by @{}'.format(self.title, self.user.username)
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
        
class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.PROTECT, 
        related_name='comments')
    user = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        related_name='user_name')
    # profile = models.ForeignKey(
    #     'users.Profile', 
    #     on_delete=models.PROTECT)
    
    # title = models.CharField(max_length=80)
    # email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.comment
        # return 'Comment by {} on {}'.format(self.title, self.post)