from aiohttp import web
from aiohttp_swagger import *
from Controller.ItemController import ItemController


app = web.Application()

controller = ItemController()
app.router.add_route("GET", "/get_item", controller.get_item)
app.router.add_route("PUT", "/put_item", controller.put_item)
app.router.add_route("POST", "/post_item", controller.post_item)
app.router.add_route("DELETE", "/delete_item", controller.delete_item)

setup_swagger(app, swagger_url="swagger", title="Aio API", api_version="1.0.0", ui_version=2)
web.run_app(app, host="localhost")
