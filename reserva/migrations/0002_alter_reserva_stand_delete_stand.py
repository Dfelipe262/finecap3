# Generated by Django 4.2.5 on 2023-10-20 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stand', '0001_initial'),
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='stand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stand.stand'),
        ),
        migrations.DeleteModel(
            name='Stand',
        ),
    ]