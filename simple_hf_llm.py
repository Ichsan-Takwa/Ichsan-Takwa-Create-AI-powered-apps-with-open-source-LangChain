# using Hugging FaceHub
import os
from langchain_community.llms import HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")
text = "tell me insteresting fact about potato"
result = llm.invoke(text)
print(result)