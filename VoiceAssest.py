import pywhatkit
command = input(">")
command_lower = command.lower()
if "open" in command_lower:
  search = command.replace("open ", "")
  try:
     pywhatkit.search(search)
     print("Searching " + search)
  except:
     print("An unknown error occured")
else:
   print(f"I don't understand what is ({command}).\n Please type help for commands.")