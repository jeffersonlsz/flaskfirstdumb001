import mysql.connector
from model.produto import Produto


class Database():
    

    def __init__(self) -> None:
        # Replace these values with your own database details
        self.host = "localhost"
        self.user = "root"
        self.password = "root"
        self.database = "warehouse"

        # Establish the connection
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            
            if self.connection.is_connected():
                print("Connected to MySQL database")
            
            # You can add your database operations here
            
        except mysql.connector.Error as e:
            print("Error:", e)


    def getconnection(self):
        return self.connection
    
    def getconnectioncursor(self):
        return self.connection.cursor()
    
    def listarProdutos(self):
            cursor = self.getconnection().cursor()
            query = "SELECT * FROM products"
            cursor.execute(query)
            products = cursor.fetchall()
            cursor.close()
            self.connection.close()
            return products
    
    def get_produto_por_id(self, produtoid):
         cursor = self.getconnection().cursor()
         query = "SELECT * FROM products where id="+str(produtoid)
         cursor.execute(query)
         product = cursor.fetchall()
         cursor.close()
         self.connection.close()
         print(product)

         retorno = Produto(product[0][1], product[0][2], product[0][3], product[0][4], product[0][5], product[0][6], product[0][7], product[0][8])
         print("%s %s %s %s %s %s %s %s"%((product[0][1], product[0][2], product[0][3], product[0][4], product[0][5], product[0][6], product[0][7], product[0][8])))
         return retorno

    def cadastrarProduto(self, produto):
         print(produto)
         cursor = self.getconnection().cursor()
         query = f'''INSERT INTO `products` (`ProductName`, `PartNumber`, `ProductLabel`,
                   `StartingInventory`, `InventoryReceived`, `InventoryShipped`, `InventoryOnHand`, `MinimumRequired`) VALUES
                    ('%s', '%s', '%s', %s, '%s', '%s','%s', '%s')'''%(produto.nome, produto.partnumber ,produto.label, produto.startinventory,
                                           produto.receivedinventory, produto.shippedinventory, produto.inventoryonhand, produto.minimumreq
                                           )
         
         
         #        receivedinventory=0, shippedinventory=0, inventoryonhand=0, minimumreq=0
         cursor.execute(query)
         self.getconnection().commit()
         cursor.close()
         self.getconnection().close()
         #print(query)

    def atualizarProduto(self, id, produtonnome, partnumber, labelprod, nstartinventory, produto):
        cursor = self.connection.cursor()
        print(produtonnome)
        print(partnumber)
        print(labelprod)
        print(nstartinventory)
        query = f''' UPDATE `products`
                                    SET 
                                        `ProductName` = '%s',
                                        `PartNumber` = '%s',
                                        `ProductLabel` = '%s',
                                        `StartingInventory` = %s
                                    WHERE `id` = %s;'''%(produtonnome, partnumber, labelprod, nstartinventory, id)

        print(query)
        cursor.execute(query)
        self.getconnection().commit()
        cursor.close()
        self.getconnection().close()


    def excluir_produto(self, _id):
        cursor = self.connection.cursor()
        query = f'''DELETE from `products` WHERE `id` = %s'''%(_id)
        cursor.execute(query)
        self.getconnection().commit()
        cursor.close()
        self.getconnection().close()