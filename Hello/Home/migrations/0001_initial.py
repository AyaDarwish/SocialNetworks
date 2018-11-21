# Generated by Django 2.0.5 on 2018-05-03 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, null=True)),
                ('like', models.PositiveIntegerField(default=0)),
                ('comment', models.PositiveIntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_No', models.CharField(max_length=11)),
                ('Birthdate', models.DateField()),
                ('Gender', models.CharField(max_length=100)),
                ('posts', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='userr',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Home.User'),
        ),
        migrations.AddField(
            model_name='likes',
            name='postt',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Home.Post'),
        ),
        migrations.AddField(
            model_name='likes',
            name='userr',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Home.User'),
        ),
        migrations.AddField(
            model_name='comments',
            name='postt',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Home.Post'),
        ),
        migrations.AddField(
            model_name='comments',
            name='userr',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Home.User'),
        ),
    ]
