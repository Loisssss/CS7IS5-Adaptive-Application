# Generated by Django 2.0.3 on 2018-03-19 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('weight', models.FloatField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adaptive_dashboard.Keywords')),
                ('opinion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adaptive_dashboard.Attitude')),
            ],
        ),
        migrations.CreateModel(
            name='PageId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totallink', models.IntegerField(max_length=128)),
                ('effectivelink', models.IntegerField(max_length=128)),
                ('weight', models.FloatField(max_length=128)),
                ('pageid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adaptive_dashboard.PageId')),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='Male', max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='records',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adaptive_dashboard.User'),
        ),
        migrations.AddField(
            model_name='page',
            name='pageid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adaptive_dashboard.PageId'),
        ),
        migrations.AddField(
            model_name='page',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adaptive_dashboard.User'),
        ),
        migrations.AddField(
            model_name='keywords',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adaptive_dashboard.Topics'),
        ),
    ]
