# Generated by Django 3.1 on 2022-08-11 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MTV', '0002_auto_20220810_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opt1', models.BooleanField(default=False)),
                ('opt2', models.BooleanField(default=False)),
                ('opt3', models.BooleanField(default=False)),
                ('opt4', models.BooleanField(default=False)),
                ('opt5', models.BooleanField(default=False)),
                ('opt6', models.BooleanField(default=False)),
                ('opt7', models.BooleanField(default=False)),
                ('opt8', models.BooleanField(default=False)),
                ('opt9', models.BooleanField(default=False)),
                ('opt10', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MTV.car')),
            ],
        ),
        migrations.CreateModel(
            name='OptionC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opt1', models.BooleanField(default=False)),
                ('opt2', models.BooleanField(default=False)),
                ('opt3', models.BooleanField(default=False)),
                ('opt4', models.BooleanField(default=False)),
                ('opt5', models.BooleanField(default=False)),
                ('opt6', models.BooleanField(default=False)),
                ('opt7', models.BooleanField(default=False)),
                ('opt8', models.BooleanField(default=False)),
                ('opt9', models.BooleanField(default=False)),
                ('opt10', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MTV.car')),
            ],
        ),
        migrations.CreateModel(
            name='OptionB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opt1', models.BooleanField(default=False)),
                ('opt2', models.BooleanField(default=False)),
                ('opt3', models.BooleanField(default=False)),
                ('opt4', models.BooleanField(default=False)),
                ('opt5', models.BooleanField(default=False)),
                ('opt6', models.BooleanField(default=False)),
                ('opt7', models.BooleanField(default=False)),
                ('opt8', models.BooleanField(default=False)),
                ('opt9', models.BooleanField(default=False)),
                ('opt10', models.BooleanField(default=False)),
                ('opt11', models.BooleanField(default=False)),
                ('opt12', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MTV.car')),
            ],
        ),
        migrations.CreateModel(
            name='OptionA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opt1', models.BooleanField(default=False)),
                ('opt2', models.BooleanField(default=False)),
                ('opt3', models.BooleanField(default=False)),
                ('opt4', models.BooleanField(default=False)),
                ('opt5', models.BooleanField(default=False)),
                ('opt6', models.BooleanField(default=False)),
                ('opt7', models.BooleanField(default=False)),
                ('opt8', models.BooleanField(default=False)),
                ('opt9', models.BooleanField(default=False)),
                ('opt10', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MTV.car')),
            ],
        ),
    ]
