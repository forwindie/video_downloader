# Generated by Django 2.0.4 on 2018-04-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'query_table',
            },
        ),
    ]
