from django.db import models

class Post(models.Model):
    pname = models.CharField(max_length=100)
    pid = models.TextField()
    Image = models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.pname