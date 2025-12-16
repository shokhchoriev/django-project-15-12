from django.db import models

# Create your models here.

class Kurtka(models.Model):
    nomi = models.CharField(max_length=250)
    brend = models.CharField(max_length=250)
    rang = models.CharField(max_length=250)
    narx = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    skidka = models.IntegerField()
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi

class futbolka(models.Model):
    brend = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    cost = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    coutry = models.CharField(max_length=255)
    we_have = models.IntegerField()
    datatime = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    parant_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
            return self.brend

    def save(self, *args, **kwargs):
        print("salom")
        super().save(*args, **kwargs)

class Telefon (models. Model):
    class RamChoices (models. TextChoices):
        gb4 = "gb4","4 gb"
        gb8 = "gb8", "8 gb"
    class ColorChoices (models. TextChoices):
        black = "qora", "Qora"
        white = "oq","Oq"
        red = "qizil","Qizil"
    class BrendChoices (models. TextChoices):
        samsung = "samsung"
        iphone = "iphone",
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    image = models. ImageField (upload_to="product/")
    color = models.CharField(max_length=30, choices=ColorChoices. choices)
    brend = models.CharField(max_length=30, choices=BrendChoices. choices)
    ram = models. CharField(max_length=30, choices=RamChoices. choices)  

    def __str__(self):
        return self. brend