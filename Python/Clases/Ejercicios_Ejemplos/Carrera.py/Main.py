import Menus 
import Participantes

while True: 
    opc = Menus.Menu_Principal()
    if opc == 1 : 
        opc_participantes = Menus.Menu_Registrar_Participantes()
        Participantes.Registrar_Participantes(opc_participantes)
    elif opc == 2 : 
        opc_ranking = Menus.Menu_Mostrar_Ranking()
        