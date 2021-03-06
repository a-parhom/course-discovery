# Generated by Django 1.9.11 on 2017-02-01 07:32


import django.db.models.deletion
import django_extensions.db.fields
import django_fsm
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publisher', '0030_create_switch_add_instructor_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRunState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', django_fsm.FSMField(choices=[('draft', 'Draft'), ('review', 'Review'), ('approved', 'Approved'), ('published', 'Published')], default='draft', max_length=50)),
                ('approved_by_role', models.CharField(blank=True, choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, null=True)),
                ('owner_role', models.CharField(choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63)),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_run', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_run_state', to='publisher.CourseRun')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='CourseState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', django_fsm.FSMField(choices=[('draft', 'Draft'), ('review', 'Review'), ('approved', 'Approved')], default='draft', max_length=50)),
                ('approved_by_role', models.CharField(blank=True, choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, null=True)),
                ('owner_role', models.CharField(choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63)),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_state', to='publisher.Course')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCourseRunState',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', django_fsm.FSMField(choices=[('draft', 'Draft'), ('review', 'Review'), ('approved', 'Approved'), ('published', 'Published')], default='draft', max_length=50)),
                ('approved_by_role', models.CharField(blank=True, choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, null=True)),
                ('owner_role', models.CharField(choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('changed_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('course_run', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='publisher.CourseRun')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical course run state',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCourseState',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', django_fsm.FSMField(choices=[('draft', 'Draft'), ('review', 'Review'), ('approved', 'Approved')], default='draft', max_length=50)),
                ('approved_by_role', models.CharField(blank=True, choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, null=True)),
                ('owner_role', models.CharField(choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('changed_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='publisher.Course')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical course state',
            },
        ),
    ]
