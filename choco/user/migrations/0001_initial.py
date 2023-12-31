# Generated by Django 4.2.2 on 2023-07-08 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='bookingform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_naame', models.CharField(max_length=50)),
                ('purchase_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('quantity', models.CharField(max_length=50)),
                ('delivery_address', models.CharField(max_length=100)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.chocolate')),
            ],
        ),
    ]
