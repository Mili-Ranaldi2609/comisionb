class Motocicleta:
    #atributo de clase
    is_new=True
    def __init__(self,color="",tuition="",brand="",model="",fabrication_date=int,top_speed=int,weight=int):
        #atributos de instancia
        self.color=color
        self.tuition=tuition
        #ATRIBUTOS PRIVADOS
        self.__fuel_filters=10
        self.__numbers_wheels=2
        #######################
        self.model=model
        self.fabrication_date=fabrication_date
        self.top_speed=top_speed
        self.weight=weight
        self.brand=brand
    def get_information(self):
        state = "nueva" if self.is_new else "usada"
        c=self.color
        t=self.tuition
        b=self.brand
        m=self.model
        fd=self.fabrication_date
        ts=self.top_speed
        w=self.weight
        ff=self.__fuel_filters
        nw=self.__numbers_wheels
        print(f"Motocicleta //estado={state}, color={c}, modelo={m}, matricula={t}")
        print(f"marca={b}, año de fabricacion={fd}, velocidad maxima={ts}, peso={w} ")
        print(f"filtros de combustible={ff}, numero de ruedas={nw}")

    #atributo de clase 
    engine=False
    def stopped_or_running(self):
        sor="en marcha" if self.engine else "detenido"
        return print(f"Esta {sor}")
    #Metodos inteligentes
    def start_up(self):
        
        if not self.engine:
            self.engine = True
            print("El motor ha arrancado.")
        else:
            print("El motor ya estaba en marcha.")
        
    def arrest(self):
        if self.engine:
            self.engine=False
            print("El motor se ha detenido.")
        else:
            print("El motor ya estaba detenido.")
    def get_price(self, precio):
        self.precio = precio



