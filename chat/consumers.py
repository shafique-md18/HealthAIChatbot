import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from . import tasks

from ai.healthAI import chatbot_response

class ChatConsumer(WebsocketConsumer):
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        response_message = chatbot_response(message)
        
        async_to_sync(self.channel_layer.send)(
                self.channel_name,
                {
                    'type': 'chat_message',
                    'message': response_message
                }
            )

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': f'{message}'
        }))
