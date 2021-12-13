from datetime import datetime

now = datetime.now()

print("Date:", now.strftime("%A" + " %d" + "th" + " %B" + " %Y"))
print("Time:", now.strftime("%X"))