def personal_message(name,language):
    print(f"Hello {name.title()}, would you like to learn some {language.lower()} today?")
    return

personal_message("eric","Python")

def quote_author(quote,author):
    print(f'{author} once said, "{quote}"')
    message = f'{author} once said, "{quote}"'
    print(message)
    return
quote_author("Our lives begin to end the day we become silent about things that matter." , "Martin Luther King Jr.")

def stripping_names(name):
    name = f"\n\t{name}"
    print("""
          Original: %s
          Using lstrip (Remove whitespace at the begin of the string): %s
          Using rstrip (Remove whitespace at the end of the string): %s
          Using strip (Remove whitespace from both sides): %s
          """%(name,name.lstrip(),name.rstrip(),name.strip()))

stripping_names(" Mishell ")