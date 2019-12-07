# Generated by Django 3.0 on 2019-12-07 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myproject.apps.ideas2.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories2', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('picture', models.ImageField(upload_to=myproject.apps.ideas2.models.upload_to, verbose_name='Picture')),
                ('rating', models.PositiveIntegerField(blank=True, choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], null=True, verbose_name='Rating')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_ideas2', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('categories', models.ManyToManyField(related_name='category_ideas', to='categories2.Category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
            },
        ),
    ]
