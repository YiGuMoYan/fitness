import os
import asyncio
import warnings

from asgiref.sync import sync_to_async
from erniebot_agent.agents import FunctionAgentWithRetrieval
from erniebot_agent.chat_models import ERNIEBot
from erniebot_agent.extensions.langchain.embeddings import ErnieEmbeddings
from langchain_community.vectorstores import FAISS

import django

# 设置 DJANGO_SETTINGS_MODULE 环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness.settings')
# 初始化 Django 设置
django.setup()

from account.models import Account
from body.models import Body
from diet.models import Diet
from task.erine_bot.faiss_searcher import FaissSearcher
from training_log.models import TrainingLog

# 禁用弃用警告
warnings.filterwarnings("ignore", category=DeprecationWarning)

os.environ["EB_AGENT_ACCESS_TOKEN"] = "7c0e2b5a75b0bf32286c9bf6b78729553e67d54c"

aistudio_access_token = os.environ.get("EB_AGENT_ACCESS_TOKEN", "")
llm = ERNIEBot(model="ernie-3.5")

# 实例化 ErnieEmbeddings
embeddings = ErnieEmbeddings(aistudio_access_token=aistudio_access_token, chunk_size=16)
faiss_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faiss_index")
print(faiss_name)
db = FAISS.load_local(folder_path=faiss_name, embeddings=embeddings, allow_dangerous_deserialization=True)
faiss_search = FaissSearcher(db=db, embeddings=embeddings)

# 创建 FunctionAgentWithRetrieval 实例
agent = FunctionAgentWithRetrieval(
    llm=llm, tools=[], knowledge_base=faiss_search, threshold=0.9
)


# 定义辅助函数
def get_account_ids():
    return list(Account.objects.values_list("id", flat=True))


def get_body_records(user_id):
    return list(Body.objects.filter(user_id=user_id).order_by('-record_date')[:3])


def get_diet_records(user_id):
    return list(Diet.objects.filter(user_id=user_id).order_by('-record_date')[:3])


def get_training_logs(user_id):
    return list(TrainingLog.objects.filter(user_id=user_id).order_by('-date')[:3])


def save_account_comment(user_id, text):
    account = Account.objects.get(id=user_id)
    account.comment = text
    account.save()


async def run():
    account_id_list = await sync_to_async(get_account_ids)()
    for account_id in account_id_list:
        params = "当前用户近期的身体身高与体重为："
        body_records = await sync_to_async(get_body_records)(account_id)
        for b in body_records:
            params += f"{b.height}cm {b.weight}kg"
        diet_records = await sync_to_async(get_diet_records)(account_id)
        params += "，饮食习惯为："
        for d in diet_records:
            params += f"{d.breakfast} {d.lunch} {d.dinner}"
        training_logs = await sync_to_async(get_training_logs)(account_id)
        params += "，训练习惯为："
        for t in training_logs:
            params += f"{t.content} {t.date}"
        params += "，请对用户进行评价，同时，给出他接下来的训练建议。"
        response = await agent.run(params)
        text = response.text
        await sync_to_async(save_account_comment)(account_id, text)


# 运行异步任务
asyncio.run(run())
