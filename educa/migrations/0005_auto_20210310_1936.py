# Generated by Django 3.1.7 on 2021-03-10 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('educa', '0004_auto_20210310_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='educa.course', verbose_name='course'),
        ),
    ]
