# Generated by Django 4.0.5 on 2022-06-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmenu', '0003_menudrinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuAlcohol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('allergies', models.TextField()),
                ('image', models.URLField(max_length=250)),
                ('alt', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='menudessert',
            name='alt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menudrinks',
            name='alt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menumain',
            name='alt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menustarter',
            name='alt',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
