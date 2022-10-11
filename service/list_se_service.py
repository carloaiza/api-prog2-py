from model.kid import Kid
from model.list_se import ListSE

class ListSEService:
    def __init__(self):
        self.list= ListSE()
        #mosquera = Kid("123456","Jeronimo Mosquera",4,"M")
        mosquera = Kid({"identification":"123456","name":"Jeronimo Mosquera","age":4,"gender":"M"})
        self.list.add(mosquera)
        murillo = Kid({"identification":"654321","name":"Jeronimo Murillo","age":5,"gender":"M"})
        self.list.add(murillo)

    def add_kid(self,data):
        #Aca irian las validaciones del dict
        if "age" in data:
            if data['age'] > 0:
                self.list.add(Kid(data))
                return "Kid adicionado exitosamente"
            else:
                return "La edad debe ser positiva"
        else:
            return "Atributo age no encontrado"
