# Generated by Django 3.1.6 on 2021-06-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='info_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('qr_code', models.ImageField(upload_to='passport')),
                ('surname', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='data_cert',
        ),
    ]
