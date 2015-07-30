from django.db import models


class PostExcerpt(models.Model):
    """
    Excerpt to generate meta description
    """

    class Meta:
        abstract = True

    def verify_title_seo(self):
        title_length = len(self.title)
        title_words = len(self.title.split(' '))
        error_msgs = []
        if title_length > 65:
            self.title_seo = False
            error_msgs.append("Title is more than 65 chars long.")
        elif title_words > 8:
            pass # TODO: add SEO checks
            
       
