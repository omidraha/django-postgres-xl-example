# Generated by Django 2.1.5 on 2019-01-30 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_samplec'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE public.ads_samplec DISTRIBUTE BY HASH(id);"
        ),

    ]
