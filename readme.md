
Example of usage Django and Postgres-XL
---------------------------------------



1. Install Postgres-XL

    https://omidraha.com/en/latest/src/postgresql/postgres-xl.html#setting-up-postgres-xl-cluster



Errors
------

1. `could not plan this distributed update`

```python

    camp = Campaign.objects.first()
    camp.name = 'CP1-UPDATED'
    camp.save()
```

By default Django apply save on all fields, even on FK:

```
self

<django.db.backends.utils.CursorDebugWrapper object at 0x7fcc6d054278>

sql

('UPDATE "ads_campaign" SET "created_at" = '
 '\'2019-01-29T14:23:32+00:00\'::timestamptz, "name" = \'CP1-UPDATED\', "company_id" = '
 '1, "updated_at" = \'2019-01-29T14:23:32.128076+00:00\'::timestamptz WHERE '
 '"ads_campaign"."id" = 1')
```

That is not allowed on distributed column:

```
could not plan this distributed update
DETAIL:  correlated UPDATE or updating distribution column currently not supported in Postgres-XL.
```

To fix this problem:

```python

    camp = Campaign.objects.first()
    camp.name = 'CP1-UPDATED'
    camp.save(update_fields=['name']))

```


http://lists.postgres-xl.org/pipermail/postgres-xl-general-postgres-xl.org/2015-May/000494.html

https://docs.djangoproject.com/en/2.0/ref/models/instances/#specifying-which-fields-to-save
