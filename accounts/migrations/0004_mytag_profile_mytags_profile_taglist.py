# Generated by Django 4.1.7 on 2023-06-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_userimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mytagname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='mytags',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='taglist',
            field=models.ManyToManyField(blank=True, related_name='users', to='accounts.mytag'),
        ),
    ]