# Generated by Django 4.2.2 on 2023-07-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chocolate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pic')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
