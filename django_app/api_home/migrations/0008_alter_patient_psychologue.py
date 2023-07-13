# Generated by Django 4.2.3 on 2023-07-12 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_home', '0007_alter_userprofile_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='psychologue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
