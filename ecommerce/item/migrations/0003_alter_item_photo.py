# Generated by Django 5.0.2 on 2024-02-07 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_remove_item_category_alter_item_photo_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to='item_photos'),
        ),
    ]