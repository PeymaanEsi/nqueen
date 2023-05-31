import random 
size_n=8
def generate(choromozome):

  population=[random.choices(range(0,size_n), k=size_n) for _ in range(choromozome)]
  print(population)


if __name__  ==  "__main__":
      generate(100)
  