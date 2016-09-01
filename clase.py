class Celular:
   Tamano=15
   Color=""
   Wifi=True
   Touch=False
   
    def _init_(self,Tamano,Color):
   		self.Tamano=Tamano
   		self.Color=Color
   
   def TipoColor(self):
   		print ("Verde")

Sony=Celular()
Sony.TipoColor()
Sony.Tamaño=20
print (Sony.Tamano)
