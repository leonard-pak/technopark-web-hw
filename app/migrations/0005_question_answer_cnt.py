# Generated by Django 4.0.3 on 2022-04-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_likeforanswer_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_cnt',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
