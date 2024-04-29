import os

from groq import Groq

client = Groq(
    api_key=("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)




# pip install Groq
# pip install stramlit