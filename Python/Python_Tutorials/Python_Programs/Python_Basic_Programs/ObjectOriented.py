class Superheros :
     def __init__(self, name, color, power):
         self.name = name;
         self.costume_color = color;
         self.power = power

     #def __init__(self, **kwargs):
      #def __init__(self, name = "hulk", color ='Green', power = "Strength"):

hulk = Superheros("Hulk", "Green" , "Strength")
print(hulk.costume_color);
print(hulk.name)