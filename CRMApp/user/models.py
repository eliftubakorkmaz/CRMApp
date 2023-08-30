from django.db import models

class Musteri(models.Model):
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=50)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.isim} {self.soyisim}"
