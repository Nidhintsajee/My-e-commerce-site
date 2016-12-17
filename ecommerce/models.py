from django.db import models
from django.utils import timezone
import os.path
from PIL import Image
#from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile

class Product(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    product_image = models.ImageField(upload_to='pictures/')
    published_date = models.DateTimeField(blank = True, null = True)
    thumbnail = models.ImageField(upload_to="thumbnails/")
    caption = models.CharField(max_length = 250, blank =True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self, force_update=False, force_insert=False, thumb_size=(180,300)):
       	product_image = Image.open(self.product_image)
        if product_image.mode not in ('L', 'RGB'):
        	product_image = product_image.convert('RGB')
       	self.product_image_width, self.product_image_height = product_image.size
       	product_image.thumbnail(thumb_size, Image.ANTIALIAS)
       	temp_handle = StringIO()
       	product_image.save(temp_handle, 'png')
       	temp_handle.seek(0)
       	suf = SimpleUploadedFile(os.path.split(self.product_image.name)[-1],temp_handle.read(),content_type='image/png')
        self.thumbnail.save(suf.name+'.png', suf, save=False)
       	self.thumbnail_width, self.thumbnail_height = product_image.size
       	super(Product, self).save(force_update, force_insert)

