from openai import OpenAI

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY_HERE"
)

completion = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named Jarvis. Skilled in general tasks like Alexa and Google."
        },
        {
            "role": "user",
            "content": "What is coding?"
        }
    ]
)

print(completion.choices[0].message.content)


