# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 01:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('encrypted_password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ordered_at', models.DateTimeField(auto_now=True)),
                ('ordered_quantity', models.IntegerField()),
                ('received_at', models.DateTimeField(null=True)),
                ('received_quantity', models.IntegerField(default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('registered_date', models.DateField()),
                ('price', models.IntegerField()),
                ('currency_unit', models.CharField(choices=[('JPY', 'JPY'), ('USD', 'USD'), ('EUR', 'EUR')], default='JPY', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Maker')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnpackHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('unpacked_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product')),
            ],
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product'),
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Shop'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.PriceHistory'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product'),
        ),
        migrations.AddField(
            model_name='externalaccount',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Shop'),
        ),
        migrations.AlterUniqueTogether(
            name='unpackhistory',
            unique_together=set([('product', 'unpacked_at', 'owner')]),
        ),
        migrations.AlterUniqueTogether(
            name='pricehistory',
            unique_together=set([('product', 'registered_date', 'shop')]),
        ),
        migrations.AlterUniqueTogether(
            name='orderhistory',
            unique_together=set([('product', 'ordered_at', 'owner')]),
        ),
        migrations.AlterUniqueTogether(
            name='externalaccount',
            unique_together=set([('name', 'shop')]),
        ),
    ]
