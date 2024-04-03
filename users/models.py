from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# # Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    phone = models.CharField(max_length=15)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # image optimization
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.image and self.image != 'default.jpg':
            img = Image.open(self.image)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                in_mem_file = ContentFile(img.tobytes())
                img.save(in_mem_file, img.format)
                in_mem_file.seek(0)
                self.image.save(self.image.name, in_mem_file, save=False)  # Save to the same file
                super().save(*args, **kwargs)