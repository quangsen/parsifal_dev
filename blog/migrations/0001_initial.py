# Generated by Django 2.2.1 on 2019-05-31 07:56

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
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, max_length=4000, null=True)),
                ('summary', models.TextField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('H', 'Hidden'), ('P', 'Published')], max_length=10)),
                ('start_publication', models.DateTimeField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
