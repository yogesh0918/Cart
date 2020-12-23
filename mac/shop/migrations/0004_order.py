# Generated by Django 3.0.2 on 2020-10-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
                ('address_line2', models.CharField(default='', max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
