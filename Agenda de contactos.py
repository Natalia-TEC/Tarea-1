                                    #Agenda de Contactos
#------------------------------------------------------------------------------------------------------------------------------------------ 
"""
Nombre: AgendaDeContactos()
Entrada:
    Número de la opción = el número de la opcion que necesita realizar según los diferentes menús.
Salidas:
    Ejecución de la opción que desea realizar.
Retricciones:
    Dígitar un número que se encuentre en las opciones disponibles.
"""

def AgendaDeContactos():
                                    #Menú principal
    print("\t", "\t", "\t", ">>>>+ Agenda de contactos +<<<<")
    print("1. Mantenimiento de contactos. ")
    print("2. Búsquedas avanzadas. ")
    print("3. Total contactos. ")
    print("\t")
    print("9. Salir. ")
                                    #Control del menú principal
    opcion=input("Dígite el número de la opción que desea realizar: ")
    print("\n")
#Al dígitar la opción lo retorna a la función que desea realizar.
    if(opcion=="1"):
        return MantenimientoDeContactos()
    elif(opcion=="2"):
            return BúsquedasAvanzadas()
    elif(opcion=="3"):#En esta opción se realiza de forma directa sin llamar a alguna función.
            archivo="agregarContacto.txt"
            agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
            """
            En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
            que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
            nombre de agenda para que fuera de mejor entendimiento.
            """
            contador =1
            for linea in agenda:
                contador+=1#Se agregó un contador para que cada vez que creemos un contacto el se sume a los ya existentes.
            mensaje = agenda.readlines()
            print(mensaje)
            agenda.close()#Importante cerrar el archivo.
            """
            En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
            nombre de agenda para que fuera de mejor entendimiento.
            """
            print("\t", "\t", "\t", ">>>- Total de contactos -<<<")
            print(f"La cantidad de contactos que posee en su agenda es de {contador//8} contactos.") #{contador//8} Devuelve el total de contactos ingresados en la agenda.
            print()
            print("\n")
            return AgendaDeContactos()
    elif(opcion=="9"):#Esta opción se utilizara por si el usuario ya desea salir de la agenda de contactos.
        return print("\t", "\t", "\t", "-- Fue un placer atenderlo -- ")
    else:#Este error es por si el usuario dígito un valor que no pertencia a las opciones del menú.
        print("** Ingrese un número que corresponda con una de las opciones disponibles **")
        print("\t")
        return AgendaDeContactos()
    
#------------------------------------------------------------------------------------------------------------------------------------------         
                                    #Menú de mantenimiento de contactos
"""
Nombre: MantenimientoDeContactos()
Entrada:
    Número de la opción = el número de la opcion que necesita realizar según los diferentes menús.
Salidas:
    Ejecución de la opción que desea realizar.
Retricciones:
    Dígitar un número que se encuentre en las opciones disponibles.
"""
def MantenimientoDeContactos():
    print("\t", "\t", "\t", ">>>- Mantenimiento de contactos -<<<")
    print("\t")
    print("11. Agregar contacto. ")
    print("12. Borrar contacto. ")
    print("13. Modificar contacto. ")
    print("14. Ver todos los contactos. ")
    print("15. Retornar. ")
    print("\n")
    opcion=input("Dígite el número de la opción que desea realizar:")

#Al dígitar la opción lo retorna a la función que desea realizar.
    if(opcion=="11"):
        return print("\t", "\t", "\t", ">>> Agregar contacto <<<"), agregarContacto()
    elif(opcion=="12"):
        return print("\t", "\t", "\t", ">>> Borrar contacto <<<"), BorrarContacto()
    elif(opcion=="13"):
        return print("\t", "\t", "\t", ">>> Modificar contacto <<<"), ModificarContacto()
    elif(opcion=="14"):#En esta opción se realiza de forma directa sin llamar a alguna función.
        return print("\t", "\t", "\t", ">>> Contactos existentes <<<"), VerTodosLosContactos()
    elif(opcion=="15"):
        return AgendaDeContactos()
    else:
        print("Error: Dígite una de las opciones disponibles. ")
        #Este error se imprimira si el usuario ingresa una respuesta que no este las opciones.
        return MantenimientoDeContactos()

#------------------------------------------------------------------------------------------------------------------------------------------ 
                                        #Funciones de mantenimiento de contactos (Agregar contacto)
"""
Nombre: agregarContacto()
Entrada:
    cedula = ingresar un número entero que contenga 10 dígitos.
    Nombre = ingresar su nombre 
    apellidos = ingresar sus apellidos completos
    sexo = ingresar una de las dos variables (H o M) según corresponda.
    telefono = ingresar un número entero que contenga 8 dígitos.
    correoElectronico = ingresar su correo electrónico.
    lugarDeTrabajo = ingresar su lugar de trabajo.
Salidas:
    Debe de escribir los datos anteriores en el archivo.txt que tenemos creado para la agenda.
Retricciones:
    cedula = debe tener 10 dígitos
    sexo = Solo debe aceptar las variables (H o M) según corresponda.
    telefono = debe tener solo 8 dígitos sin separadores.
    correoElectronico = debe contener el carácter @.
    No debe repetir cédulas.
"""
def agregarContacto():#Esta función agrega los contactos a la agenda.
    archivo="agregarContacto.txt"
    cedula=int(input("Dígite el número de cédula: "))
    verificar=ListaDeContactos()
    if(isinstance(cedula,int)and cedula >999999999)and cedula<10000000000:#Validación del dato dato ingrasado para verificar si cumple con las restricciones.
        cedula=str(cedula)
        if(cedula+"\n" in verificar)==False:#Validación del dato para que no se repitan las cédulas.
            Nombre=input("Ingrese su nombre: ")
            if(isinstance(Nombre,str)):#Validación del dato dato ingrasado para verificar si cumple con las restricciones.
                apellidos=input("Ingrese sus apellidos: ")
                sexo=input("Ingrese su sexo según M(mujer) o H(hombre): ")
                if(isinstance(apellidos,str)and isinstance(sexo,str)and sexo=="H" or sexo=="M"):#Validación del dato dato ingrasado para verificar si cumple con las restricciones.
                   telefono=input("Dígite su numero de teléfono: ")
                   telefono=int(telefono)
                   if(isinstance(telefono,int)and telefono>9999999)and telefono<100000000:#Validación del dato dato ingrasado para verificar si cumple con las restricciones.
                       correoElectronico=input("Ingrese su correo electronico, con el caráctes @: ")
                       if(isinstance(correoElectronico,str)and "@" in correoElectronico):#Validación del dato dato ingrasado para verificar si cumple con las restricciones.
                           agenda = open (archivo,'a')#Se abre el archivo en el modo que deseamos.
                           """
                           En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                           que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                           nombre de agenda para que fuera de mejor entendimiento.
                           """
                           #Se escriben los datos recolectados en el archivo.txt, en nuestro caso ese archivo lleva el nombre de "agregarContacto.txt".
                           agenda.write(cedula+"\n")
                           agenda.write(Nombre+"\n")
                           agenda.write(apellidos+"\n")
                           agenda.write(sexo+"\n")
                           telefono=str(telefono)
                           agenda.write(telefono+"\n")
                           agenda.write(correoElectronico+"\n")
                           lugarDeTrabajo=input("Ingrese su lugar de trabajo: ")
                           agenda.write(lugarDeTrabajo+"\n")
                           agenda.write("--------------------------"+"\n")
                           agenda.close()#Importante cerrar el archivo.
                           """
                           En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                           nombre de agenda para que fuera de mejor entendimiento.
                           """
                           print("\n", "\t", "\t", "\t","¡Contacto agregado exitosamente! ")
                           #imprimimos un mesaje para comunicarle al usuari que el contacto a sido agregado con éxito.
                           print("\n")
                           return MantenimientoDeContactos()
                           """
                           Apartir de aquí se imprimen los errores, según no se cumpla con las restricciones predeterminadas,
                           todos los errores lo retonan al principio de la funcion de agregarContacto() para que lo vuelva a
                           intentar.
                           """
                       else:
                           print("Error: Dígite un correo que contenga el cáracter @. ")
                           return agregarContacto()
                   else:
                       print("Error: Dígite un número de teléfono con 8 dígitos. ")
                       return agregarContacto()
                else:
                    print("Error: Dígite M(mujer) o H(hombre) según corresponda.  ")
                    return agregarContacto()
        else:
            print(f"Error: Cédula repetida. La cédula {cedula} ya existe en nuestra agenda de contactos. ")
            print("Por favor ingresar de nuveo los datos del contacto que desea agregar.")
            return agregarContacto()
    else:
        print("Error: Dígite una cedula con 10 dígitos. ")
        return agregarContacto()
    
#------------------------------------------------------------------------------------------------------------------------------------------ 
                                        #Funciones de mantenimiento de contactos (Borrar contacto)
"""
Nombre: MantenimientoDeContactos()
Entrada:
    Número entero = el número de cédula del contacto que desea borrar.
Salidas:
    Va a eliminar el contacto del archivo.txt y después va a imprimir un mensaje dependiendo de su ejecución.
Retricciones:
    Para poder eliminar va tener que dígitar el número de cédula del contacto que desea eliminar.
"""
def BorrarContacto():
    cedula=input("Dígite el número de cédula del contacto que desea borrar: ")
    agenda= open("agregarContacto.txt")#Se abre el archivo.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    Contactos = agenda.readlines()#Lee las líneas del archivo.
    if ((cedula + "\n") in Contactos):#Verificamos si el número de cédula esta en nuestra agenda.
        linea = Contactos.index(cedula + "\n")
        Contactos = EliminarContacto(Contactos,linea, 0)#Llamamos una función para eliminar el contacto.
        agenda.close()
        agenda = open("agregarContacto.txt", "w")#Se abre el archivo en el modo que deseamos.
        agenda.write(Contactos)
        agenda.close()#Importante cerrar el archivo.
        """
        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
        nombre de agenda para que fuera de mejor entendimiento.
        """
        #Imprime un comunicado para informarle al usuario que el contacto fue eliminado de una forma exitosa.
        print(f"¡El contacto con la cédula {cedula} a sido elimidado exitosamente!")
        print("\n")
        return AgendaDeContactos()
    else:#Inprime un comunicado debido a que la cédula no se encuentra.
        print(f"No hay ningún contacto con la cédula [cedula], vuelva a intentarlo.")
        agenda.close()#Importante cerrar el archivo.
        return BorrarContacto()
    
#------------------------------------------------------------------------------------------------------------------------------------------ 
#Función que elimina el contacto.
"""
Nombre: EliminarContacto(Contactos,linea, contador)
Entrada:
    Contactos = una variable que tiene el valor de *EliminarContacto(Contactos,linea, 0)*
    linea = una variable que tiene el valor de *Contactos.index(cedula + "\n")*
    Contador = una variable que tiene como valor inicial 0.
Salidas:
    Va a eliminar el contacto del archivo.txt y  va a convertir el dato en un string.
Retricciones:
    Los parámetro de entrada debe de ser verificados.
"""
def EliminarContacto(Contactos,linea, contador):
    if contador == 8:#Cada contacto va a tener 8 líneas con información solicitada. 
        return convertir_a_string(Contactos)#Llama a una función, para covertir el dato ingresado en un string.
    else:
        print(Contactos[linea].rstrip())
        Contactos.pop(linea)
        return EliminarContacto(Contactos,linea, contador + 1)#Se retorna la función que elimina el contacto.
    
#------------------------------------------------------------------------------------------------------------------------------------------
#Función que convierte un dato en un string.
"""
Nombre: convertir_a_string(lista)
Entrada:
    lista = al dato que se desea convertir.
Salidas:
    Va a convertir el dato en un string.
Retricciones:
    El parámetro debe de ser una lista.
"""
def convertir_a_string(lista):
    if isinstance(lista, list):#El parámetro de entrada debe de ser una lista(restricción).
        string = ""
        for linea in lista:
            string += linea
        return string
    else:#Se imprime el error en el caso de que el parámetro de entrada no cumple con las restriciones predeterminadas.
        print("Error: No se puede convertir a string, debido a que el tipo de dato de entrada no es una lista.")


#------------------------------------------------------------------------------------------------------------------------------------------ 
                                        #Funciones de mantenimiento de contactos (Modificar contacto)
"""
Nombre: ModificarContacto()
Entrada:
    cedula = número de cédula del contacto que se desea eliminar.
Salidas:
    Hace la modificación del contacto.
Retricciones:
    cedula, debe de cumplir con las restricciones de la función principal.
"""
def ModificarContacto():
    cedula=input("Dígite el número de cédula del contacto que desea modificar: ")
    listaContactos = ListaDeContactos()
    if ((cedula + "\n") in listaContactos):#Verificamos que el número de cédula se encuetre en el archivo. 
        indice = listaContactos.index(cedula + "\n")
        MostrarContacto(listaContactos, indice, 0)
        listaModificada = ModificarContacto_Aux(listaContactos, indice + 1, 0)#Se creo una variable para ingresar los nuevos datos.
        agenda = open("agregarContacto.txt", "w")#Se abre el archivo en el modo que deseamos.
        """
        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
        nombre de agenda para que fuera de mejor entendimiento.
        """
        agenda.write(convertir_a_string(listaModificada))#Se escribe la modificación del contacto en el archivo.
        agenda.close()#Importante cerrar el archivo.
        """
        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
        nombre de agenda para que fuera de mejor entendimiento.
        """
        print("\n", "\t", "\t", "\t","¡Contacto modificado con éxito! ", "\n")
        return AgendaDeContactos()
    else:
        print("No tienes ningún contacto con el número de cédula ", cedula, "vuelva a intentarlo de nuevo.")
        return ModificarContacto()#Retorna nuevamente a la función para que el usuario lo vuelva a intentar.
    
#------------------------------------------------------------------------------------------------------------------------------------------ 
#Función para mostrar el contacto.
"""
Nombre: MostrarContacto(listaContactos, indice, cont)
Entrada:
    listaContactos = una variable que tiene el valor de *ListaDeContactos()*
    indice = una variable que tiene el valor de *listaContactos.index(cedula + "\n")*
    cont = valor inicial 0.
Salidas:
    Muestra el contacto que va hacer modificado.
Retricciones:
    El parámetro de entrada debe de ser verificado.
"""
def MostrarContacto(listaContactos, indice, cont):
    if cont > 6:#Se hace la debida verificación de la restricción.
        print("\n")
    else:#Si la primera restricción no se cumple se retorna a esta.
        print(listaContactos[indice].rstrip())
        return MostrarContacto(listaContactos, indice + 1, cont + 1)#Muestra el contacto que el usuario desea eliminar.

#------------------------------------------------------------------------------------------------------------------------------------------ 
#Funcion de lista de contactos.
"""
Nombre: MostrarContacto(listaContactos, indice, cont)
Entrada:
    Va abrir el archivo.
Salidas:
    Va a leer las líneas del archivo.
Restricciones:
    Abrir el archivo correcto.
"""   
def ListaDeContactos():
    agenda = open("agregarContacto.txt")#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    listaDeContactos = agenda.readlines()#Lee el archivo.
    agenda.close()#Importante cerrar el archivo.
    """
    En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    return listaDeContactos

#------------------------------------------------------------------------------------------------------------------------------------------
#Función de modificar contacto.
"""
Nombre: ModificarContacto_Aux(agenda, linea, contador)
Entradas: (agenda, linea, contador)
Salida:
    Va a retornar el contacto modificado.
Restricciones:
    Los parámetros de entrada deben de ser verificados.
"""
def ModificarContacto_Aux(agenda, linea, contador):
    if contador == 6:
        return agenda#Archivo al cual le se le dió ese nombre.
    else:#Se hacen las modificaciones del contacto respectivamente.
        if contador == 0:
            ContactoModificado = input("Ingrese el nuevo nombre que desea: ")
            agenda[linea] = ContactoModificado + "\n"
            return ModificarContacto_Aux(agenda, linea+1, contador+1)
        elif(contador==1):
            ContactoModificado = input("Ingrese el nuevo apellido que desea: ")
            agenda[linea] =  ContactoModificado + "\n"
            return ModificarContacto_Aux(agenda, linea+1, contador+1)
        elif(contador==2):
            ContactoModificado = input("Ingrese el nuevo sexo que desea, M(mujer) o H(hombre) según corresponda: ")
            if(ContactoModificado=="H")or ContactoModificado=="M":
                agenda[linea] = ContactoModificado + "\n"
                return ModificarContacto_Aux(agenda, linea+1, contador+1)
            else:
                print("Dígite M(mujer) o H(hombre) según corresponda. ")
                return ModificarContacto_Aux(agenda, linea, contador)
        elif(contador==3):
            ContactoModificado = int(input("Dígite nuevo el número de teléfono: "))
            if(ContactoModificado>9999999)and ContactoModificado<100000000:
                ContactoModificado=str(ContactoModificado)
                agenda[linea] = ContactoModificado + "\n"
                return ModificarContacto_Aux(agenda, linea+1,contador+1)
            else:
                print("Dígite un número de teléfono con 8 dígitos ")
                return ModificarContacto_Aux(agenda,linea,contador)
        elif(contador==4):
            ContactoModificado = input("Ingrese su nuevo correo electronico, con el caráctes @: ")
            if("@" in ContactoModificado):
                agenda[linea] = ContactoModificado + "\n"
                return ModificarContacto_Aux(agenda, linea+1,contador+1)
            else:
                print("Dígite un correo que contenga el cáracter @. ")
                return ModificarContacto_Aux(agenda,linea,contador)
        else:
            ContactoModificado= input("Ingrese su nuevo lugar de trabajo: ")
            agenda[linea] = ContactoModificado + "\n"
            return ModificarContacto_Aux(agenda, linea+1,contador+1)

#------------------------------------------------------------------------------------------------------------------------------------------ 
                                        #Funciones de mantenimiento de contactos (Ver todos los contactos)
"""
Nombre: VerTodosLosContactos()
Entradas:
    El archivo en modo de lectura.
Salida:
    Va a dar una lista de todos lo contactos existentes en la agenda.
Restricciones:
    Abrir el archivo de manera correcta.
"""        
def VerTodosLosContactos():
    archivo="agregarContacto.txt"
    agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    contador =1
    for linea in agenda:
        print("linea",contador,":",linea)#Imprimir todos los contactos existentes en la agenda.
        contador+=1 #Agregamos un contador para que el usuario pueda ver en que linea corresponde a cada dato. 
    agenda.close()#Importante cerrar el archivo.
    """
    En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    return MantenimientoDeContactos()
                      
#------------------------------------------------------------------------------------------------------------------------------------------ 
                                        #Menú de Búsquedas avanzadas
"""
Nombre: BúsquedasAvanzadas()
Entrada:
    Número de la opción = el número de la opcion que necesita realizar según los diferentes menús.
Salidas:
    Ejecución de la opción que desea realizar.
Retricciones:
    Dígitar un número que se encuentre en las opciones disponibles.
"""  
def BúsquedasAvanzadas():
    print("\t", "\t", "\t", ">>>- Búsquedas avanzadas -<<<")
    print("\t")
    print("21. Buscar por nombre. ")
    print("22. Buscar por teléfono. ")
    print("23. Buscar por lugar de trabajo. ")
    print("24. Buscar por correo electrónico. ")
    print("25. Retonar. ")
    print("\n")
    opcion=input("Dígite la opcion que necesita realizar: ")
    #Al dígitar la opción lo retorna a la función que desea realizar.
    if(opcion=="21"):
        return print("\t", "\t", "\t", ">>> Búsqueda por nombre <<<"), BuscarNombre()
    elif(opcion=="22"):
        return print("\t", "\t", "\t", ">>> Búsqueda por número de teléfono <<<"), BuscarTelefono()
    elif(opcion=="23"):
        return print("\t", "\t", "\t", ">>> Búsqueda por lugar de trabajo <<<"), BuscarPorLugarDeTrabajo()
    elif(opcion=="24"):
        return print("\t", "\t", "\t", ">>> Búsqueda por correo electrónico <<<"), BuscarPorCorreo()
    elif(opcion=="25"):
        return AgendaDeContactos()
    else:
        print("Dígite una de las opciones presentes en el menú: ")
        return BúsquedasAvanzadas()

#------------------------------------------------------------------------------------------------------------------------------------------ 
"""
Nombre: BúsquedasAvanzadas()
Entrada:
    nombre = nombre del contacto que desea buscar.
Salidas:
    Retorna el o los contactos al que pertence que ese nombre.
Retricciones:
    Que nombre cumpliera las restricciones dadas en su función madre *agregarContacto()*
"""    
def BuscarNombre():
    nombre=input("Dígite el nombre del contacto que desea buscar: ")
    listaContactos = ListaDeContactos()
    BuscarContacto(listaContactos, nombre,1, False,1,"nombre")#Busca el contacto solicitado y retorna la información del mismo.
    return BúsquedasAvanzadas()

#------------------------------------------------------------------------------------------------------------------------------------------ 
"""
Nombre: BúsquedasAvanzadas()
Entrada:
    telefono = número de teléfono del contacto que desea buscar.
Salidas:
    Retorna el o los contactos al que pertence que ese número de teléfono.
Retricciones:
    Que telefono cumpliera las restricciones dadas en su función madre *agregarContacto()*
""" 
def BuscarTelefono():
    telefono=input("Dígite el número de teléfono del contacto que desea buscar: ")
    listaContactos = ListaDeContactos()
    BuscarContacto(listaContactos, telefono,4, False, 4,"telefono")#Busca el contacto solicitado y retorna la información del mismo.
    return BúsquedasAvanzadas()  
    
#------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: BuscarContacto(Contactos, buscar,linea,ExisteElContacto, PrimeraLinea,nombre)
Entrada: (Contactos, buscar,linea,ExisteElContacto, PrimeraLinea,nombre)
Salidas:
    Retornara la búsqueda del contacto según corresponda.
Retricciones:
    Verificacion de los parámetros de entrada.
""" 
def BuscarContacto(Contactos, buscar,linea,ExisteElContacto, PrimeraLinea,nombre):#Función que ayuda al funcionamiento de las funciones de búsqueda.
    if linea > len(Contactos):
        if ExisteElContacto:
            print(f"Estos son los contactos encontrados según el dato que ingreso. ")
        else:
            print(f"No se encontro nigún contacto que contenga el dato que ingreso, vuelva a intentarlo de nuevo.")
    else:
        if buscar in Contactos[linea]:
            MostrarContacto(Contactos,linea - PrimeraLinea, 0)
            return BuscarContacto(Contactos, buscar, linea + 8, True, PrimeraLinea, nombre)
        else:
            return BuscarContacto(Contactos, buscar, linea + 8, ExisteElContacto, PrimeraLinea,nombre)

#------------------------------------------------------------------------------------------------------------------------------------------ 
"""
Nombre: BuscarPorLugarDeTrabajo()
Entrada:
    lugar = lugar de trabajo del contacto que desea buscar.
Salidas:
    Retorna el o los contactos al que pertence que trabaja en ese lugar
Retricciones:
    Que lugar cumpliera las restricciones dadas en su función madre *agregarContacto()*
""" 
def BuscarPorLugarDeTrabajo():
    lugar=input("Dígite el lugar de trabajo del contacto que desea buscar: ")
    Contactos=ListaDeContactos()
    BuscarContacto(Contactos,lugar,6,False,6,"lugar de trabajo")#Busca el contacto solicitado y retorna la información del mismo.
    return BúsquedasAvanzadas()

#------------------------------------------------------------------------------------------------------------------------------------------ 
"""
Nombre: BuscarPorCorreo()
Entrada:
    correo = correo electrónico del contacto que desea buscar.
Salidas:
    Retorna el o los contactos al que pertence el correo electrónico.
Retricciones:
    Que correo cumpliera las restricciones dadas en su función madre *agregarContacto()*
""" 
def BuscarPorCorreo():
    correo=input("Dígite el correo electrónico del contacto que desea buscar: ")
    Contactos=ListaDeContactos()
    BuscarContacto(Contactos,correo,5,False,5,"correo")#Busca el contacto solicitado y retorna la información del mismo.
    return BúsquedasAvanzadas()

#------------------------------------------------------------------------------------------------------------------------------------------ 

AgendaDeContactos()
