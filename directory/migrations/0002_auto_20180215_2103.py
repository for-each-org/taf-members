# Generated by Django 2.0.2 on 2018-02-15 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256)),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social',
        ),
        migrations.AddField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_img_url',
            field=models.URLField(max_length=256),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.URLField(max_length=256),
        ),
        migrations.AddField(
            model_name='socialfield',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Profile'),
        ),
    ]