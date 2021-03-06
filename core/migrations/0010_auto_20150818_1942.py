# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_homepage_number_of_columns_of_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='number_of_rows_of_external_articles',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='homepage',
            name='number_of_rows_of_visualizations',
            field=models.IntegerField(default=2),
        ),
    ]
