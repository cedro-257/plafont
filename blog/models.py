from django.conf import settings
from django.db import models
from PIL import Image

# Create your models here.
class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    IMAGE_MAX_SIZE = (800, 800)
    
    def resize_image(self):
        image =Image.open(self.image)
        image.thumbnail_size(self.IMAGE_MAX_SIZE)
        #sauvegarder de l'image redimensionner dans le systemes des fichiers
        #ce 'est pas la methodes save() du modele
        image.save(self.image.path)
        
class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
