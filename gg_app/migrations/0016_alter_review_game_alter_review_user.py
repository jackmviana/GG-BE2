# Generated by Django 4.1.4 on 2022-12-30 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gg_app', '0015_alter_review_game_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='game',
            field=models.ForeignKey(default='no pk', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='gg_app.game'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default='no pk', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='gg_app.user'),
        ),
    ]
