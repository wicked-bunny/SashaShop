from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IProductRepository(ABC):

    @abstractmethod

    def get_all_products(self) -> List[Dict[str, Any]]:
        """Returns a list of all products in the form of dictionaries"""
        pass
