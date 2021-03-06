# Generated by Django 2.2.5 on 2019-12-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, null=True, verbose_name='criado em')),
                ('modificado', models.DateTimeField(auto_now=True, null=True, verbose_name='modificado em')),
                ('nome', models.CharField(max_length=30, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'exercicio',
            },
        ),
    ]
