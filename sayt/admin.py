from django.contrib import admin
from .models import *


# class TkanInline(admin.StackedInline):
#     model = Tkan
#     extra = 1


# class CharacterInline(admin.StackedInline):
#     model = Character
#     extra = 1
#


class ProductImgInline(admin.StackedInline):
    model = ProductImg
    extra = 1


class ProductTkanImg(admin.StackedInline):
    model = ProductImg
    extra = 1


# class Tkan(admin.StackedInline):
#     model = Tkan
#     extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgInline, ProductTkanImg]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
