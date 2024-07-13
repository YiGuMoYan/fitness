import os
from pprint import pprint

import yaml
from erniebot_agent.extensions.langchain.embeddings import ErnieEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import SpacyTextSplitter
from langchain_community.vectorstores import FAISS

os.environ["EB_AGENT_ACCESS_TOKEN"] = "7c0e2b5a75b0bf32286c9bf6b78729553e67d54c"

aistudio_access_token = os.environ.get("EB_AGENT_ACCESS_TOKEN", "")
embeddings = ErnieEmbeddings(aistudio_access_token=aistudio_access_token, chunk_size=16)

faiss_name = "faiss_index"
if os.path.exists(faiss_name):
    db = FAISS.load_local(faiss_name, embeddings)
else:
    loader = PyPDFDirectoryLoader(r"D:\Document\Project\fitness\fitness\task\erine_bot\pdf")
    documents = loader.load()
    text_splitter = SpacyTextSplitter(pipeline="zh_core_web_sm", chunk_size=320, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    docs = [doc.page_content[:500] if len(doc.page_content) >= 500 else doc for doc in docs]
    pprint(docs)
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(faiss_name)
