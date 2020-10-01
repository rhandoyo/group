from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Usermasuk (models.Model):
    nama_user_masuk = models.ForeignKey(User, on_delete=models.CASCADE,related_name='semua_user_masuk')
    poto_profil     = models.ImageField(upload_to='profil/', default='', null=True, blank=True)
    email           = models.EmailField(max_length=254)
    jenis_kelamin   = models.CharField(max_length=10)

    def __str__(self):
        return str(self.nama_user_masuk)
    

class Post(models.Model):
    nama          = models.ForeignKey(Usermasuk, on_delete=models.CASCADE, related_name='semua_postingan')
    status        = models.TextField()
    gambar        = models.ImageField(upload_to='images/', default='', null=True, blank=True)
    waktu_posting = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return str(self.nama)
    