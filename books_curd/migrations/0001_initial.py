# Generated by Django 4.2.1 on 2023-05-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, null=True)),
                ('author', models.CharField(max_length=10)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('image_path', models.URLField()),
            ],
        ),
    ]
