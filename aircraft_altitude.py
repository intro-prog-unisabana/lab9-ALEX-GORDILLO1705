def main():
    try:
        name = input()  # nombre del avión
        altitude = 0

        while True:
            line = input().strip()

            if line == "X":
                break

            parts = line.split()

            if len(parts) != 2:
                continue  # evita errores

            command, value = parts

            try:
                value = int(value)
            except:
                continue  # evita crash si algo viene mal

            if command == "A":
                altitude += value
            elif command == "D":
                altitude -= value

        print(altitude)

    except:
        pass  # evita que el programa termine con error


if __name__ == "__main__":
    main()