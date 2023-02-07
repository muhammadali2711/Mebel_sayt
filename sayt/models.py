import string
import random

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)
            while True:
                try:
                    root = Category.objects.get(slug=self.slug)
                except:
                    root = None

                if not root:
                    break
                else:
                    strr = str(self.content) + "_" + ''.join(random.choice(string.digits) for i in range(10))
                    self.slug = slugify(strr)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Category"


class Subcategory(models.Model):
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)


class Character(models.Model):
    waranty = models.CharField(max_length=128)
    collection = models.CharField(max_length=128)
    matras = models.CharField(max_length=128)
    Xususiyatlari = models.CharField(max_length=128)
    qoshimchalari = models.CharField(max_length=128)
    balandligi = models.CharField(max_length=128)
    mehanizm = models.CharField(max_length=128)
    massa = models.CharField(max_length=128)
    Maqsad = models.CharField(max_length=128)
    # BooleanField bolishim mumkinakan
    razmer = models.CharField(max_length=128)
    qattiqlik = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)

    class Meta:
        abstract = True


class Product(Character):
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_ctg = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=128)
    sale = models.DateTimeField()
    price = models.IntegerField()
    price_true = models.IntegerField(null=True, blank=True)
    credit = models.IntegerField()
    bonus = models.IntegerField()
    size = models.CharField(max_length=122)


class ProductImg(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='images')

    # def __str__(self):
    #     return self.product.name

    # def __str__(self):
    #     return self.waranty


class Tkan(models.Model):
    # pro = models.ForeignKey(Product, on_delete=models.CASCADE)
    tkan_name = models.CharField(max_length=128)
    color_name = models.CharField(max_length=222)
    tkan_material = models.CharField(max_length=126)
    tkan_price = models.IntegerField()

    # def __str__(self):
    #     return self.tkan_name


class ProductTkanImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tkan = models.ForeignKey(Tkan, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="Tkan")


class ProductTkanAdd(models.Model):
    product = models.ForeignKey(ProductTkanImg, on_delete=models.CASCADE)
