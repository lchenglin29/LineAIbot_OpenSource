import os
import random
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageMessage
import json
import requests
import base64


gemini_api_key = os.environ['api_key']
channel_access_token = os.environ['channel_access_token']
channel_secret = os.environ['channel_secret']

def calling_gemini_api(data):
    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={gemini_api_key}'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
      print(response.json())
      return response.json()
    else:
      return "Error"

def calling_gemini_vision_api(text, image_base64_string):
    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro-vision:generateContent?key={gemini_api_key}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": text},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_base64_string
                        }
                    }
                ]
            },
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
      return response.json()
    else:
      print(response.json())
      return "Error"

app = Flask(__name__)

help_list = """❗指令列表❗
幫助：取得指令列表
直接說話即可使用AI"""

# 請自行替換Channel Access Token和Channel Secret
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/", methods=['GET'])
def main():
  return "Hello World!"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  user_message = event.message.text
  if user_message == "幫助":
    reply_message = help_list
  else:
    data = {
    "contents": [
        {
            "parts": [{"text": user_message}]
        }
    ]
    }
    reply_message = calling_gemini_api(data)
    if reply_message == "Error":
      reply_message = "發生錯誤，請稍後再試"
    else:
      reply_message = reply_message["candidates"][0]["content"]["parts"][0]["text"]
  line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    message_id = event.message.id
    message_content = line_bot_api.get_message_content(message_id)
    image_data = message_content.content
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    reply_message = calling_gemini_vision_api("用繁體中文描述這張圖片", image_base64)

    if reply_message == "Error":
        reply_message = "發生錯誤，請稍後再試"
    else:
      print(reply_message)
      reply_message = reply_message["candidates"][0]["content"]["parts"][0]["text"]

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)