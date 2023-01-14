class Film:
    def __init__(self, sor_lista):
        self.Cim = sor_lista[0]
        self.Rendezo = sor_lista[1]
        self.Foszereplo = sor_lista[2]
        self.ev = int(sor_lista[3])
        self.Perc = int(sor_lista[4])

    def __str__(self):
        return f"{self.Cim}, {self.Rendezo}, {self.Foszereplo}, {self.ev}, {self.Perc},"

