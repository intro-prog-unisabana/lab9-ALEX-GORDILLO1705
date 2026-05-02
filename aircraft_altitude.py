from aircraft import Aircraft

model = input()
aircraft = Aircraft(model)

while True:
    try:
        command = input()
    except EOFError:
        break

    if command == "X":
        break

    parts = command.split()

    if len(parts) < 2:
        continue

    action = parts[0]
    value = int(parts[1])

    if action == "A":
        aircraft.ascend(value)
    elif action == "D":
        aircraft.descend(value)

print(f"Final altitude: {aircraft.altitude} feet")