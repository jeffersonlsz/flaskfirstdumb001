
class Produto():
    def __init__(self, nome, partnumber, label, startinventory, 
                 receivedinventory=0, shippedinventory=0, inventoryonhand=0, minimumreq=0) -> None:
        
        self.nome = nome
        self.partnumber = partnumber
        self.label = label
        self.startinventory = startinventory
        self.receivedinventory = receivedinventory
        self.shippedinventory = shippedinventory
        self.inventoryonhand = inventoryonhand
        self.inventoryonhand = inventoryonhand
        self.minimumreq = minimumreq
        
    def get_nome(self):
        return self.nome
    
    def get_part_number(self):
        return self.partnumber
    
    def get_label(self):
        return self.label
    
    def get_start_inventory(self):
        return self.startinventory