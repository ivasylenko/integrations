
from centra_contracts import Item
from .inventories import InventoriesControl

from fastapi import FastAPI
app = FastAPI()


class IntegrationApp:

    def __init__(self, inventory_controller: InventoriesControl):
        self.inventory_controller = inventory_controller
        self.setup_routes()

    async def get_all(self):
        return self.inventory_controller.get_all()

    def setup_routes(self):
        """Set up the API routes for the integration."""
        app.add_api_route(
            "/items",
            self.get_all,
            response_model=Item,
            methods=["GET"]
        )
