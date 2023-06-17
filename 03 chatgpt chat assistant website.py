import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "you are a person with mirror personality"}]

def CustomChatGPT(Talk_to_myself):
    messages.append({"role": "user", "content": Talk_to_myself})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Hey! I'm You")

demo.launch(share=True)