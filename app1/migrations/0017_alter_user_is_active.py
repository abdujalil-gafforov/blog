# Generated by Django 4.1.3 on 2022-12-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_post_options_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
