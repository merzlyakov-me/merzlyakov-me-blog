from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampMixin(models.Model):
    """
    Class to contain creation date, modification date
    and other time-based statistics
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(_('Created'), auto_now_add=True, editable=False,
                                        help_text=_('Time entity was first saved.'))
    updated_at = models.DateTimeField(_('Updated'), auto_now=True, editable=True,
                                        help_text=_('Time entity was updated last time.'))
    published_at = models.DateTimeField(_('Published'), null=True, editable=True,
                                        help_text=_('Time entity was published.'))


class MetaFieldsMixin(models.Model):
    """
    Class to contain Meta information on for Entities
    """
    description = models.TextField(_('Description'), blank=True)
    auto_gen_description = models.BooleanField(_('Generate description automatically'), default=True,
                                                help_text=_('Check to generate entity description automatically'+ \
                                                            ' when entity created.'))
    comments_enabled = models.BooleanField(_('Comments enabled'), default=True,
                                        help_text=_('Check to activate comments for entity.'))

