# Generated by Django 4.2.2 on 2023-08-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(null=True)),
                ('updated', models.DateTimeField(null=True)),
                ('deleted', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'ref_kategori',
            },
        ),
    ]