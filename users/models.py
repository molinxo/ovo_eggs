from django.db import models
from PIL import Image

class Profile(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)

    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    profpic = models.ImageField(default='default.jpg',upload_to='profpics/% Y/% m/% d/')

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profpic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
