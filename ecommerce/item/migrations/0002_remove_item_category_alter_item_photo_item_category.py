# Generated by Django 5.0.2 on 2024-02-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to='Media/item/Photos'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(to='item.category'),
        ),
    ]
