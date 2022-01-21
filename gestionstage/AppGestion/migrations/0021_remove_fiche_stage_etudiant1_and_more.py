# Generated by Django 4.0 on 2022-01-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestion', '0020_alter_fiche_stage_sujet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiche_stage',
            name='Etudiant1',
        ),
        migrations.RemoveField(
            model_name='fiche_stage',
            name='Etudiant2',
        ),
        migrations.RemoveField(
            model_name='fiche_stage',
            name='Etudiant3',
        ),
        migrations.AddField(
            model_name='fiche_stage',
            name='Etudiant',
            field=models.ManyToManyField(to='AppGestion.Stagiaire'),
        ),
        migrations.AlterField(
            model_name='fiche_stage',
            name='Groupe',
            field=models.IntegerField(),
        ),
    ]
