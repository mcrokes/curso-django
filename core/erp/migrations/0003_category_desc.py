# Generated by Django 4.2.3 on 2023-07-25 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_alter_category_id_alter_client_id_alter_detsale_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción'),
        ),
    ]