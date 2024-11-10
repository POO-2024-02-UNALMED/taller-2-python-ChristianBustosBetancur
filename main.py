class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados= cantidadCreados


    def cantidadAsientos(self):
        cantAsientos = 0
        for asiento in self.asientos:
            if type(asiento) == Asiento:
                cantAsientos += 1
        return cantAsientos


    def verificarIntegridad(self):
        original = True
        if self.motor.registro != self.registro:
            print("Las piezas no son originales")
            original = False

        for asiento in self.asientos:
            if asiento.registro != self.registro:
                print("Las piezas no son originales")
                original = False
        if original == True:
            print("Las piezas son originales")

class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,colorCambiar):
        lstColoresAdm = ["rojo","verde","amarillo","negro","blanco"]
        if colorCambiar in lstColoresAdm:
            self.color = colorCambiar
            return self.color
        return self.color

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,numRegistroCambiar):
        self.registro = numRegistroCambiar

    
    def asignarTipo(self,tipoMotorCambiar):
        tipoMotores = ["electrico","gasolina"]
        if tipoMotorCambiar in tipoMotores:
            self.tipo = tipoMotorCambiar
        return self.tipo