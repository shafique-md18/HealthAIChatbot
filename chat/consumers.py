import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from . import tasks

from ai.healthAI import chatbot_response

class ChatConsumer(WebsocketConsumer):

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # get data from chatbot
        (response_message, code) = chatbot_response(message)
        status = 1
        if (code == None):
            code = 0 # default return code
        if (message == None):
            code = 0
            status = 0
            message = ""

        async_to_sync(self.channel_layer.send)(
                self.channel_name,
                {
                    'type': 'chat_message',
                    'status': status,
                    'code': code,
                    'message': response_message
                }
            )

    def chat_message(self, event):
        status = event['status']
        code = event['code']
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'status': status,
            'code': code,
            'message': f'{message}'
        }))
