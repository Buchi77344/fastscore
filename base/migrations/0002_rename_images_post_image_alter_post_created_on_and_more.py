# Generated by Django 4.1.6 on 2023-11-25 15:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='images',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='CommentQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('comment_box', models.TextField()),
                ('publish', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.BooleanField(default=True)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='base.post')),
            ],
        ),
    ]
