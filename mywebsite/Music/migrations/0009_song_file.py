# Generated by Django 3.0.6 on 2020-06-05 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0008_auto_20200603_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
