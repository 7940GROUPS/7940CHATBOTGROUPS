from __future__ import unicode_literals

import os
import sys
import redis
import json
import requests

from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, VideoMessage, VideoSendMessage, FileMessage, StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, PostbackTemplateAction, CarouselTemplate, CarouselColumn, URITemplateAction
)
from linebot.utils import PY3

from string import Template


HOST ="redis-10410.c8.us-east-1-4.ec2.cloud.redislabs.com"
PWD = "SjFeUnDCknI8l7E8Zw4gdOZ8hwXiKEY7"
PORT = "10410"
redis1 = redis.Redis(host = HOST, password = PWD, port = PORT)


redis1.set("COVID-19 Introduction","COVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019. Until 12th Mar, there are totally 118325 confirmed case globally")
test=redis1.get("COVID-19 Introduction").decode('UTF-8')

redis1.set("Incubation Period","COVID-19 ranges from 1-14 days, most commonly around five days.")
test1=redis1.get("Incubation Period").decode('UTF-8')

redis1.lpush("COVID-19","COVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019. Until 12th Mar, there are totally 118325 confirmed case globally",
             "COVID-19 ranges from 1-14 days, most commonly around five days.",
             "https://i0.wp.com/www.newtelegraphng.com/wp-content/uploads/2020/01/Coronavirus.png?w=622&ssl=1",
             "https://cdn.the-scientist.com/assets/articleNo/67045/aImg/35755/coronavirus-incubation-l.jpg")
test11=redis1.lindex("COVID-19",3).decode('UTF-8')
test10=redis1.lindex("COVID-19",2).decode('UTF-8')
test2=redis1.lindex("COVID-19",1)
test3=redis1.lindex("COVID-19",0)


redis1.lpush("1","龍城大藥房","尖沙咀加連威老道28號","22.302755","114.185589")
test4=redis1.lindex("1",3).decode('UTF-8')
test5=redis1.lindex("1",2).decode('UTF-8')
test6=redis1.lindex("1",1)
test7=redis1.lindex("1",0)


redis1.lpush("2","華潤堂","銅鑼灣軒尼詩道488-490號軒尼詩大廈地下C鋪","22.28271","114.19439")
test32=redis1.lindex("2",3).decode('UTF-8')
test33=redis1.lindex("2",2).decode('UTF-8')
test34=redis1.lindex("2",1)
test35=redis1.lindex("2",0)


redis1.lpush("3","仁豐藥房","Shatin Plaza, L3/F, 41, 42A","22.3820646","114.1888745")
test36=redis1.lindex("3",3).decode('UTF-8')
test37=redis1.lindex("3",2).decode('UTF-8')
test38=redis1.lindex("3",1)
test39=redis1.lindex("3",0)


redis1.lpush("4","志成大藥房","Tsuen Wan, Ham Tin St, 46號地下 Shing On Building","22.3675929","114.112213")
test40=redis1.lindex("4",3).decode('UTF-8')
test41=redis1.lindex("4",2).decode('UTF-8')
test42=redis1.lindex("4",1)
test43=redis1.lindex("4",0)


redis1.lpush("5","龍豐药房","Yuen Long, 壽富街 19號 地下 龍 豐藥房","22.4445157","114.0232547")
test44=redis1.lindex("5",3).decode('UTF-8')
test45=redis1.lindex("5",2).decode('UTF-8')
test46=redis1.lindex("5",1)
test47=redis1.lindex("5",0)


redis1.lpush("symptoms","http://cloudvideo.thepaper.cn/sparker/f954b6f1c81d4c44a5e4d2a437a1fe2a/ld/9db4ba09-1427-4503-b1b3-6f68fc630ed8-659e9aa5-4ff1-1dd0-5f12-0df81cc3bf64.mp4",
             "https://cdn.images.express.co.uk/img/dynamic/151/590x/coronavirus-uk-face-mask-safety-development-world-first-covid-19-resistant-mask-1254044.jpg?r=1584025841438")
test8=redis1.lindex("symptoms",1)
test9=redis1.lindex("symptoms",0)

redis1.lpush("COVID News","發佈日期：2020-04-14","香港地區個案累計1013宗，新增3宗","點擊查看詳細報道","https://www.info.gov.hk/gia/general/202004/14/P2020041400583.htm",
                          "發佈日期：2020-04-13","香港地區個案累計1010宗，新增5宗","點擊查看詳細報道","https://www.info.gov.hk/gia/general/202004/13/P2020041300626.htm",
                          "發佈日期：2020-04-12","香港地區個案累計1005宗，新增4宗","點擊查看詳細報道","https://www.info.gov.hk/gia/general/202004/12/P2020041200558.htm",
                          "發佈日期：2020-04-11","香港地區個案累計1001宗，新增11宗","點擊查看詳細報道","https://www.info.gov.hk/gia/general/202004/11/P2020041100605.htm",
                          "發佈日期：2020-04-10","香港地區個案累計990宗，新增16宗","點擊查看詳細報道","https://www.info.gov.hk/gia/general/202004/10/P2020041000577.htm")
test12=redis1.lindex("COVID News",19).decode('UTF-8')
test13=redis1.lindex("COVID News",18).decode('UTF-8')
test14=redis1.lindex("COVID News",17).decode('UTF-8')
test15=redis1.lindex("COVID News",16)

test16=redis1.lindex("COVID News",15).decode('UTF-8')
test17=redis1.lindex("COVID News",14).decode('UTF-8')
test18=redis1.lindex("COVID News",13).decode('UTF-8')
test19=redis1.lindex("COVID News",12)

test20=redis1.lindex("COVID News",11).decode('UTF-8')
test21=redis1.lindex("COVID News",10).decode('UTF-8')
test22=redis1.lindex("COVID News",9).decode('UTF-8')
test23=redis1.lindex("COVID News",8)

test24=redis1.lindex("COVID News",7).decode('UTF-8')
test25=redis1.lindex("COVID News",6).decode('UTF-8')
test26=redis1.lindex("COVID News",5).decode('UTF-8')
test27=redis1.lindex("COVID News",4)

test28=redis1.lindex("COVID News",3).decode('UTF-8')
test29=redis1.lindex("COVID News",2).decode('UTF-8')
test30=redis1.lindex("COVID News",1).decode('UTF-8')
test31=redis1.lindex("COVID News",0)









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
    if(event.message.text=="COVID-19 Introduction"):
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(test)
    )

    elif(event.message.text=="Incubation Period"):
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
                        text= 'COVID-19 Introduction',
                        data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url= test3.decode(),
                        action=PostbackTemplateAction(
                        label='Incubation',
                        text= "Incubation Period",
                        data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)






    elif(event.message.text=="mask"):
        print(event.message.text)
        msg = 'Which district do you live? (Please type number)\n1.油尖旺區\n2.灣仔區\n3.沙田區\n4.荃灣區\n5.觀塘區' 
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(msg)
    )
    
    
    elif(event.message.text=="1"):
        message = LocationSendMessage(
            title= test4,
            address= test5,
            latitude= test6.decode(),
            longitude= test7.decode()
        )
        line_bot_api.reply_message(
        event.reply_token, 
        message)
    

    elif(event.message.text=="2"):
        message = LocationSendMessage(
            title= test32,
            address= test33,
            latitude= test34.decode(),
            longitude= test35.decode()
        )
        line_bot_api.reply_message(
        event.reply_token, 
        message)
    
        
        
    elif(event.message.text=="3"):
        message = LocationSendMessage(
            title= test36,
            address= test37,
            latitude= test38.decode(),
            longitude= test39.decode()
        )
        line_bot_api.reply_message(
        event.reply_token, 
        message)
    
    
    elif(event.message.text=="4"):
        message = LocationSendMessage(
            title= test40,
            address= test41,
            latitude= test42.decode(),
            longitude= test43.decode()
        )
        line_bot_api.reply_message(
        event.reply_token, 
        message)
    
    
    elif(event.message.text=="5"):
        message = LocationSendMessage(
            title= test44,
            address= test45,
            latitude= test46.decode(),
            longitude= test47.decode()
        )
        line_bot_api.reply_message(
        event.reply_token, 
        message)



    elif(event.message.text=="wash hands"):
        message = VideoSendMessage(
            original_content_url = 'https://firebasestorage.googleapis.com/v0/b/linechatbot-groups.appspot.com/o/linevideo%2Fmimi%202020-03-03%2017.25.15.mp4?alt=media&token=d001bac0-847b-455a-ad7e-2408ee86f79a',
            preview_image_url= 'https://firebasestorage.googleapis.com/v0/b/linechatbot-groups.appspot.com/o/linevideo%2FIMG_0869.PNG?alt=media&token=81a8b13c-3d16-4a26-ba11-8e4d0e2c5ad8'
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    

    elif(event.message.text=="COVID News"):
        message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title= test12,
                        text= test13,
                        actions=[
                            URITemplateAction(
                               label= test14,
                               uri= test15.decode()
                            )
                        ]
                    ),
                    CarouselColumn(
                        title= test16,
                        text= test17,
                        actions=[
                            URITemplateAction(
                               label= test18,
                               uri= test19.decode()
                            )
                        ]
                    ),
                    CarouselColumn(
                        title= test20,
                        text= test21,
                        actions=[
                            URITemplateAction(
                               label= test22,
                               uri= test23.decode()
                            )
                        ]
                    ),
                    CarouselColumn(
                        title= test24,
                        text= test25,
                        actions=[
                            URITemplateAction(
                               label= test26,
                               uri= test27.decode()
                            )
                        ]
                    ),
                    CarouselColumn(
                        title= test28,
                        text= test29,
                        actions=[
                            URITemplateAction(
                               label= test30,
                               uri= test31.decode()
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage('請輸入正確的關鍵字：\n1.如果您想查找新冠肺炎的相關介紹，請輸入：COVID-19\n2.如果您想查詢哪裡可以買口罩，請輸入：mask\n3.如果您想知道如何正確洗手，請輸入：wash hands\n4.如果您想了解最新的新冠肺炎發展趨勢，請輸入：COVID News')
        )
        
    
        

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
