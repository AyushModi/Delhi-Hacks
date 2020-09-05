# Generated by Django 3.1.1 on 2020-09-05 21:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200905_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machinery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=12)),
                ('surname', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('product', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField()),
                ('production_date', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=9)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Machinerie',
        ),
        migrations.RemoveField(
            model_name='crop',
            name='title',
        ),
        migrations.AddField(
            model_name='crop',
            name='condition',
            field=models.CharField(default=django.utils.timezone.now, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='email',
            field=models.EmailField(default='a@b.c', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='forename',
            field=models.CharField(default='c', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='location',
            field=models.CharField(default='d', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='product',
            field=models.CharField(default='e', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='production_date',
            field=models.DateField(default='2020-09-05'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='quantity',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='surname',
            field=models.CharField(default='h', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='telephone',
            field=models.CharField(default='12345-67890', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crop',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]
