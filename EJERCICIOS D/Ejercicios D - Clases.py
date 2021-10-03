x = "Bienvenido al menú de las clases"
print(x)

class Humano:
    cerebro = 1
    corazon = 1
    organos = True
    extremidades = True
    especie = "homo sapiens"
    organismo = "pluricelular"
    orden = "primate"
    clase = "mamalia"
    funciones = ["alimentacion", "respiracion", "circulacion", "excrecion", "reproduccion"]
    sentidos = ["vista", "tacto", "gusto", "olfato", "oido", "equilibrio"]

    def avanzar(self):
        print("El ser humano ha caminado hacía adelante")

    def comer(self):
        print("El ser humano esta ingeriendo alimento")

    def reir(self):
        print("El humano está riendo")

    def dormir(self):
        print("El ser humano se durmió")

class Animal:
    dominio = ["eukaryota", "opimoda", "podiata", "amorphea", "opisthokonta", "holozoa", "filozoa", "apokoizoa"]
    reino = "animalia"
    organismo = "pluricelular"
    funciones = ["alimentacion", "respiracion", "circulacion", "excrecion", "reproduccion"]
    organos = True
    extremidades = True

    def cazar(self):
        print("El animal está casando")

    def comer(self):
        print("El animal está comiendo")

    def dormir(self):
        print("El animal está durmiendo")

class Coche:
    motor = 1
    ruedas = 4
    transmision = ["manual", "automatica"]
    frenos = True
    puertas = True
    asientos = True
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
   

class Television:
    medio = "telecomunicacion"
    color = ["monocromatica", "multicolor"]
    transmision = ["analoga", "digital"]
    pantallas = 1
    combustible = "electrico"
    funcion = "reproduccion"
    puertos = True
    visuales = "imagenes"

    def prender(self):
        print("La T.V. está encendida")

    def aumentar_volumen(self):
        x = 0
        x = x + 1
        print("El volumen es de:", x)

    def disminuir_volumen(self):
        y = 0
        y = y - 1
        print("El volumen es de:", x)

    def apagar(self):
        print("La T.V. está apagada")

humano = Humano()
humano.avanzar()
humano.comer()
humano.reir()
humano.dormir()

animal = Animal()
animal.cazar()
animal.comer()
animal.dormir()

coche = Coche()
coche.encender()
coche.avanzar()
coche.retroceder()
coche.frenar()
coche.apagar()

television = Television()
television.prender()
television.aumentar_volumen()
television.disminuir_volumen()
television.apagar()