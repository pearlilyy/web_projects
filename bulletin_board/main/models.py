from django.db import models

# Create your models here.
# Post page needs posttitle, contents


class Post(models.Model):
    posttitle = models.CharField(max_length=50)
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # showing the each titles of the posts
    def __str__(self):
        return self.posttitle
