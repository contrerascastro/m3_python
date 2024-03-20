print("Protocolo de primeros auxilios\n")
print("Observe, responda a las preguntas y siga los pasos que se describen a continuación\n")

estimulo = input("El paciente responde a estímulos (puede escuchar, mirar, o palpar)? [s/n]: ").lower()#s; n; S; N;

if estimulo == "s":
    print("Lleve al paciente al centro de salud más cercano (Hospital, SAMU, SAPU o clínica)")
else:
    print("Abra la via aérea del paciente acostado: Con la yema de sus dedos bajo el mentón del paciente, eleve el mentón para abrir la vía aérea")
    
    respira = input("El paciente está respirando? [s/n]: ").lower()

    if respira == "s":
        print("Ponga al paciente en una posición de suficiente ventilación. Por ejemplo: recostado")
    else:
        print("Administre 5 ventilaciones y luego llame una ambulancia al 131")
        
        ambulancia= "n"
        while ambulancia == "n":
            signos_vida = input("¿Tiene signos de vida (pulso, pálpitos, respiración)?[s/n]:").lower()

            if signos_vida == "s":
                print("Monitoree los signos de vida a la espera de la ambulancia")
            else:
                print("Administre compresiones torácicas hasta que llegue la ambulancia")

            ambulancia= input("¿Llegó la ambulancia? [s/n]:").lower()
            
        
print("Bien hecho")