class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.rutas = []
        self.horarios = []

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    def agregar_horario(self, horario):
        self.horarios.append(horario)


class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []

    def agregar_horario(self, horario):
        self.horarios.append(horario)

    def esta_disponible(self, horario):
        return horario not in self.horarios


class administración:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self):
        placa = input("Ingrese la placa del bus: ")
        bus = Bus(placa)
        self.buses.append(bus)
        print(f"Bus con placa {placa} agregado.")

    def agregar_ruta_a_bus(self):
        placa = input("Ingrese la placa del bus: ")
        bus = next((b for b in self.buses if b.placa == placa), None)
        if bus:
            ruta = input("Ingrese la ruta del bus: ")
            bus.agregar_ruta(ruta)
            print(f"Ruta {ruta} agregada al bus {placa}.")
        else:
            print("Bus no encontrado.")

    def registrar_horario_a_bus(self):
        placa = input("Ingrese la placa del bus: ")
        bus = next((b for b in self.buses if b.placa == placa), None)
        if bus:
            horario = input("Ingrese el horario del bus (solo hora): ")
            bus.agregar_horario(horario)
            print(f"Horario {horario} registrado para el bus {placa}.")
        else:
            print("Bus no encontrado.")

    def agregar_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado.")

    def agregar_horario_a_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        conductor = next((c for c in self.conductores if c.nombre == nombre), None)
        if conductor:
            horario = input("Ingrese el horario (solo hora): ")
            if conductor.esta_disponible(horario):
                conductor.agregar_horario(horario)
                print(f"Horario {horario} asignado al conductor {nombre}.")
            else:
                print(f"El conductor {nombre} ya tiene turno en ese horario.")
        else:
            print("Conductor no encontrado.")

    def asignar_bus_a_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        conductor = next((c for c in self.conductores if c.nombre == nombre), None)
        if conductor:
            placa = input("Ingrese la placa del bus: ")
            bus = next((b for b in self.buses if b.placa == placa), None)
            if bus:
                horario = input("Ingrese el horario para asignar al conductor: ")
                if conductor.esta_disponible(horario):
                    conductor.agregar_horario(horario)
                    bus.agregar_horario(horario)
                    print(f"Bus {placa} asignado al conductor {nombre} en el horario {horario}.")
                else:
                    print(f"El conductor {nombre} ya está ocupado en ese horario.")
            else:
                print("Bus no encontrado.")
        else:
            print("Conductor no encontrado.")

    def mostrar_menu(self):
        while True:
            print("\n1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_bus()
            elif opcion == "2":
                self.agregar_ruta_a_bus()
            elif opcion == "3":
                self.registrar_horario_a_bus()
            elif opcion == "4":
                self.agregar_conductor()
            elif opcion == "5":
                self.agregar_horario_a_conductor()
            elif opcion == "6":
                self.asignar_bus_a_conductor()
            elif opcion == "7":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")


# Ejecutar el sistema
sistema = administración()
sistema.mostrar_menu()