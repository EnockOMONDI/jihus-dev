# Generated by Django 2.0.1 on 2020-10-09 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_create_initial_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='subject',
        ),
        migrations.AddField(
            model_name='quiz',
            name='Completion_ext',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='quiz',
            name='Invitation_Text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='quiz',
            name='Maximum_resends',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='quiz',
            name='Survey_Type',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=20),
        ),
        migrations.AddField(
            model_name='quiz',
            name='Target',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='quiz',
            name='Trigger_Code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='quiz',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('PUblished', 'Published')], default='Draft', max_length=20),
        ),
        migrations.AddField(
            model_name='quiz',
            name='channels',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='classroom.Channels'),
        ),
    ]
