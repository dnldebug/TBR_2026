from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait
from rotas import rotaI_missao1,rotaII_missao1,rotaIII_missao2,rotaIV_missao3, rotaV_missao4

hub = PrimeHub()

hub.system.set_stop_button(Button.BLUETOOTH)

def rota_1_missao1():
    #  código da rota 1 missao 1
    rotaI_missao1()
    pass

def rota3_missao2():
    #código da rota 3 missao 2
    rotaIII_missao2()
    pass

def rota_2_mission1():
    #  código da rota 2 missao 1
    rotaII_missao1()
    pass

def rota4_mission3():
    #  código da rota 4 missao 3
    rotaIV_missao3()
    pass;

def rota5_mission4():
    #Código da rota 5 missao 4 e 5
    rotaV_missao4()
    pass

rotas = [rota_1_missao1, rota3_missao2,rota_2_mission1,rota4_mission3,rota5_mission4]
selecionada = 0

def esperar_soltar():
    while hub.buttons.pressed():
        wait(10)

while True:
    hub.display.number(selecionada + 1)
    botoes = hub.buttons.pressed()

    if Button.RIGHT in botoes:
        selecionada = (selecionada + 1) % len(rotas)
        esperar_soltar()

    elif Button.LEFT in botoes:
        selecionada = (selecionada - 1) % len(rotas)
        esperar_soltar()

    elif Button.CENTER in botoes:
        esperar_soltar()
        rotas[selecionada]()                      # executa a rota
        selecionada = (selecionada + 1) % len(rotas)  # já deixa a próxima selecionada
    wait(10)
