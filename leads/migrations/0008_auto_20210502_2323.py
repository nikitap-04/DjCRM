# Generated by Django 3.1.4 on 2021-05-02 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_auto_20210502_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]
