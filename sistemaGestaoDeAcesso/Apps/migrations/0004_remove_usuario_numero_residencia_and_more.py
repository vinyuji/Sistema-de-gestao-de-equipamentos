# Generated by Django 4.2.21 on 2025-07-09 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0003_usuario_cep_usuario_cpf_usuario_numero_matricula_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='numero_residencia',
        ),
        migrations.AddField(
            model_name='usuario',
            name='numero_telefone',
            field=models.CharField(default=0, max_length=10, verbose_name='Número de telefone'),
            preserve_default=False,
        ),
    ]
