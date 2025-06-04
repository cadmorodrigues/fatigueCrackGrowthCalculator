import tkinter, os, math
global toOnde
toOnde = [] 
toOnde.append("main")


"""_______________________________________________________'

> funções """

def meLocaliza(agora):
    toOnde.clear()
    toOnde.append(agora)
    
def mainClique(eventorigin):
    x0 = eventorigin.x
    y0 = eventorigin.y
    #print(toOnde)
    #print(toOnde)
    
    # quando na tela inicial
    if(toOnde[0] == "main"):
                # start
        if(x0 >= 98 and x0 <= 195 and y0 >= 138 and y0 <= 175):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = n1p1Background_arquivo)
            backgroundLabel.place(x=0, y=0)
            meLocaliza("select the crack type - P1")
            
        # options
        if(x0 >= 98 and x0 <= 195 and y0 >= 201 and y0 <= 228):
            #meLocaliza("options")
            print("options")
    
        # about
        if(x0 >= 84 and x0 <= 200 and y0 >= 252 and y0 <= 271):
            #meLocaliza("about")
            print("about")
            
    # quando na primeira tela de opções de trincas
    elif(toOnde[0] == "select the crack type - P1"):
        # saída para main
        if(x0 >= 1056 and x0 <= 1116 and y0 >= 9 and y0 <= 78):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = mainBackground_arquivo)
            backgroundLabel.place(x=0, y=0)       
            meLocaliza("main")
            
        # próxima página
        if(x0 >= 1076 and x0 <= 1108 and y0 >= 526 and y0 <= 557):
            global caixaA, caixaSigma, caixaW, caixaK 
            backgroundLabel = tkinter.Label(janelaPrincipal, image = n1p2Background_arquivo)
            backgroundLabel.place(x=0, y=0)
            meLocaliza("select the crack type - P2")
            
        # center-cracked
        if(x0 >= 440 and x0 <= 610 and y0 >= 137 and y0 <= 452):
            # background
            backgroundLabel = tkinter.Label(janelaPrincipal, image = n2centerCrackedBACKGROUND_arquivo)
            backgroundLabel.place(x=0, y=0)
            
            # caixas de input
            caixaA = tkinter.Entry (janelaPrincipal, font = ("Play", 12), justify="center") 
            caixaA.place(x = 523, y = 268, height= 37, width = 138)
            caixaSigma = tkinter.Entry (janelaPrincipal, font = ("Play", 12), justify="center") 
            caixaSigma.place(x = 523, y = 324, height= 37, width = 138)
            caixaW = tkinter.Entry (janelaPrincipal, font = ("Play", 12), justify="center") 
            caixaW.place(x = 738, y = 268, height= 37, width = 138)
            
            # localizando
            meLocaliza("center-cracked")
            
            
        # edge-cracked
        if(x0 >= 791 and x0 <= 940 and y0 >= 146 and y0 <= 447):
            print("edge-cracked") 
            # meLocaliza("edge-cracked")
            
    # quando na secunda tela de opções de trincas
    elif(toOnde[0] == "select the crack type - P2"):
        # saída para main
        if(x0 >= 1056 and x0 <= 1116 and y0 >= 9 and y0 <= 78):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = mainBackground_arquivo)
            backgroundLabel.place(x=0, y=0)       
            meLocaliza("main")
            
        # próxima página
        if(x0 >= 1076 and x0 <= 1108 and y0 >= 526 and y0 <= 557):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = n1p3Background_arquivo)
            backgroundLabel.place(x=0, y=0)
            meLocaliza("select the crack type - P3")
            
        # página anterior
        if(x0 >= 1032 and x0 <= 1065 and y0 >= 526 and y0 <= 557):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = n1p1Background_arquivo)
            backgroundLabel.place(x=0, y=0)
            meLocaliza("select the crack type - P1")
            
        # wide center-cracked
        if(x0 >= 110 and x0 <= 300 and y0 >= 120 and y0 <= 480):
            global caixaP, caixab, caixaB 
            
            # background
            backgroundLabel = tkinter.Label(janelaPrincipal, image = n2wideCenterCRACKEDbackground_arquivo)
            backgroundLabel.place(x=0, y=0)
            
            # caixas de input
            caixaA = tkinter.Entry (janelaPrincipal, font = ("Play", 12), justify="center") 
            caixaA.place(x = 523, y = 268, height= 37, width = 138)
            caixaP = tkinter.Entry (janelaPrincipal, font = ("Play", 12), justify="center") 
            caixaP.place(x = 523, y = 324, height= 37, width = 138)
            caixab = tkinter.Entry (janelaPrincipal, font = ("Play", 12), justify="center") 
            caixab.place(x = 738, y = 268, height= 37, width = 138)
            caixaB = tkinter.Entry (janelaPrincipal, font = ("Play", 12), justify="center") 
            caixaB.place(x = 738, y = 324, height= 37, width = 138)
            
            # localizando
            meLocaliza("wide center-cracked")
            
        # plate with a radially cracked hole loaded
        if(x0 >= 451 and x0 <= 667 and y0 >= 120 and y0 <= 480):
            print("plate with a radially cracked hole loaded") 
            # meLocaliza("plate with a radially cracked hole loaded")
            
        # two symmetric edge cracks
        if(x0 >= 831 and x0 <= 1016 and y0 >= 120 and y0 <= 480):
            print("two symmetric edge cracks") 
            # meLocaliza("two symmetric edge cracks")
             
    # quando na terceira tela de opções de trincas
    elif(toOnde[0] == "select the crack type - P3"):
        # saída para main
        if(x0 >= 1056 and x0 <= 1116 and y0 >= 9 and y0 <= 78):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = mainBackground_arquivo)
            backgroundLabel.place(x=0, y=0)       
            meLocaliza("main")
            
        # página anterior
        if(x0 >= 1032 and x0 <= 1065 and y0 >= 526 and y0 <= 557):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = n1p2Background_arquivo)
            backgroundLabel.place(x=0, y=0)
            meLocaliza("select the crack type - P2")
            
        # compacted-tension
        if(x0 >= 110 and x0 <= 300 and y0 >= 120 and y0 <= 480):
            print("compacted-tension")       
            # meLocaliza("compacted-tension")
            
        # edge-cracked bending
        if(x0 >= 451 and x0 <= 667 and y0 >= 120 and y0 <= 480):
            print("edge-cracked bending") 
            # meLocaliza("edge-cracked bending")
            
        # flat elliptical crack
        if(x0 >= 831 and x0 <= 1016 and y0 >= 120 and y0 <= 480):
            print("flat elliptical crack") 
            # meLocaliza("flat elliptical crack")    
    
    # quandod entro das telas de cada trinca
    # center-cracked
    elif(toOnde[0] == "center-cracked"):
        # saída para main
        if(x0 >= 1056 and x0 <= 1116 and y0 >= 9 and y0 <= 78):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = mainBackground_arquivo)
            backgroundLabel.place(x=0, y=0)       
            meLocaliza("main") 
            
        # solve
        if(x0 >= 896 and x0 <= 1023 and y0 >= 484 and y0 <= 522):
            
            # lendo imputados
            a = float(caixaA.get())
            sigma = float(caixaSigma.get())
            W = float(caixaW.get())
            
            # realizando contas para K
            auxK = (math.pi * a) / W
            auxK = 1 / math.cos(auxK)
            K = sigma * ((math.pi * a) ** 0.5) * (auxK ** 0.5)
            
            # saída de dados na rela
            if ((2*a/W)<=0.8):
                verifica = "| Reliable, 2*a/W = " + str(round(2*a/W, 2)) + " <= 0.80 "
            else:
                verifica = "| Unreliable, 2*a/W = " + str(2*a/W) + " > 0.80 "
            textoSaida = "K = " + str(round(K, 2)) + " MPa.m^0.5. " + verifica
            
            textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = textoSaida, font = ("Play", 10), justify="center")
            textoSaidaCAIXA.place(x = 523,y = 484, height = 37, width = 355)
        
    # wide center-cracked
    elif(toOnde[0] == "wide center-cracked"):
        # saída para main
        if(x0 >= 1056 and x0 <= 1116 and y0 >= 9 and y0 <= 78):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = mainBackground_arquivo)
            backgroundLabel.place(x=0, y=0)       
            meLocaliza("main") 
            
        # solve
        if(x0 >= 896 and x0 <= 1023 and y0 >= 484 and y0 <= 522):
            # lendo imputados
            a = float(caixaA.get())
            P = float(caixaP.get())
            b = float(caixab.get())
            B = float(caixaB.get())
            
            # realizando contas para K
            K = (P/(B*((math.pi * a) ** 0.5))) * (((a + b)/(a - b)) ** 0.5)
            
            # saída de dados na tela
            textoSaida = "K = " + str(round(K, 2)) + " MPa.m^0.5"
            
            textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = textoSaida, font = ("Play", 20), justify="center")
            textoSaidaCAIXA.place(x = 523,y = 484, height = 37, width = 355)
        
        
"""_______________________________________________________'

> main """
# > definições iniciais importantes
pastaAtual = os.path.dirname(os.path.realpath(__file__))
auxDiretorioPROJETO = pastaAtual.split('script')
caminhoBackground = str(auxDiretorioPROJETO[0]) + 'layout\\' + '/'

# > imagens dos backgrounds
mainBackground = caminhoBackground + 'N0.png'
n1p1Background = caminhoBackground + 'N1_P1.png'
n1p2Background = caminhoBackground + 'N1_P2.png'
n1p3Background = caminhoBackground + 'N1_P3.png'
n2centerCrackedBACKGROUND = caminhoBackground + 'N2_centerCracked.png'
n2wideCenterCRACKEDbackground  = caminhoBackground + 'N2_wideCenterCRACKED.png'

# > criação da janela
global janelaPrincipal
janelaPrincipal = tkinter.Tk()
janelaPrincipal.geometry('1120x573')
janelaPrincipal.title('Fatigue Crack Growth Calculator | R00')
janelaPrincipal.resizable(False, False)

# linkando backgrounds
mainBackground_arquivo = tkinter.PhotoImage(file = mainBackground)
n1p1Background_arquivo = tkinter.PhotoImage(file = n1p1Background)
n1p2Background_arquivo = tkinter.PhotoImage(file = n1p2Background)
n1p3Background_arquivo = tkinter.PhotoImage(file = n1p3Background)
mainBackground_arquivo = tkinter.PhotoImage(file = mainBackground)
n2centerCrackedBACKGROUND_arquivo = tkinter.PhotoImage(file = n2centerCrackedBACKGROUND)
n2wideCenterCRACKEDbackground_arquivo = tkinter.PhotoImage(file = n2wideCenterCRACKEDbackground)

# setando background
backgroundLabel = tkinter.Label(janelaPrincipal, image = mainBackground_arquivo)
backgroundLabel.place(x=0, y=0)



# >>> cliques
janelaPrincipal.bind("<Button 1>", mainClique)

janelaPrincipal.mainloop()
# <<fim  início de loop da janela principal