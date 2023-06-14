# Generated by Django 2.2.17 on 2023-06-06 13:49

from django.db import migrations, models
import django.db.models.deletion
import django_jsonfield_backport.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'object_pk',
                    models.CharField(
                        db_index=True, max_length=255, verbose_name='object pk'
                    ),
                ),
                (
                    'object_id',
                    models.BigIntegerField(
                        blank=True,
                        db_index=True,
                        null=True,
                        verbose_name='object id',
                    ),
                ),
                (
                    'object_repr',
                    models.TextField(verbose_name='object representation'),
                ),
                (
                    'action',
                    models.PositiveSmallIntegerField(
                        choices=[(0, 'create'), (1, 'update'), (2, 'delete')],
                        db_index=True,
                        verbose_name='action',
                    ),
                ),
                (
                    'changes',
                    models.TextField(
                        blank=True, verbose_name='change message'
                    ),
                ),
                ('actor', models.TextField(verbose_name='actor')),
                (
                    'remote_addr',
                    models.GenericIPAddressField(
                        blank=True, null=True, verbose_name='remote address'
                    ),
                ),
                (
                    'timestamp',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='timestamp'
                    ),
                ),
                (
                    'additional_data',
                    django_jsonfield_backport.models.JSONField(
                        blank=True, null=True, verbose_name='additional data'
                    ),
                ),
                (
                    'content_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='+',
                        to='contenttypes.ContentType',
                        verbose_name='content type',
                    ),
                ),
            ],
            options={
                'verbose_name': 'log entry',
                'verbose_name_plural': 'log entries',
                'ordering': ['-timestamp'],
                'get_latest_by': 'timestamp',
            },
        ),
    ]