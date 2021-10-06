# Creamos nuestras clases con sus diferentes propiedades

class Autos():
    motor = 1
    ruedas = 4
    transmision = ["manual", "automatica"]
    frenos = 1
    puertas = True
    asientos = True
    ventanas = True
    neumaticos = 4
    cajuela = 1
    conductor = 1
    radio = 1
    antena = 1
    color = "rojo"
    material = "titanio"
    combustible = ["electrico", "gas", "biocombustible", "hibrido"]

    def encender(self):
        print("El coche está encendiendo")

    def avanzar(self):
        print("El coche está avanzando")

    def retroceder(self):
        print("El coche está retrocediendo")     

    def frenar(self):
        print("El coche se está deteniendo")

    def apagar(self):
        print("El coche se está apagando")

    def __init__(self, color, radio):
        self.color = color
        self.radio = radio

class Felinos():
    reino = "animalia"
    familia = "felidade"
    orden = "carnivorae"
    bigotes = True
    garras = True
    nocturnos = True
    carnivoros = True
    organismo = "pluricelular"
    pelaje = ["lineas", "manchas", "camuflajeado", "plano"]
    color = ["gris", "blanco", "naranja", "café", "negro", "multicolor"]
    tamaño = ["grande", "mediano", "pequeño"]

    def cazar(self):
        print("El animal está casando")

    def comer(self):
        print("El animal está comiendo")

    def dormir(self):
        print("El animal está durmiendo")

    def __init__(self, reino, familia):
        self.reino = reino
        self.familia = familia

class Celulares(): 
    portatil = True
    medio_de_comunicacion = True
    bateria = 1
    tarjeta_sim = 1
    pantallas = 1
    tarjeta_madre = 1
    duracion_bateria = 9
    gpu = 1
    internet = True
    material = "aluminio"
    color = "negro"
    tipo = "herramienta"
    senal = ["3G", "4G", "5G"]

    def prender(self):
        print("El celular esta prendido")

    def actualizar(self):
        print("El celular se esta actualizando")

    def jugar(self):
        print("El celular se esta usando para jugar")
    
    def apagar(self):
        print("El celular se esta apagando")

    def __init__(self, material, tipo):
        self.material = material
        self.tipo = tipo

class Barcos():
    transporte = "navío"
    navegacion = "maritimo"
    chimenea = 1
    popa = 1
    helice = 1
    obra = 1
    ancla = 1
    bulbo = 1
    proa = 1
    cubierta = 1
    estructura = 1
    material = "acero"
    color = "blanco"
    tamano = ["barcos mayores", "barcos menores"]
    propulsion = ["humana", "eolica", "motorizada"]

    def avanzar(self):
        print("El barco está avanzando")

    def flotar(self):
        print("El barco esta flotando")

    def anclar(self):
        print("El barco se esta anclando")

    def explotar(self):
        print("El barco esta explotando")

    def __init__(self, chimenea, popa):
        self.chimenea = chimenea
        self.popa = popa

class Bebidas():
    base = "liquida"
    ingesta = "ingerición"
    compuesto = "agua"
    controlador = "hypotalamo"
    quimica = "h2o"
    tipos = ["pura", "alcoholica", "saborizada", "carbonizada", "lacteos", "vegetal", "jugos", "infusiones"]
    funcionalidad = ["vital", "cultural", "entretenimiento", "gusto"]
    sentido = "gusto"
    consumo = "boca"
    color = "variado"
    material = "hidrogeno"

    def servir(self):
        print("La bebida se esta sirviendo")

    def batir(self):
        print("La bebida se esta batiendo")

    def tomar(self):
        print("La bebida esta siendo tomada")

    def __init__(self, base, compuesto):
        self.base = base
        self.compuesto = compuesto

# Creamos varios objetos para nuestras clases

ferrari = Autos
lamborghini = Autos
toyota = Autos
Nissan = Autos

tigre = Felinos
gato = Felinos
pantera = Felinos
cheeta = Felinos

note = Celulares
iphone = Celulares
pixel = Celulares
poco = Celulares

kayak = Barcos
ferry = Barcos
yate = Barcos
buque = Barcos

cerveza = Bebidas
limonada = Bebidas
téverde = Bebidas
cappuccino = Bebidas

# Hacemos que todos nuestros objetos realicen un metodo o una accion

ferrari.encender(Autos)
ferrari.avanzar(Autos)
ferrari.retroceder(Autos)
ferrari.frenar(Autos)
ferrari.apagar(Autos)

lamborghini.encender(Autos)
lamborghini.avanzar(Autos)
lamborghini.retroceder(Autos)
lamborghini.frenar(Autos)
lamborghini.apagar(Autos)

toyota.encender(Autos)
toyota.avanzar(Autos)
toyota.retroceder(Autos)
toyota.frenar(Autos)
toyota.apagar(Autos)

Nissan.encender(Autos)
Nissan.avanzar(Autos)
Nissan.retroceder(Autos)
Nissan.frenar(Autos)
Nissan.apagar(Autos)

tigre.cazar(Felinos)
tigre.comer(Felinos)
tigre.dormir(Felinos)

gato.cazar(Felinos)
gato.comer(Felinos)
gato.dormir(Felinos)

pantera.cazar(Felinos)
pantera.comer(Felinos)
pantera.dormir(Felinos)

cheeta.cazar(Felinos)
cheeta.comer(Felinos)
cheeta.dormir(Felinos)

note.prender(Celulares)
note.jugar(Celulares)
note.actualizar(Celulares)
note.apagar(Celulares)

iphone.prender(Celulares)
iphone.jugar(Celulares)
iphone.actualizar(Celulares)
iphone.apagar(Celulares)

poco.prender(Celulares)
poco.jugar(Celulares)
poco.actualizar(Celulares)
poco.apagar(Celulares)

pixel.prender(Celulares)
pixel.jugar(Celulares)
pixel.actualizar(Celulares)
pixel.apagar(Celulares)

kayak.avanzar(Barcos)
kayak.flotar(Barcos)
kayak.anclar(Barcos)
kayak.explotar(Barcos)

ferry.avanzar(Barcos)
ferry.flotar(Barcos)
ferry.anclar(Barcos)
ferry.explotar(Barcos)

yate.avanzar(Barcos)
yate.flotar(Barcos)
yate.anclar(Barcos)
yate.explotar(Barcos)

buque.avanzar(Barcos)
buque.flotar(Barcos)
buque.anclar(Barcos)
buque.explotar(Barcos)

cerveza.servir(Bebidas)
cerveza.batir(Bebidas)
cerveza.tomar(Bebidas)

limonada.servir(Bebidas)
limonada.batir(Bebidas)
limonada.tomar(Bebidas)

téverde.servir(Bebidas)
téverde.batir(Bebidas)
téverde.tomar(Bebidas)

cappuccino.servir(Bebidas)
cappuccino.batir(Bebidas)
cappuccino.tomar(Bebidas)

# Inicializacion de un auto

a1 = Autos("rojo", 1)
print(a1.color)
print(a1.radio)

# Inicializacion de un felino

f1 = Felinos("animalia", "felidae")
print(f1.reino)
print(f1.familia)

# Inicializacion de un celular

c1 = Celulares("aluminio", "herramienta")
print(c1.material)
print(c1.tipo)

# Inicializacion de un barco

b1 = Barcos(1,1)
print(b1.chimenea)
print(b1.popa)

# Inicializacion de una bebida

be1 = Bebidas("liquida", "agua")
print(be1.base)
print(be1.compuesto)