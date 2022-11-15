# Generated by Django 3.2 on 2022-11-14 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('headshot', models.ImageField(blank=True, null=True, upload_to='authors')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField()),
                ('state', models.CharField(choices=[('published', 'Published'), ('not_published', 'Not published'), ('in_progress', 'In progress'), ('cancelled', 'Cancelled'), ('rejected', 'Rejected')], default='published', max_length=100)),
                ('isbn', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pages', models.PositiveIntegerField(default=200)),
                ('stock_count', models.PositiveIntegerField(default=30)),
                ('authors', models.ManyToManyField(related_name='books', to='book.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.publisher')),
                ('tags', models.ManyToManyField(blank=True, related_name='books', to='book.Tag')),
            ],
            options={
                'ordering': ['isbn'],
            },
        ),
    ]