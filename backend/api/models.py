# models.py
from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=120)
    # description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title