from django.db import models
from django.utils.translation import ugettext_lazy as _
from merzlyakov.core import TimeStampMixin


class Comment(models.Model, TimeStampMixin):
    """
    Model to contain blog comments
    """
#   Custom user model should be written to let guests to register and comment
#    user = models.ForeignKey(CustomUser)
    content = models.TextField(_('Content'), blank=False, null=False, help_text='Comment text.')
    is_blocked = models.BoolenField(_('Blocked'), help_text='Is comment banned?')
    block_reason = models.CharField(_('Reason for ban'), max_length=255, blank=True, help_text='Reason for comment ban.')


class BlogCategory(models.Model):
    """
    A category to group blog posts thematically
    """
    title = models.CharField(_('Category'), max_length=255, blank=False, null=False, help_text='Category name')


class BlogPost(models.Model, TimeStampMixin):
    """
    Model to contain blog posts
    """
    title = models.CharField(_('Title'), max_length=140, blank=False, null=False)
    content = models.TextField(_('Content'), blank=False, null=False)
    category = models.ForeignKey(BlogCategory)
#   Should either use taggit lib or write custom tagging
#    tags = models.ManyToManyField(Tags)
    comments = models.ForeignKey(Comment)

