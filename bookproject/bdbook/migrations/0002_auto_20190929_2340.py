# Generated by Django 2.2.5 on 2019-09-29 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]