print("Bun venit la calculator gravitatei obiectelor pe planete.")
print("Acestea sunt planetele:")
planets_list = ['Mercur', 'Venus', 'Pamanat', 'Marte', 'Jupiter', 'Saturn', 'Uranus', 'Neptun']
print("Numar de planete: " + str(len(planets_list)))
print(planets_list)

class Pamant:
  def __init__(self, gravity):
     self.nume = "Pamant"
     self.gravity = 1.0
earth = Pamant(1)

class Mercur:
    def __init__(self, gravity):
        self.nume = "Mercur"
        self.gravity = 0.38
mercury = Mercur(0.38)

class Venus:
    def __init__(self, gravity):
        self.nume = "Venus"
        self.gravity = 0.9
venus = Venus(0.9)

class Marte:
    def __init__(self, gravity):
        self.nume = "Marte"
        self.gravity = 0.815
marte = Marte(0.815)

class Jupiter:
    def __init__(self, gravity):
        self.nume = "Jupiter"
        self.gravity = 2.65
jupiter = Jupiter(2.65)

class Saturn:
    def __init__(self, gravity):
        self.nume = "Saturn"
        self.gravity = 1.17
saturn = Saturn(1.17)

class Uranus:
    def __init__(self, gravity):
        self.nume = "Uranus"
        self.gravity = 1.27
uranus = Uranus(1.27)

class Neptun:
    def __init__(self, gravity):
        self.nume = "Neptun"
        self.gravity = 1.64
neptun = Neptun(1.64)

_greutatea_obiectului = input("Introduceti greutatea obiectului: ")
print("Introduceti numele planetei: ")
_nume_planeta = input()
if _nume_planeta == "Pamant":
     print("Greutatea obiectului pe planeta " + _nume_planeta + " este " + str(float(_greutatea_obiectului) * earth.gravity) + " kg.")
elif _nume_planeta == "Mercur":
     print("Greutatea obiectului pe planeta " + _nume_planeta + " este " + str(float(_greutatea_obiectului) * mercury.gravity) + " kg.")
elif _nume_planeta == "Venus":
     print("Greutatea obiectului pe planeta " + _nume_planeta + " este " + str(float(_greutatea_obiectului) * venus.gravity) + " kg.")
elif _nume_planeta == "Marte":
     print("Greutatea obiectului pe planeta " + _nume_planeta + " este " + str(float(_greutatea_obiectului) * marte.gravity) + " kg.")
elif _nume_planeta == "Jupiter":
     print("Greutatea obiectului pe planeta " + _nume_planeta + " este " + str(float(_greutatea_obiectului) * jupiter.gravity) + " kg.")
elif _nume_planeta == "Saturn":
     print("Greutatea obiectului pe planeta " + _nume_planeta + " este " + str(float(_greutatea_obiectului) * saturn.gravity) + " kg.")
elif _nume_planeta == "Uranus":
     print("Greutatea obiectului pe planeta " + _nume_planeta + " este " + str(float(_greutatea_obiectului) * uranus.gravity) + " kg.")
elif _nume_planeta == "Neptun":
     print("Greutatea obiectului pe planeta " + _nume_planeta + " este " + str(float(_greutatea_obiectului) * neptun.gravity) + " kg.")
