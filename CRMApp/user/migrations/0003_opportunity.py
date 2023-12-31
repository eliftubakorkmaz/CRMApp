# Generated by Django 4.2.1 on 2023-09-02 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anlasma', models.DecimalField(decimal_places=2, max_digits=10)),
                ('asama', models.CharField(max_length=20)),
                ('kapanis', models.DateField()),
                ('durum', models.CharField(max_length=20)),
                ('Musteri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.musteri')),
            ],
        ),
    ]
