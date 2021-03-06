# Generated by Django 3.0.4 on 2020-11-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
