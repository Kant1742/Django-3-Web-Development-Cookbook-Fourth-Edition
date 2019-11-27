# Generated by Django 3.0rc1 on 2019-11-27 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViralVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Title')),
                ('embed_code', models.TextField(blank=True, verbose_name='YouTube embed code')),
                ('anonymous_views', models.PositiveIntegerField(default=0, verbose_name='Anonymous impressions')),
                ('authenticated_views', models.PositiveIntegerField(default=0, verbose_name='Authenticated impressions')),
            ],
            options={
                'verbose_name': 'Viral video',
                'verbose_name_plural': 'Viral videos',
            },
        ),
    ]