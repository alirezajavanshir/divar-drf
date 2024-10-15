import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import *
from .models import ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.listing_id = self.scope["url_route"]["kwargs"]["listing_id"]
        self.room_group_name = f"chat_{self.listing_id}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope["user"]

        # Save message to database
        await sync_to_async(ChatMessage.objects.create)(
            listing_id=self.listing_id, user=user, message=message
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": user.username,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "user": user,
                }
            )
        )
