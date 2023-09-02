from django.db import models

class Musteri(models.Model):
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=50)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.isim} {self.soyisim}"

class Fırsat(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    anlasma = models.CharField(max_length=100)
    asama = models.CharField(max_length=100)
    kapanis = models.DateField()
    durum = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.musteri} {self.anlasma}"
       
