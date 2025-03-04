#Mishell Arroyo 04/03/2025
def personal_message(name,language):
    #Se imprime la variable name en su forma gramaticalmente correcta (Mayusculas al principio) y "language" se imprime en minúscula
    print(f"Hello {name.title()}, would you like to learn some {language.lower()} today?")
    return

personal_message("eric","Python") #Output: Hello Eric, would you like to learn some python today?

def quote_author(quote,author):
    #Se imprime el nombre del autor y su cita en una sola línea
    print(f'{author} once said, "{quote}"')
    # Igualmente see puede guardar en una variable 
    message = f'{author} once said, "{quote}"'
    print(message)
    return
quote_author("Our lives begin to end the day we become silent about things that matter." , "Martin Luther King Jr.")

def stripping_names(name):
    #En la variable "name" se esta agregando un salto de lina y un espacio en blanco con el fin de aplicar métodos
    name = f"\n\t{name}"
    # Se aplica el metodo .lstrip(), .rstrip(), .strip() para quitar espacios en la izquierda, derecha y ambos lados, respectivamente.
    print("""
          Original: %s
          Using lstrip (Remove whitespace at the begin of the string): %s
          Using rstrip (Remove whitespace at the end of the string): %s
          Using strip (Remove whitespace from both sides): %s
          """%(name,name.lstrip(),name.rstrip(),name.strip()))

stripping_names(" Mishell ")