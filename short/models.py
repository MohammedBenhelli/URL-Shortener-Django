from django.db import models
from hashlib import md5


class URL(models.Model):
    url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def click(self):
        self.count += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.url.encode('utf-8')).hexdigest()[:10]
        return super().save(*args, **kwargs)