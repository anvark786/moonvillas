# Generated by Django 4.0.1 on 2022-01-14 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwoBhk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ground_floor_list_item', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='web/VillaDetails/')),
            ],
        ),
    ]