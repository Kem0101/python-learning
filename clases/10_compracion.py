class Coordenadas():
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

    def __eq__(self, __value: object) -> bool:
        return self.lat == __value.lat and self.lon == __value.lon

    def __lt__(self, __value: object) -> bool:
        return self.lat + self.lon < __value.lat + __value.lon

    def __le__(self, __value: object) -> bool:
        return self.lat + self.lon <= __value.lat + __value.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

# con este tipo de comparación de dos objectos lo que compara python es si son exactamente el mismo objeto en el mismo especio de memoria
print(coords >= coords2)
