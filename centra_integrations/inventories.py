
from centra_contracts import Item
from abc import ABC, abstractmethod


class InventoriesControl(ABC):

    @abstractmethod
    def get_all(self) -> Item:
        """This method should be implemented by the subclass to return an Item."""
        raise NotImplementedError("This method should be implemented by the subclass.")
