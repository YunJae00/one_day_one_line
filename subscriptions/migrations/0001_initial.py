# Generated by Django 4.2 on 2025-04-20 01:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contents', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', '활성'), ('paused', '일시중지'), ('cancelled', '취소')], default='active', max_length=10, verbose_name='상태')),
                ('frequency', models.CharField(choices=[('daily', '매일'), ('three_per_week', '주 3회 (월/수/금)'), ('weekly', '주 1회 (월요일)')], default='daily', max_length=15, verbose_name='수신 주기')),
                ('preferred_time', models.TimeField(default=datetime.time(8, 0), verbose_name='선호 시간')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='시작일')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='종료일')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='contents.category', verbose_name='카테고리')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '구독',
                'db_table': 'subscriptions',
            },
        ),
    ]
