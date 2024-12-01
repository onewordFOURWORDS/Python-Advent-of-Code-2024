def main():
    numbers = open("numbers.txt", "r")

    list1 = []
    list2 = []
    for line in numbers:
        split = line.split("   ")

        list1.append(int(split[0]))
        list2.append(int(split[1]))

    list1.sort()
    list2.sort()

    counter = 0
    for i in range(len(list1)):
        counter += abs(list1[i] - list2[i])

    print(counter)

main()