from openai import AzureOpenAI
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    # Get user message from the POST request
    user_message = request.json.get('message')

    development_name: str = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
    search_endpoint: str = os.environ.get("AZURE_SEARCH_RESOURCE_URI")
    search_index: str = os.environ.get("AZURE_SEARCH_INDEX_NAME")
    print(development_name)
    client = AzureOpenAI(
        api_key=os.environ.get("AZURE_OPENAI_APIKEY"),
        azure_endpoint=os.environ.get("AZURE_OPENAI_RESOURCE_URI"),
        api_version="2024-02-01"
    )

# res = client.chat.completions(
#     development_name=development_name,
# )

    response = client.chat.completions.create(
        model=development_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    print(response.choices[0].message.content)

    return {'message': response.choices[0].message.content}


if __name__ == '__main__':
    app.run(debug=True)
