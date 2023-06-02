def sortdata(data, max_fitness): 

    data.sort(key=lambda a: a[1], reverse=True) 

    sumchance = 0 

    for i in range(len(data)): 

        chance = data[i][1] / max_fitness 

        data[i].append(chance) 

        sumchance += chance 

    for i in range(len(data)): 

        data[i].append(data[i][2] / sumchance) 

    return data 

