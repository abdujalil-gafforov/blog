# Generated by Django 4.1.3 on 2022-11-26 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='app1.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='default.png', upload_to='users'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
