import openai

api_key = "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"
openai.api_key = api_key

prompt = "What's the most popular ski resort in Europe?"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response['choices'][0]['message']['content'])
