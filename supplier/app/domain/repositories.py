from abc import abstractmethod


class SupplierRepository:
    @abstractmethod
    def save(self):
        pass
