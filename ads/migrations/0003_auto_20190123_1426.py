# Generated by Django 2.1.4 on 2019-01-23 14:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ads', '0002_auto_20190123_1426'),
    ]

    operations = [

        # Django considers "id" the primary key of these tables, but
        # Postgres-XL want the primary key to be (company_id, id)
        migrations.RunSQL("""
      ALTER TABLE ads_campaign
      DROP CONSTRAINT ads_campaign_pkey CASCADE;

      ALTER TABLE ads_campaign
      ADD CONSTRAINT ads_campaign_pkey
      PRIMARY KEY (company_id, id)
    """),

        migrations.RunSQL("""
      ALTER TABLE ads_ads
      DROP CONSTRAINT ads_ads_pkey CASCADE;

      ALTER TABLE ads_ads
      ADD CONSTRAINT ads_ads_pkey
      PRIMARY KEY (company_id, id)
    """),

        migrations.RunSQL(
            "ALTER TABLE public.ads_campaign DISTRIBUTE BY HASH(company_id);"
        ),

        migrations.RunSQL(
            "ALTER TABLE public.ads_ads DISTRIBUTE BY HASH(company_id);"
        ),
    ]