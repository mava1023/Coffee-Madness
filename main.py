from graphics import Lienzo
from random import randint, choice
from time import sleep as esperar

ANCHURA_LIENZO = 700
ALTURA_LIENZO = 400

def sprite_jugador(lienzo,altura_rect, diametro_circulo, x1_cabeza, y1_cabeza, color_jugador):
    x1= x1_cabeza
    y1 = y1_cabeza
    x2= x1 + diametro_circulo
    y2 = y1 + diametro_circulo
    altura_r = altura_rect

    distancia_cuadrado = 10

    x1_rect = x1 - distancia_cuadrado
    x2_rect = x2 + distancia_cuadrado
    y1_rect = y2 + 20
    y2_rect = y1_rect + altura_r
    lienzo.crear_óvalo(x1 - 80, y1 - 20, x2 + 80, y2_rect + 30,"#E8E9EB", "#adaaa1")
    lienzo.crear_óvalo(x1,y1,x2,y2, color_jugador)
    lienzo.crear_rectángulo(x1_rect, y1_rect, x2_rect,y1_rect + altura_r, color_jugador ) 
def sprite_pan(lienzo):
    #Se encarga de hacer el gráfico del tomate
    x1 = 312
    y1 = 193
    pan = lienzo.crear_imagen_con_tamaño(x1, y1, 55, 49, "pancito-removebg-preview.png")
    return pan, x1, y1

def sprite_tomate(lienzo):
    #Se encarga de hacer el gráfico del tomate
    x1 = 377
    y1 = 193
    tomate = lienzo.crear_imagen_con_tamaño(377, 193, 53, 41, "tomate-removebg-preview.png")
    return tomate, x1, y1

def sprite_lechuga(lienzo):
    #Se encarga de hacer el gráfico de la lechuga
    x1 = 308
    y1 = 130
    lechuga = lienzo.crear_imagen_con_tamaño(x1, y1, 46, 61, "lechuga.png")
    return lechuga, x1, y1

def sprite_queso(lienzo):
    #Se encarga de hacer el gráfico del queso
    x1 = 370
    y1 = 134
    queso = lienzo.crear_imagen_con_tamaño(x1, y1, 53, 51, "quesito-removebg-preview.png")
    return queso, x1, y1

def sprite_cafe_small(lienzo): 
    #Se encarga de hacer el gráfico del café pequeño
    x1 = 182
    y1 = 143
    s_coffee = lienzo.crear_imagen_con_tamaño(x1, y1, 34, 40, "smol_kopi.png")
    return s_coffee

def sprite_cafe_large(lienzo):
    #Se encarga de hacer el gráfico del café grande
    x1 = 182
    y1 = 143
    l_coffee = lienzo.crear_imagen_con_tamaño(x1, y1, 47, 57, "Cafe grande.png")
    return l_coffee

def sprite_basura(lienzo):
    basura = lienzo.crear_imagen_con_tamaño(605, 181, 100, 133, "basura.png")
    return basura

def sprite_cafetera(lienzo):
    cafetera = lienzo.crear_imagen_con_tamaño(61,30, 115, 179, "Cafetera.png")
    return cafetera

def sprite_boton_mapa(lienzo):
    boton = lienzo.crear_imagen_con_tamaño(7,10, 225, 40, "boton_xd.png")
    return boton

def perfil_jugador(lienzo):
    #Se encarga de preguntar al jugador un color en hexadecimal y el nombre y guardarlo
    lienzo.establecer_color_fondo("#E8E9EB")
    lienzo.crear_imagen_con_tamaño(0, 0, ANCHURA_LIENZO, 200, "vine.png")
    lienzo.crear_imagen_con_tamaño(0, ALTURA_LIENZO- 200, ANCHURA_LIENZO, 200, "vine.png")
    lienzo.crear_texto(ANCHURA_LIENZO/2, ALTURA_LIENZO/2, "Mira la consola", "Garamond", 40, "#313638")
    print("Hola, bienvenido a Coffee Madness")
    nombre_jugador= str(input("Por favor escribe tu nombre de usuario (que no termine con e o E):  "))
    colores = ["#FFC759","#296EB4","#E4B7E5", "#28965A", "#8A4F7D" ]
    color_jugador= choice(colores)
    print("Ahora mira el lienzo")
    lienzo.eliminar_todo()
    altura_rect = 100
    diametro_circulo = 70
    x1_cabeza = ANCHURA_LIENZO/ 2 - diametro_circulo/2
    y1_cabeza = 140
    sprite_jugador(lienzo,altura_rect, diametro_circulo, x1_cabeza, y1_cabeza, color_jugador)
    lienzo.crear_texto(ANCHURA_LIENZO/2, 85, "Bienvenid@ " + nombre_jugador, "Garamond", 40, "#313638")
    lienzo.crear_imagen_con_tamaño(50,100, 170, 200, "estrellitas verdes.png")
    lienzo.crear_imagen_con_tamaño(510,100, 170, 200, "corazones azules.png")

    return nombre_jugador
    
def mapa_niveles(lienzo, progreso_nivel):
    # Se encarga de crear un mapa en donde haya botones interactivos para entrar a los niveles y ver el progreso del jugador 

    circulo_n_1 = lienzo.crear_ovalo(39,113,154,232)
    circulo_n_2 = lienzo.crear_ovalo(206,78,322,197)
    circulo_n_3 = lienzo.crear_ovalo(374,60,492,179)
    circulo_n_4 = lienzo.crear_ovalo(515,113,633,232)
    circulo_n_5 = lienzo.crear_ovalo(416,214,534,332)
    circulo_n_6 = lienzo.crear_ovalo(260,252,375,370)
    circulo_n_7 = lienzo.crear_ovalo(102,269,219,390)
    mapa_niveles = lienzo.crear_imagen_con_tamaño(0, 0, ANCHURA_LIENZO, ALTURA_LIENZO, "mapa niveles.png")
    diametro_punto_marrón_feo = 23
    jaja =lienzo.crear_óvalo(110, ALTURA_LIENZO - diametro_punto_marrón_feo, 110 + diametro_punto_marrón_feo, ALTURA_LIENZO, "#E8E9EB")
    nivel = lienzo.crear_texto(470, ALTURA_LIENZO - 20, "Dale click al círculo del nivel en el que vas (" + str(progreso_nivel) + " )")
    return (circulo_n_1, circulo_n_2, circulo_n_3,circulo_n_4, circulo_n_5, circulo_n_6, circulo_n_7, mapa_niveles, jaja, nivel)

def entrar_nivel(lienzo, circulos_niveles, escogiendo):

 #Se encarga de entrar al nivel siguiente o correspondiente al progreso del jugador
    x_mouse = lienzo.obtener_mouse_x()
    y_mouse = lienzo.obtener_mouse_y()
    
    nivel_escogido = 0
    escogiendo_nivel = escogiendo

    while escogiendo_nivel == True:
        super_click_niveles = []
        ultimo_click = lienzo.obtener_ultimo_clic_mouse()
        if ultimo_click != None:
            x_click = ultimo_click[0]
            y_click = ultimo_click[1]
            super_click_niveles = lienzo.encontrar_superposiciones(x_click, y_click, x_click + 1, y_click + 1)
            for i in range(0,7):
                if circulos_niveles[i] in super_click_niveles:
                    escogiendo_nivel = False
                    nivel_escogido = i + 1
                
    
    return nivel_escogido
 

def barra_de_cafe(lienzo):
    #Se encarga de crear el mundo en donde el jugador va a hacer órdenes y entregarlas
    barra = lienzo.crear_imagen_con_tamaño(0, 0, ANCHURA_LIENZO, ALTURA_LIENZO, "mapa_cocina.png")
    pan_f = sprite_pan(lienzo)
    pan = pan_f[0]
    queso_f = sprite_queso(lienzo)
    queso = queso_f[0]
    tomate_f = sprite_tomate(lienzo)
    tomate = tomate_f[0]
    lechuga_f = sprite_lechuga(lienzo)
    lechuga = lechuga_f[0]
    basura = sprite_basura(lienzo)
    cafetera = sprite_cafetera(lienzo)
    volver_mapa = sprite_boton_mapa(lienzo)
    pan2 = lienzo.crear_imagen_con_tamaño(250,134, 55, 49, "pancito-removebg-preview.png")
    

    return (barra,pan,queso,tomate,lechuga,basura,cafetera,volver_mapa, pan2)
    
def manejar_tiempo(progreso_nivel, lienzo, tiempo_nivel, tiempo_actual, time):
    if tiempo_actual % 40 == 0:
        tiempo_nivel -= 1
        texto_tiempo = lienzo.establecer_texto(time, str(tiempo_nivel))

    tiempo_actual += 1
    return tiempo_nivel, tiempo_actual

def manejar_monedas(progreso_nivel, lienzo):
    monedas_iniciales = 5
    aumento_monedas = 10
    monedas_nivel = monedas_iniciales + (progreso_nivel * aumento_monedas)

    objetivo_monedas = lienzo.crear_texto (464,42, str (monedas_nivel), "Garamond", 20, "negro")

    return monedas_nivel, objetivo_monedas

def update_tus_monedas(texto_mis_monedas, mis_monedas, aumento_monedas, lienzo):
    mis_monedas = mis_monedas + aumento_monedas
    txt_monedas_mis= lienzo.establecer_texto(texto_mis_monedas,str(mis_monedas))
    return mis_monedas

def jugando_ando(lienzo, elementos, nivel_escogido, progreso_nivel,cafe_pequeño, cafe_grande):
    #Se encarga de unir todas las mecanicas del juego
    objetivo_monedas, texto_objetivo_monedas = manejar_monedas(progreso_nivel, lienzo)
    monedas_jugador = 0
    decremento_tiempo_por_n = 20
    tiempo_nivel = 180 - (progreso_nivel * decremento_tiempo_por_n)
    tiempo_actual = 0
    time = lienzo.crear_texto(101,364, str(tiempo_nivel), "Garamond", 20, "negro")
    esperar(1)
    mis_monedas = 0
    texto_mis_monedas = lienzo.crear_texto(384, 370, str(mis_monedas),"Garamond", 20, "negro")
    pan = elementos[1]
    queso = elementos[2]
    tomate= elementos[3]
    lechuga = elementos[4]
    basura = elementos[5]
    cafetera = elementos[6]
    boton_mapa = elementos[7]
    pan2 = elementos[8]

    texto = ""
    orden = lienzo.crear_texto (240,300,texto, "Garamond", 20, "Negro")
    orden_original = crear_una_orden()
    texto_orden_original = lienzo.establecer_texto(orden, "Orden: " + str(orden_original[0]) + ", " + str(orden_original[1]) + ", " + str(orden_original[2]) + ", " + str(orden_original[3]) + ", " + str(orden_original[4])+ ", " + str(orden_original[5]))

    ingredientes = [pan,queso,tomate,lechuga, pan2]
    orden_entregada = []

    while mis_monedas <= objetivo_monedas :
        click_mouse = lienzo.obtener_ultimo_clic_mouse()

        if click_mouse != None:
            x_click = click_mouse[0]
            y_click = click_mouse[1]
            super_mouse_comida = lienzo.encontrar_superposiciones(x_click,y_click, x_click + 1, y_click + 1)            
            for element in ingredientes:
                if element in super_mouse_comida:
                    figura = element
                    lienzo.moverse_hacia(figura, 471,153)
                    orden_entregada.append(figura)
            if cafetera in super_mouse_comida:
                tamaño_coffee = hacer_café(lienzo)
                if tamaño_coffee == 1:
                    lienzo.establecer_oculto(cafe_pequeño, False)
                    orden_entregada.insert(0,cafe_pequeño)
                elif tamaño_coffee == 2:
                    lienzo.establecer_oculto(cafe_grande,False)
                    orden_entregada.insert(0,cafe_grande)

            if basura in super_mouse_comida:
                for i in range (len(ingredientes)):
                    lienzo.establecer_oculto(ingredientes[i], True)
                lienzo.establecer_oculto(cafe_grande, True)
                lienzo.establecer_oculto(cafe_pequeño, True)

                lienzo.moverse_hacia(pan, 312 , 193)
                lienzo.moverse_hacia(tomate,377, 193)
                lienzo.moverse_hacia(lechuga, 308, 130)
                lienzo.moverse_hacia(queso, 370, 134)
                lienzo.moverse_hacia(pan2,250,134)
                
                for i in range (len(ingredientes)):
                    lienzo.establecer_oculto(ingredientes[i], False)

                orden_entregada =[]    
                tiempo_nivel -= 7


        ultimo_teclado = lienzo.obtener_ultimo_clic_teclado()
        if ultimo_teclado != None:
            if "e" in ultimo_teclado:
                aumento_monedas = verificar_orden(orden_original, orden_entregada)
                mis_monedas= update_tus_monedas(texto_mis_monedas, mis_monedas, aumento_monedas, lienzo)
                for i in range (len(ingredientes)):
                    lienzo.establecer_oculto(ingredientes[i], True)
                lienzo.establecer_oculto(cafe_grande, True)
                lienzo.establecer_oculto(cafe_pequeño, True)

                lienzo.moverse_hacia(pan, 312 , 193)
                lienzo.moverse_hacia(tomate,377, 193)
                lienzo.moverse_hacia(lechuga, 308, 130)
                lienzo.moverse_hacia(queso, 370, 134)
                lienzo.moverse_hacia(pan2,250,134)
                
                for i in range (len(ingredientes)):
                    lienzo.establecer_oculto(ingredientes[i], False)

                orden_original = crear_una_orden()
                texto_orden_original = lienzo.establecer_texto(orden, "Orden: " + str(orden_original[0]) + ", " + str(orden_original[1]) + ", " + str(orden_original[2]) + ", " + str(orden_original[3]) + ", " + str(orden_original[4])+ ", " + str(orden_original[5]))
                
                orden_entregada = []
                ingredientes = [pan,queso,tomate,lechuga, pan2]
                
        tiempo_nivel, tiempo_actual= manejar_tiempo(progreso_nivel, lienzo, tiempo_nivel,tiempo_actual, time)
        esperar(1/60)
        if tiempo_nivel == 0:
            resultado_nivel = False


    if tiempo_nivel > 0:
        if monedas_jugador <= objetivo_monedas:
            resultado_nivel = True

    super_lienzo = lienzo.encontrar_superposiciones(0,0,ANCHURA_LIENZO,ANCHURA_LIENZO)
    
    lienzo.eliminar(orden)
    lienzo.eliminar(time)
    lienzo.eliminar(texto_objetivo_monedas)
    lienzo.eliminar(texto_mis_monedas)
    for element in super_lienzo:
        lienzo.establecer_oculto(element,True)

    return resultado_nivel
        
    
def hacer_café(lienzo):
    #Se encarga de hacer el gráfico de la cafetera
    tamaño_cafe = 0

    tamaño= 75
    small = lienzo.crear_rectangulo(71,210, 71 + tamaño, 232, "#E8E9EB")
    t_small = lienzo.crear_texto(105,221, "Pequeño", "Garamond", 18, "negro")
    large = lienzo.crear_rectangulo(195,210, 195 + tamaño, 232, "#E8E9EB")
    t_large = lienzo.crear_texto(225,221, "Grande", "Garamond", 18, "negro")

    lienzo.esperar_por_clic()
    ultimo_click = lienzo.obtener_ultimo_clic_mouse()
    if ultimo_click != None:
        x_mouse = ultimo_click[0]
        y_mouse = ultimo_click[1]
        super_opcion_cafe = lienzo.encontrar_superposiciones(x_mouse, y_mouse, x_mouse + 1, y_mouse + 1)

        if small in super_opcion_cafe :
            tamaño_cafe = 1

        if large in super_opcion_cafe:
            tamaño_cafe = 2

    
    lienzo.eliminar(small)
    lienzo.eliminar(t_small)
    lienzo.eliminar(large)
    lienzo.eliminar(t_large)
    
    return tamaño_cafe

def crear_una_orden():
    ingredientes =  ['tomate', 'lechuga', 'queso']
    cafe = ['café pequeño', 'café grande']

    tamaño_cafe = choice (cafe)
    san1 = choice(ingredientes)
    ingredientes.pop(ingredientes.index(san1))
    san2 = choice(ingredientes)
    ingredientes.pop(ingredientes.index(san2))
    san3 = choice(ingredientes)

    orden= [tamaño_cafe,'pan',san1, san2,san3, 'pan']

    return orden

def verificar_orden(orden_original, orden_entregada):
    comida = {"shape_10":'pan',"shape_11":'queso', "shape_12":'tomate', "shape_13":'lechuga', 'shape_17': 'pan',"shape_18" : 'café pequeño', "shape_19":'café grande'}

    orden_entregada_traducida=[]
    for element in orden_entregada:
        orden_entregada_traducida.append(comida[element])

    aumento_monedas = 0
    if orden_original == orden_entregada_traducida:
        aumento_monedas = 7
    else :
        aumento_monedas = -7
    
    return aumento_monedas

    
def mouse(lienzo):
    while True:
        x = lienzo.obtener_mouse_x()
        y = lienzo.obtener_mouse_y()
        print(x,y)


def main():
    lienzo = Lienzo(ANCHURA_LIENZO, ALTURA_LIENZO)
    nombre_jugador = perfil_jugador(lienzo)
    elementos= barra_de_cafe(lienzo)
    for element in elementos:
        lienzo.establecer_oculto(element, True)
    cafe_pequeño = sprite_cafe_small(lienzo)
    cafe_grande = sprite_cafe_large(lienzo)
    lienzo.establecer_oculto(cafe_pequeño, True)
    lienzo.establecer_oculto(cafe_grande, True)

    esperar(3)
    progreso_nivel = 1

    while progreso_nivel <= 7:
        
        circulos_niveles = mapa_niveles(lienzo, progreso_nivel)
        escogiendo = True

        nivel_escogido = entrar_nivel(lienzo, circulos_niveles, escogiendo)
        
        if  progreso_nivel == nivel_escogido:
            for element in circulos_niveles:
                lienzo.establecer_oculto(element, True)

            for i in range (len(elementos)):
                lienzo.establecer_oculto(elementos[i], False)

            result = jugando_ando(lienzo, elementos, nivel_escogido, progreso_nivel, cafe_pequeño, cafe_grande)
            if result == True:
                    progreso_nivel += 1
                    
    
        else:
            while progreso_nivel != nivel_escogido :
                for element in circulos_niveles:
                        lienzo.establecer_oculto(element, True)
                rect = lienzo.crear_rectangulo(0, 0, ANCHURA_LIENZO, ALTURA_LIENZO, "blanco")
                txt = lienzo.crear_texto(ANCHURA_LIENZO/2, ALTURA_LIENZO/ 2, "Dale click al círculo del nivel en el que vas (" + str(progreso_nivel) + " )")
                esperar(3)
                lienzo.eliminar(rect)
                lienzo.eliminar(txt)

                for element in circulos_niveles:
                        lienzo.establecer_oculto(element, False)
                
                escogiendo = True
                nivel_escogido = entrar_nivel(lienzo, circulos_niveles, escogiendo)

                if progreso_nivel == nivel_escogido:
                    for i in range (len(elementos)):
                        lienzo.establecer_oculto(elementos[i], False)
                    for element in circulos_niveles:
                        lienzo.establecer_oculto(element, True)
                    

                    result = jugando_ando(lienzo,elementos,nivel_escogido, progreso_nivel, cafe_pequeño, cafe_grande)

                    if result == True:
                        progreso_nivel += 1
                
                    for element in elementos:
                        lienzo.establecer_oculto(element, True)
    
    if progreso_nivel > 7 :
        lienzo.eliminar_todo()
        lienzo.crear_texto(ANCHURA_LIENZO/2, ALTURA_LIENZO/2, "Felicitaciones " + nombre_jugador + ", has pasado todos los niveles", "Garamond", 30)
            
            
        
if __name__ == '__main__':
    main()