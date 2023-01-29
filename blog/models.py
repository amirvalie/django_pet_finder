from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from pet.models import CategoryABC
# Create your managers here.
User=get_user_model()

class ArticleManager(models.Manager):
	def published(self):
		return self.filter(status='p')

class CategoryManager(models.Manager):
	def active(self):
		return self.filter(status=True) 


class BlogCategory(CategoryABC):
    parent=models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name='children',
    )
    thumbnail=models.ImageField(
        upload_to='category',
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
	STATUS_CHOICES = (
		('d', 'Draft'),	
		('p', "Public"),
	)

	author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='articles',
    )
	title = models.CharField(
        max_length=200,
    )
	slug = models.SlugField(
        max_length=100,
        unique=True,
    )
	category = models.ForeignKey(
        BlogCategory,
        null=True,
        on_delete=models.SET_NULL,
        related_name="articles"
    )
	description = models.TextField()
	thumbnails = models.ImageField(
        upload_to="images/article",
    )
	thumbnail = models.ImageField(
        upload_to="images/article",
    )
	publish = models.DateTimeField(
        default=timezone.now,
    )
	created = models.DateTimeField(
        auto_now_add=True,
    )
	updated = models.DateTimeField(
        auto_now=True,
    )
	status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='d',
    )

	objects = ArticleManager()

	def __str__(self):
		return self.title
