from django.db import models
import os
import logging


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email =models.CharField(max_length=200, default="")
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_people = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name



def news_image_path(instance, filename):
    # Generate a unique filename based on the post's title
    ext = filename.split('.')[-1]  # Get the file extension
    filename = f"{instance.title.replace(' ', '_')}_image.{ext}"
    return os.path.join('news_images', filename)

    logger = logging.getLogger(__name__)
    logger.info(f"Instance title: {instance.title}")
    logger.info(f"Generated filename: {filename}")



class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    body = models.TextField(default=())
    image = models.ImageField(upload_to=news_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return self.title