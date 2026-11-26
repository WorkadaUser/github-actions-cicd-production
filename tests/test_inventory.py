import pytest
from inventory_app.inventory import Inventory

@pytest.fixture
def inventory():
    return Inventory()


def test_add_product(inventory):
    inventory.add_product("LAPTOP",10,800)
    assert inventory.get_stock("LAPTOP") == 10
    
    
def test_add_existing_product(inventory):
    inventory.add_product("LAPTOP",5,800)
    inventory.add_product("LAPTOP",3,900)
    assert inventory.get_stock("LAPTOP") == 8
    

def test_remove_product(inventory):
    inventory.add_product("MOUSE",20, 25)
    inventory.remove_product("MOUSE",5)
    assert inventory.get_stock("MOUSE") == 15
    
    
def test_insufficient_stock(inventory):
    inventory.add_product("MOUSE", 3, 25)
    with pytest.raises(ValueError, match="Insufficient stock"):
        inventory.remove_product("MOUSE", 5)
        
def test_negative_quantity(inventory):
    with pytest.raises(ValueError):
        inventory.add_product("LAPTOP", -1, 800)
        
def test_negative_price(inventory):
    with pytest.raises(ValueError):
        inventory.add_product("LAPTOP", 1, -800)
        
def test_empty_sku(inventory):
    with pytest.raises(ValueError):
        inventory.add_product("", 1, 100)


def test_missing_product(inventory):
    with pytest.raises(KeyError):
        inventory.get_stock("UNKNOWN")
        

def test_invalid_removal_quantity(inventory):
    inventory.add_product("MOUSE", 5, 25)
    with pytest.raises(ValueError):
        inventory.remove_product("MOUSE", 0)
        
        
def test_total_inventory_value(inventory):
    inventory.add_product("LAPTOP", 2, 800)
    inventory.add_product("MOUSE", 4, 25)
    assert inventory.total_value() == 1700
    

def  test_empty_inventory_value(inventory):
    assert inventory.total_value() == 0
