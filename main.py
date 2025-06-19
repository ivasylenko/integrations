

from centra_integrations import AppController, IntegrationApp
from centra_integrations.models import Item


class IntegrationController(AppController):

    def get_inventory_bla(self) -> Item:
        print('we going to call super API and come back to you')
        return Item(
            name="IntA",
            description="An item of type IntA",
            price=10.0,
            in_stock=True
        )

IntegrationApp().set_controller(IntegrationController()).setup_routes().run()
