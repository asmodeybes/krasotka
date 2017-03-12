from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("Category name"))
    def post_count(self):
        return Post.objects.filter(category_id=self.id).count()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")



class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name=_("Post title"))
    content = models.TextField(verbose_name=_("Post content"))
    published_date = models.DateTimeField(auto_created=True, verbose_name=_("Post date published"))
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    user = models.ForeignKey(User, verbose_name=_("Author"))
    img = models.ImageField(upload_to="posts", verbose_name=_("Фото"))
    #comment=models.ForeignKey(Comment, verbose_name=_("Comment"))
    def comments_count(self):
        return Comment.objects.filter(post_id=self.id).count()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class Comment (models.Model):
    content = models.TextField(verbose_name=_("Текст комментария"), max_length=100)
    published_date = models.DateTimeField(auto_created=True, verbose_name=_("Comment date published"))
    user = models.ForeignKey(User, verbose_name=_("Author"))
    post= models.ForeignKey(Post, verbose_name=_("Post"))


    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comment")
