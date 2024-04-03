from openai import AzureOpenAI
from typing import List
from models.data import Data
import os



development_name:str = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
search_endpoint: str = os.environ.get("AZURE_SEARCH_RESOURCE_URI")
search_index: str = os.environ.get("AZURE_SEARCH_INDEX_NAME")
print(development_name)
client = AzureOpenAI(
    api_key=os.environ.get("AZURE_OPENAI_APIKEY"),
    azure_endpoint= os.environ.get("AZURE_OPENAI_RESOURCE_URI"),
    api_version="2024-02-01"
)

data = Data()
# res = client.chat.completions(
#     development_name=development_name,
# )
prompt: str = "Does the number of individual tax filings per municipality in Puerto Rico, h?"

response = client.chat.completions.create(
    model=development_name,
    temperature=0.3,
    messages=[
        {"role": "system", "content": f"You are an expert urban planner, specializing in walkable cities and green infrastructure. \
                You are able to provide advice on how to make cities more walkable and sustainable, while aiming to develop the economy as well as the demographics of the municipality.\
                This is the annual estimate of Puerto Rico population by municipalty: {data.population_by_municipality}\
                This is the annual estimate of Puerto Rico income tax filings by municipalty: {data.income_tax_filings_by_municipality}"},
        # {"role": "user", "content": ""},
        # {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": prompt},
    ],
    max_tokens=500,
)

print(response.choices[0].message.content)