from django.db import models



class ImageModel(models.Model):
    code = models.CharField(max_length=255, unique=True)
    image = models.ImageField(null=False)
    
    def __str__(self) -> str:
        return f"{self.code}"