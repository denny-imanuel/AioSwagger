import json

from Model.Item import Item
from aiohttp import web


class ItemController:

    def __init__(self):
        self.itemList = []
        self.itemList.append(Item("Air", 10))
        self.itemList.append(Item("Brush", 20))
        self.itemList.append(Item("Candy", 30))

    async def get_item(self, request):
        """
        ---
        tags:
        - Get Item
        parameters:
        - in: query
          name: idx
        """
        idx = int(request.rel_url.query["idx"])
        item = self.itemList[idx]
        str = json.dumps(item.__dict__)
        return web.json_response(str)

    async def put_item(self, request):
        """
        ---
        tags:
        - Put Item
        parameters:
        - in: query
          name: idx
        - in: body
          name: item
        """
        idx = int(request.rel_url.query["idx"])
        if idx < len(self.itemList):
            body = request.json()
            obj = json.loads(body)
            item = Item(**obj)
            self.itemList[idx] = item
            return web.Response(text=str(True))
        else:
            return web.Response(text=str(False))

    async def post_item(self, request):
        """
        ---
        tags:
        - Post Item
        parameters:
        - in: body
          name: item
        """
        body = request.json()
        obj = json.loads(body)
        item = Item(**obj)
        self.itemList.append(item)
        return web.Response(text=str(True))

    async def delete_item(self, request):
        """
        ---
        tags:
        - Delete Item
        parameters:
        - in: query
          name: idx
        """
        idx = int(request.rel_url.query["idx"])
        if idx < len(self.itemList):
            del self.itemList[idx]
            return web.Response(text=str(True))
        else:
            return web.Response(text=str(False))
