# Generated by Django 2.2.5 on 2019-12-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0010_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='image',
            field=models.ImageField(default='', upload_to='department_images/'),
        ),
    ]
