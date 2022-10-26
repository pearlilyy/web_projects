from django.contrib import admin
from .models import Post

# Register your models here.
# admin has authority to see and delete to the posts
admin.site.register(Post)
