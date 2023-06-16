def elitism(data, share): 

    chroms = [] 

    survivals = int(len(data) * share) 

    data.sort(key=lambda a: a[4], reverse=True) 

    suvivors = data[:survivals] 

    for e in suvivors: 

        chroms.append(e[0])

    return chroms 

