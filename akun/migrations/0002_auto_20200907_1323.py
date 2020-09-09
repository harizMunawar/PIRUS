# Generated by Django 3.1.1 on 2020-09-07 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('akun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='akun_admin', to='akun.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='direkturrs',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='akun_direktur', to='akun.customuser'),
            preserve_default=False,
        ),
    ]