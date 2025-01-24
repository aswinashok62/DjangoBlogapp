from django.db import models
   # Django-Blog-master/blog/models.py
from django.db import models

class Blog(models.Model):
    class Meta:
        app_label = 'admin'  # Specify the app label here
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
