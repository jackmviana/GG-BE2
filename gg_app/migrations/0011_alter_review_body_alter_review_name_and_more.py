# Generated by Django 4.1.4 on 2022-12-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gg_app', '0010_alter_review_body_alter_review_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.CharField(default='no body', max_length=250),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(default='no name', max_length=250),
        ),
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.CharField(default='no photo', max_length=250),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
