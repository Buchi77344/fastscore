# Generated by Django 4.1.6 on 2023-11-25 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_delete_commentq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post_c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_box', to='base.post')),
            ],
        ),
    ]
