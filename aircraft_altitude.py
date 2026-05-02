from aircraft import Aircraft

try:
    model = input()
except EOFError:
    model = ""

aircraft = Aircraft(model)

while True:
    try:
        command = input()
    except EOFError:
        break

    if command == "X":
        break

    parts = command.split()

    if len(parts) != 2:
        continue

    action, value = parts[0], parts[1]

    try:
        value = int(value)
    except:
        continue

    if action == "A":
        aircraft.ascend(value)
    elif action == "D":
        aircraft.descend(value)

print(f"Final altitude: {aircraft.altitude} feet")