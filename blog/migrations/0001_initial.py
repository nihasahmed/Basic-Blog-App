# Generated by Django 2.2.7 on 2019-11-27 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('postdate', models.DateTimeField(auto_now_add=True)),
                ('editdate', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
