# Generated by Django 4.2.13 on 2024-11-04 13:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_category', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='P',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_p', models.CharField(max_length=64, unique=True)),
                ('description_p', models.TextField()),
                ('text_p', models.TextField()),
                ('quantity_p', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('cost_p', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('datetime_p', models.DateTimeField(auto_now_add=True)),
                ('category_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='simpleapp.category')),
            ],
        ),
    ]
