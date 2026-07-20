import pyautogui
import pyperclip
import time
from openai import OpenAI



# Give yourself a few seconds to switch to the target window
time.sleep(3)

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY_HERE"
)

def is_last_message_from_user(chat_history, user_id, assistant_id):
    # Implement logic to determine if the last message is from the user
    # This is a placeholder and should be replaced with actual logic
    is_last_message_from_user
    

while True:

    # Click the icon
    pyautogui.click(1296, 1041)
    print("clciked icon")
    time.sleep(5)

    # Select text by dragging
    pyautogui.hotkey('ctrl', 'c') # Copy selected text
    time.sleep(0.5)
    pyautogui.moveTo(991, 303)
    pyautogui.dragTo(1516, 939, duration=1, button='left')

    time.sleep(0.5)

    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')

    time.sleep(0.5)

    # Get clipboard contents
    selected_text = pyperclip.paste()

    print("Copied text:")
    print(selected_text)

    # Now it's available in a variable
    text_variable = selected_text


    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )
    response =  print(chat_completion.choices[0].message.content)

    pyautogui.click(1296, 1041)  # Click the icon again to focus
    time.sleep(0.5)

    pyautogui.hold('ctrl','v')  # Paste the response
    time.sleep(0.5)

    pyautogui.press('enter')  # Press Enter to send the message
