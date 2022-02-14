from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Drink (models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

class Image (models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    allergy_name = models.CharField(max_length=45)
    name = models.ManyToManyField('Drink', through="Allergy_drink")

    class Meta:
        db_table = 'allergys'

class Allergy_drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_drinks'

class Nutrition(models.Model):
    kcal = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    sodium = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    fat = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    sugar = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    protein = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    caffeine = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    dirnk_nu = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'

class Size(models.Model):
    size_name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45)
    size_ounce = models.CharField(max_length=45)
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE)


    class Meta:
        db_table = 'sizes'