from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
) 
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('x/8+yr3afBpF/0Sp1LBOe5JkX6e87wlwOfmShKyyxdcw1kKV233dqrAXz7g3MYW3WorJCLuZHLjPdKBmBZDgW+KA/VOVm8MFNvXtzxFMwndmljEb2i14F951qiZf/NuJZJ1gCoJNwxF2pBXC3lg47QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f526a4253059dfd52ad71bac2739a190')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = '宣宣最可蒂萌寶愛'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()