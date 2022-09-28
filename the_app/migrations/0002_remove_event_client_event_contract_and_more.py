# Generated by Django 4.1 on 2022-09-28 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='client',
        ),
        migrations.AddField(
            model_name='event',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='the_app.contract'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Gestion', 'Gestion'), ('Vente', 'Vente'), ('Support', 'Support')], default='Vente', max_length=255),
        ),
    ]
