# Generated by Django 4.0.3 on 2022-05-01 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao_html',
            field=models.TextField(blank=True, help_text='Ex: <h1>Este é o melhor produto do mundo</h1>', null=True, verbose_name='Descrição em HTML'),
        ),
    ]
