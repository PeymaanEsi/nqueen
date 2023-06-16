def sortdata(data, max_fitness): 

    data.sort(key=lambda a: a[1], reverse=True) 

    sumchance = 0 

    selectchance = 0 

    for i in range(len(data)): 

        rank = len(data) - i 

        data[i].append(rank) 

        chance = rank / len(data) 

        data[i].append(chance) 

        sumchance += chance 

    for i in range(len(data)): 

        data[i].append(data[i][3] / sumchance) 

        selectrange = [] 

        selectrange.append(selectchance) 

        selectchance += data[i][4] 

        selectrange.append(selectchance) 

        data[i].append(selectchance) 

        data[i].append(selectrange) 

    return data 

