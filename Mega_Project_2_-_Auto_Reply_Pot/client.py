from openai import OpenAI

#pip install openai
# if you saved the key under a different environment varisble name, you can do something like this
client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY_HERE"
)

command = '''
Mashalah ab dekho PS D:\python_cwh_17_5_26\Mega_Project_2_-_Auto_Reply_Pot> & d:/python_cwh_17_5_26/Mega_Project_2_-_Auto_Reply_Pot/.venv/Scripts/python.exe d:/python_cwh_17_5_26/Mega_Project_2_-_Auto_Reply_Pot/program.py
clciked icon
Traceback (most recent call last):
  File "d:\python_cwh_17_5_26\Mega_Project_2_-_Auto_Reply_Pot\program.py", line 11, in <module>
    time.sleep(5)
KeyboardInterrupt
PS D:\python_cwh_17_5_26\Mega_Project_2_-_Auto_Reply_Pot> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& d:\python_cwh_17_5_26\Mega_Project_2_-_Auto_Reply_Pot\.venv\Scripts\Activate.ps1)
(.venv) PS D:\python_cwh_17_5_26\Mega_Project_2_-_Auto_Reply_Pot> & d:/python_cwh_17_5_26/Mega_Project_2_-_Auto_Reply_Pot/.venv/Scripts/python.exe d:/python_cwh_17_5_26/Mega_Project_2_-_Auto_Reply_Pot/program.py
clciked icon
Copied text:
lagao.

Phir run karo:

python program.py

Ya jo command tum use kar rahe ho usse run karo.

Phir mujhe batao:

"Clicked icon" print hone ke baad 5 second ke andar kaunsi window saamne aati hai?

WhatsApp?
ChatGPT?
Chrome?
VS Code?

Wahi asli clue hai. 🔍
(.venv) PS D:\python_cwh_17_5_26\Mega_Project_2_-_Auto_Reply_Pot> 
'''

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
print(chat_completion.choices[0].message.content)
