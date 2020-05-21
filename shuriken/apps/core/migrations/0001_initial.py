# Generated by Django 3.0.6 on 2020-05-15 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='en', max_length=2)),
                ('location', models.CharField(default='jp', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('company', models.CharField(max_length=64)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post')),
            ],
        ),
    ]
