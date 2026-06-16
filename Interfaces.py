from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IProductRepository(ABC):
    """Source Interface"""

    @abstractmethod
    def get_all_products(self) -> List[Dict[str, Any]]:
        """Returns a list of all products in the form of dictionaries"""
        pass
    @abstractmethod
    def get_all_main_tabs(self)-> List[Dict[str, Any]]:
        """Returns a list of all main Tabs in the form dictionaries"""
        pass
