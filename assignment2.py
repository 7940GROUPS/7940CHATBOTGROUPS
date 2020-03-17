from __future__ import unicode_literals

import os
import sys
import redis
import json

from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, VideoMessage, VideoSendMessage, FileMessage, StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, PostbackTemplateAction
)
from linebot.utils import PY3

from string import Template

HOST ="redis-11707.c73.us-east-1-2.ec2.cloud.redislabs.com"
PWD = "fzUPMVnd6cvDmBYjPuioH2FHP8n5oGvR"
PORT = "11707"
redis1 = redis.Redis(host = HOST, password = PWD, port = PORT)


redis1.set("COVID","COVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019. Until 12th Mar, there are totally 118325 confirmed case globally")
test=redis1.get("COVID").decode('UTF-8')

redis1.set("incubation period","COVID-19 ranges from 1-14 days, most commonly around five days.")
test1=redis1.get("incubation period").decode('UTF-8')

redis1.lpush("COVID-19","COVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019. Until 12th Mar, there are totally 118325 confirmed case globally","COVID-19 ranges from 1-14 days, most commonly around five days.","https://i0.wp.com/www.newtelegraphng.com/wp-content/uploads/2020/01/Coronavirus.png?w=622&ssl=1","https://cdn.the-scientist.com/assets/articleNo/67045/aImg/35755/coronavirus-incubation-l.jpg")
test11=redis1.lindex("COVID-19",3).decode('UTF-8')
test10=redis1.lindex("COVID-19",2).decode('UTF-8')
test2=redis1.lindex("COVID-19",1)
test3=redis1.lindex("COVID-19",0)


redis1.lpush("mask","龍城大藥房","香港特別行政區油尖旺區尖沙咀加連威老道28號","22.302755","114.185589")
test4=redis1.lindex("mask",3).decode('UTF-8')
test5=redis1.lindex("mask",2).decode('UTF-8')
test6=redis1.lindex("mask",1)
test7=redis1.lindex("mask",0)

redis1.lpush("symptoms","https://www.youtube.com/watch?v=fg3SArRmYOI","https://cdn.images.express.co.uk/img/dynamic/151/590x/coronavirus-uk-face-mask-safety-development-world-first-covid-19-resistant-mask-1254044.jpg?r=1584025841438")
test8=redis1.lindex("symptoms",1)
test9=redis1.lindex("symptoms",0)




app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

# obtain the port that heroku assigned to this app.
heroku_port = os.getenv('PORT', None)

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if isinstance(event.message, TextMessage):
            handle_TextMessage(event)
        if isinstance(event.message, ImageMessage):
            handle_ImageMessage(event)
        if isinstance(event.message, VideoMessage):
            handle_VideoMessage(event)
        if isinstance(event.message, FileMessage):
            handle_FileMessage(event)
        if isinstance(event.message, StickerMessage):
            handle_StickerMessage(event)
        if isinstance(event.message, LocationMessage):
            handle_LocationMessage(event)
        

        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

    return 'OK'

# Handler function for Text Message
def handle_TextMessage(event):
    print(event.message.text)
    if(event.message.text=="COVID"):
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(test)
    )

    elif(event.message.text=="incubation period"):
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(test1)
    )

    elif(event.message.text=="COVID-19"):
        message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url= test2.decode(),
                        action=PostbackTemplateAction(
                        label='Introduction',
                        text= test11,
                        data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url= test3.decode(),
                        action=PostbackTemplateAction(
                        label='Incubation',
                        text= test10,
                        data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)



    elif(event.message.text=="mask"):
        message = LocationSendMessage(
            title= test4,
            address= test5,
            latitude= test6.decode(),
            longitude= test7.decode()
        )
        line_bot_api.reply_message(
        event.reply_token, 
        message)



    elif(event.message.text=="symptoms"):
        message = VideoSendMessage(
            original_content_url= test8.decode(),
            preview_image_url= test9.decode()
        )
        line_bot_api.reply_message(event.reply_token, message)

    
        

# Handler function for Sticker Message
def handle_StickerMessage(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )

# Handler function for Image Message
def handle_ImageMessage(event):
    line_bot_api.reply_message(
	event.reply_token,
	TextSendMessage(text="Nice image!")
    )

# Handler function for Video Message
def handle_VideoMessage(event):
    line_bot_api.reply_message(
	event.reply_token,
	TextSendMessage(text="Nice video!")
    )

# Handler function for File Message
def handle_FileMessage(event):
    line_bot_api.reply_message(
	event.reply_token,
	TextSendMessage(text="Nice file!")
    )

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host='0.0.0.0', debug=options.debug, port=heroku_port)
