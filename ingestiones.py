import json




class Ingestiones():    
    def __init__(self):
        self.ruta_static="C:/Repositorios/yenny_gordillo/src/pad_2025/static/"
        
        
    def leer_json(self):
        # r leer . w escribir

        ruta_json="{}json/datos_personas.json".format(self.ruta_static)
        datos=""
        with open(ruta_json="r",encoding="utf-8")as f:
            datos=json.load(f)
        return datos


inges = Ingestiones()
datos_json = inges.leer_json()
print(datos_json)
