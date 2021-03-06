# Generated by Django 3.1.2 on 2020-11-15 06:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.PositiveIntegerField(choices=[(0, 'photograph'), (1, 'awesome photograph'), (2, 'gallery')], default=2, verbose_name='Category')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=1024)),
                ('thumb', models.ImageField(upload_to='albums')),
                ('tags', models.CharField(max_length=250)),
                ('is_visible', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=50, upload_to='albums')),
                ('thumb', models.ImageField(blank=True, max_length=50, upload_to='albums')),
                ('desc', models.CharField(default='The author is too lazy and leave nothing!', max_length=300)),
                ('like_num', models.PositiveIntegerField(default=0, verbose_name='like number')),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('alt', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=70)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='album.album')),
            ],
        ),
    ]
