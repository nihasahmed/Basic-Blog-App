from channels.generic.websocket import AsyncJsonWebsocketConsumer


class Notification(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add("notification", self.channel_name)
        await self.accept()
        print("Added "+self.channel_name+" channel to gossip")


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notification", self.channel_name)



    async def liked_notification(self, event):
        if(self.scope['user'].id == event['author']):
            await self.send_json(event)
