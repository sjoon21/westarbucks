# Generated by Django 4.0.2 on 2022-02-13 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergys',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=45)),
                ('english_name', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'drinks',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kcal', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('sodium', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('sugar', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('caffeine', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('dirnk_nu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=45)),
                ('size_ml', models.CharField(max_length=45)),
                ('size_ounce', models.CharField(max_length=45)),
                ('nutrition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.nutrition')),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
        migrations.CreateModel(
            name='Allergy_drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
            ],
            options={
                'db_table': 'allergy_drinks',
            },
        ),
        migrations.AddField(
            model_name='allergy',
            name='name',
            field=models.ManyToManyField(through='products.Allergy_drink', to='products.Drink'),
        ),
    ]
