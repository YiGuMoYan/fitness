import asyncio
from datetime import datetime

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore

from task.erine_bot.agent import run, run_async_task


class Command(BaseCommand):
    help = '启动定时任务.'

    def handle(self, *args, **options):
        # 调度器
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)

        # 任务存储
        scheduler.add_jobstore(DjangoJobStore(), 'default')

        # 配置线程池执行器，限制最大并发数为1，防止并发
        executor = ThreadPoolExecutor(max_workers=1)
        scheduler.executor = executor

        # 注册定义任务
        id_print_task = 'print_task_job'
        print('开始-增加任务({})'.format(id_print_task))

        # 使用 CronTrigger 设置每天20:50执行任务
        scheduler.add_job(
            run_async_task,
            id=id_print_task,
            name=id_print_task,
            max_instances=1,
            replace_existing=True,
            trigger=CronTrigger(hour=24, minute=0, second=0, timezone=settings.TIME_ZONE),
        )
        print('完成-增加任务({})'.format(id_print_task))

        # 启动定时任务
        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
