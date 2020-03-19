from django.db import models

# Veri Tabanı entegrasyon kısmı

class Author(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')

#kitap ve yazarlar arasında ilişki kuracaz.

class Book(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')
    # Author ile oluşturduğumuz tablo ile ilişkilendirdik.
    # on_delete ise yazar silinirse kitapları da silinmesi için yaptık.
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2,max_digits=4,null=True)

