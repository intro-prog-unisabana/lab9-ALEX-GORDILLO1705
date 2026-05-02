def main():
    try:
        name = input()
        altitude = 0

        while True:
            line = input().strip()

            if line == "X":
                break

            parts = line.split()

            if len(parts) != 2:
                continue

            command, value = parts

            try:
                value = int(value)
            except:
                continue

            if command == "A":
                altitude += value
            elif command == "D":
                altitude -= value

        print(f"Final altitude: {altitude} feet")

    except:
        pass


if __name__ == "__main__":
    main()