# Generated by Django 3.2.8 on 2021-10-21 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image_url', models.URLField()),
                ('bio', models.TextField()),
                ('contact_message', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('resume_download', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillmessage', models.CharField(max_length=200)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=40)),
                ('years', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('user', models.CharField(max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('class_name', models.CharField(max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level', models.PositiveIntegerField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=20)),
                ('image_url', models.URLField()),
                ('url', models.URLField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.portfolio')),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('logo_url', models.URLField()),
                ('website_url', models.URLField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('graduated', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.PositiveIntegerField()),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]
