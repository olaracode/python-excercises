import random

def sum(a, b):
    return a + b

x = lambda a, b: a + b
# range(inicio, fin, steps) -> 
# Inicio es inclusivo, 
# fin es no inclusivo, 
# steps: cantidad de pasos por vuelta(?)
# range(5) [0, 1, 2, 3, 4]

# Domain Generator

adj = ["The", "We", "Hi"]
name = ["House", "People", "You"]
excuse = ["Ate my food", "Took my car", "Cualquier cosa"]
extensions = [".com", ".es", ".ve"]

#Domain generator
def domain_generator():
  for adjetivo in adj:
      for nombre in name:
          for extension in extensions:
              print("www." + adjetivo + nombre + extension)
domain_generator() # Ejecuto el domain_generator

# Excuse Generator
def excuse_generator():
    random_adj = random.choice(adj)
    random_name = random.choice(name)
    random_excuse = random.choice(excuse)
    print(random_adj, random_name, random_excuse)
excuse_generator() # Ejecuto el domain_generator
