from aircraft import Aircraft

def main():
    model = input()
    aircraft = Aircraft(model)

    while True:
        command = input()

        if command == "X":
            break

        parts = command.split()
        action = parts[0]
        value = int(parts[1])

        if action == "A":
            aircraft.ascend(value)
        elif action == "D":
            aircraft.descend(value)

    print(f"Final altitude: {aircraft.altitude} feet")


if __name__ == "__main__":
    main()