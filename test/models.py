from django.db import models

class app(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def run_app(self, name):
        return "Corrio "+name