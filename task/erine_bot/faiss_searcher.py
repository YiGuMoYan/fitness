from langchain_community.utils.math import cosine_similarity


class FaissSearcher:
    def __init__(self, db, embeddings):
        # 类的初始化方法，接收一个数据库实例并将其存储在类的实例变量 self.db 中，接收一个embeddings方法传到self.embeddings中
        self.db = db
        self.embeddings = embeddings

    def search(self, query: str, top_k: int = 10, **kwargs):
        # 定义一个搜索方法，接受一个查询字符串 'query' 和一个整数 'top_k'，默认为 10
        docs = self.db.similarity_search(query, top_k)
        # 调用数据库的 similarity_search 方法来获取与查询最相关的文档
        para_result = self.embeddings.embed_documents([i.page_content for i in docs])
        # 对获取的文档内容进行嵌入（embedding），以便进行相似性比较
        query_result = self.embeddings.embed_query(query)
        # 对查询字符串也进行嵌入
        similarities = cosine_similarity([query_result], para_result).reshape((-1,))
        # 计算查询嵌入和文档嵌入之间的余弦相似度
        retrieval_results = []
        for index, doc in enumerate(docs):
            retrieval_results.append(
                {"content": doc.page_content, "score": similarities[index], "title": doc.metadata["source"]}
            )
        # 遍历每个文档，将内容、相似度得分和来源标题作为字典添加到结果列表中
        return retrieval_results  # 返回包含搜索结果的列表
