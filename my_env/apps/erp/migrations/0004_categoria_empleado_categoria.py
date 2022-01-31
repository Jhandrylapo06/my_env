# Generated by Django 4.0.1 on 2022-01-31 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_tipo_empleado_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='categoria',
            field=models.ManyToManyField(to='erp.Categoria'),
        ),
    ]