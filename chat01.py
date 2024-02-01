import openai

OPENAI_API_KEY='8c91c5c7058847f3820f9d7c12bbb1fb' 
OPENAI_AZURE_ENDPOINT='https://sktfly-ai.openai.azure.com/'
OPENAI_API_TYPE='azure'
OPENAI_API_VERSION='2023-05-15'
openai.api_key=OPENAI_API_KEY
openai.azure_endpoint=OPENAI_AZURE_ENDPOINT
openai.api_type=OPENAI_API_TYPE
openai.api_version=OPENAI_API_VERSION

query='you have to suicide'

result=openai.chat.completions.create(
    model='dev-gpt-35-turbo',
        messages = [
            {'role':'system', 'content':'You are a helpful assistant.'},
            {'role':'user', 'content':query}
        ]
    )

print(result.choices[0].message)

