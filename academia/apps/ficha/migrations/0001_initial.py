# Generated by Django 2.2.5 on 2019-12-07 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, null=True, verbose_name='criado em')),
                ('modificado', models.DateTimeField(auto_now=True, null=True, verbose_name='modificado em')),
                ('obs', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ficha',
            },
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, null=True, verbose_name='criado em')),
                ('modificado', models.DateTimeField(auto_now=True, null=True, verbose_name='modificado em')),
                ('titulo', models.CharField(blank=True, max_length=3, verbose_name='Treino')),
            ],
            options={
                'db_table': 'treino',
            },
        ),
        migrations.CreateModel(
            name='FichaExercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, null=True, verbose_name='criado em')),
                ('modificado', models.DateTimeField(auto_now=True, null=True, verbose_name='modificado em')),
                ('series', models.CharField(default=None, max_length=1, null=True, verbose_name='Séries')),
                ('repeticoes', models.CharField(default=None, max_length=2, null=True, verbose_name='Repetições')),
                ('exercicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercicio.Exercicio')),
                ('ficha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ficha.Ficha')),
                ('treino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ficha.Treino')),
            ],
            options={
                'db_table': 'ficha_exercicio',
            },
        ),
        migrations.CreateModel(
            name='FichaAtual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, null=True, verbose_name='criado em')),
                ('modificado', models.DateTimeField(auto_now=True, null=True, verbose_name='modificado em')),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.Ficha')),
            ],
            options={
                'db_table': 'ficha_atual',
            },
        ),
    ]
