

from centra_integrations.inventories import InventoriesControl
from centra_integrations.app import IntegrationApp, app
from centra_contracts import Item


class IntAInventory(InventoriesControl):

    def get_all(self) -> Item:
        print('we going to call super API and come back to you')
        return Item(
            name="IntA",
            description="An item of type IntA",
            price=10.0,
            in_stock=True
        )

IntegrationApp(IntAInventory())
