# ./task/task_list.py

from datetime import datetime


def print_task():
    print('Scheduler测试任务执行：{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
