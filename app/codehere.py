from openai import AzureOpenAI
import os


client = AzureOpenAI(
    api_key=os.environ.get("AZURE_OPENAI_APIKEY"),
    azure_endpoint= os.environ.get("AZURE_OPENAI_RESOURCE_URI"),
    api_version="2024-02-01"
)

development_name:str = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
search_endpoint: str = os.environ.get("AZURE_SEARCH_RESOURCE_URI")
search_index: str = os.environ.get("AZURE_SEARCH_INDEX_NAME")

res = client.chat.completions(
    development_name=development_name,
)

response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response.choices[0].message.content)