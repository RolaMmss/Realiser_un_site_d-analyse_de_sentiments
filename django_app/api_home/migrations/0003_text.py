# Generated by Django 4.2.3 on 2023-07-12 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_home', '0002_rename_nom_patient_firstname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('evaluation', models.FloatField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_home.patient')),
            ],
            options={
                'verbose_name_plural': 'Texts',
            },
        ),
    ]
