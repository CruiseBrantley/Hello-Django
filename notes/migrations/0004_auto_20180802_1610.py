# Generated by Django 2.1 on 2018-08-02 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='photo',
            field=models.ImageField(upload_to='notestorage'),
        ),
    ]
