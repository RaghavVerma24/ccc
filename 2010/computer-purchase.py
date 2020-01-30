n = int(input())

if n == 1:
    name, _, _, _ = input().split()
    print(name)
elif n != 0:

    first = -1
    second = -2

    a = ""
    b = ""

    for i in range(n):
        name, ram, cpu, disk = input().split()

        ram = int(ram)
        cpu = int(cpu)
        disk = int(disk)

        score = 2 * ram + 3 * cpu + disk

        if score > first:
            second = first
            first = score

            b = a
            a = name
        elif score == first:
            if name < a:
                second = first
                first = score

                b = a
                a = name
            else:
                second = score
                b = name
        elif score > second:
            second = score
            b = name
        elif score == second:
            if score < b:
                second = score
                b = name

    print(a)
    print(b)
