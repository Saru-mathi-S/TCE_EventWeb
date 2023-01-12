# Generated by Django 3.2.16 on 2022-11-03 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_auto_20221103_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='club_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('venue', models.CharField(max_length=60, verbose_name='Venue')),
                ('image', models.ImageField(upload_to='static/clubevents', verbose_name='Image')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('time', models.CharField(max_length=20, verbose_name='Time')),
                ('contact_details', models.TextField(verbose_name='Contact details')),
                ('clubs', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.clubs', verbose_name='Club')),
            ],
        ),
        migrations.CreateModel(
            name='dept_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('venue', models.CharField(default='NULL', max_length=60, verbose_name='Venue')),
                ('hover_description', models.TextField(blank=True, default='', null=True, verbose_name='Hover Description')),
                ('time', models.CharField(default='', max_length=30, verbose_name='Time')),
                ('image', models.ImageField(upload_to='static/club', verbose_name='Image')),
                ('conducted_by', models.CharField(max_length=30, verbose_name='Organized By')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('rules', models.TextField(default='', verbose_name='Rules')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('rewards', models.TextField(default='', verbose_name='Rewards')),
                ('participants', models.CharField(choices=[('Inter-departmental', 'Inter-departmental'), ('Intra-departmental', 'Intra-departmental')], default='Intradepartmental', max_length=40, verbose_name='Inter or Intra')),
                ('OD', models.CharField(choices=[('OD will be Provided', 'OD will be Provided'), ('OD will not be Provided', 'OD will not be Provided')], default='OD will not be Provided', max_length=40, verbose_name='Info about OD')),
                ('participation_type', models.CharField(choices=[('Individual', 'Individual'), ('Team size-2', 'Team size-2'), ('Team size-3', 'Team size-3'), ('Team size-4', 'Team size-4'), ('Team size-5', 'Team size-5'), ('Team size-6', 'Team size-6')], default='Individual', max_length=40, verbose_name='Type of Participation')),
                ('contact_details', models.TextField(default='', verbose_name='Contact details')),
                ('link', models.URLField(default='', verbose_name='Registration Link')),
            ],
        ),
        migrations.RemoveField(
            model_name='event_cl',
            name='clubs',
        ),
        migrations.RemoveField(
            model_name='main',
            name='dashboard',
        ),
        migrations.DeleteModel(
            name='waste',
        ),
        migrations.RenameModel(
            old_name='dashboard',
            new_name='dept',
        ),
        migrations.DeleteModel(
            name='event_cl',
        ),
        migrations.DeleteModel(
            name='main',
        ),
        migrations.AddField(
            model_name='dept_events',
            name='dashboard',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.dept', verbose_name='Department'),
        ),
    ]