def estructura(names, goals, goals_avoided, assists):
   i = 0
   jugadores = {}    
    
   for name in names:
       jugadores[name] = dict(zip(("goals", "goals_avoided", "assists"), (goals[i], goals_avoided[i], assists[i])))
       i += 1
   return jugadores

#-----------------------------------------------------------------------------------------------------------------
#def goleador(jugadores):
    #nombre, goles = max(jugadores.items(), key= lambda x: x[1]["goals"])
    #return nombre, goles["goals"]

def goleador(jugadores):
    nombre = " "
    maxi = -1
    for jugador in jugadores:
        if jugadores[jugador]["goals"] > maxi:
            maxi = jugadores[jugador]["goals"]
            nombre = jugador
    return nombre, maxi
#-------------------------------------------------------------------------------------------------------------------
def influencias(jugadores):
    dic_influencias = {jugador: (jugadores[jugador]["goals"] * 1.5) + (jugadores[jugador]["goals_avoided"] * 1.25) +     
    jugadores[jugador]["assists"] for jugador in jugadores}
    return dic_influencias
#-------------------------------------------------------------------------------------------------------------------
def mas_influyente(jugadores):
    dic_influyentes = influencias(jugadores)
    influyente = max(dic_influyentes, key= lambda x: dic_influyentes[x])
    return influyente
#-------------------------------------------------------------------------------------------------------------------
#Otra opcion:
#def promedio_gol(goals):
    #promedio = sum(goals) / partidos
    #return promedio


def promedio_gol(jugadores):
    total = 0
    for jugador in jugadores:
        total += jugadores[jugador]["goals"]
    promedio = total / 25
    return promedio
#-------------------------------------------------------------------------------------------------------------------
def promedio_gol_jugador(jugadores, jugador):
    promedio = jugadores[jugador]["goals"] / 25
    return promedio