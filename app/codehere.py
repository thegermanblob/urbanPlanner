from openai import AzureOpenAI
import os


client = AzureOpenAI(
    api_key=os.environ.get("AZURE_OPENAI_APIKEY"),
    azure_endpoint= os.environ.get("AZURE_OPENAI_RESOURCE_URI")
)

development_name:str = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
search_endpoint: str = os.environ.get("AZURE_SEARCH_RESOURCE_URI")
search_index: str = os.environ.get("AZURE_SEARCH_INDEX_NAME")

res = client.chat.completions(
    development_name=development_name,
)

