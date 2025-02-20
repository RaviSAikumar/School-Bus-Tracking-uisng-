# Generated by Django 4.1.4 on 2022-12-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildModels',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('children_rollnum', models.CharField(help_text='children_rollnum', max_length=50, null=True)),
                ('children_name', models.CharField(help_text='collector_name', max_length=50)),
                ('children_mothername', models.CharField(help_text='children_mothername', max_length=50)),
                ('children_fathername', models.CharField(help_text='collector_fathername', max_length=50)),
                ('children_contact', models.CharField(help_text='children_contact', max_length=50, null=True)),
                ('children_email', models.EmailField(help_text='children_email', max_length=254)),
                ('children_password', models.CharField(help_text='children_password', max_length=50, null=True)),
                ('children_address', models.TextField(help_text='children_address')),
                ('children_class', models.CharField(help_text='children_class', max_length=50)),
                ('children_image', models.ImageField(help_text='children_image', null=True, upload_to='')),
                ('children_qrcode', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'childrens_data',
            },
        ),
    ]
