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

    num_counts = {}
    for i in range(len(list2)):
        if num_counts.get(list2[i]) != None:
            num_counts[list2[i]] += 1
        else:
            num_counts[list2[i]] = 1

    counter = 0
    for i in range(len(list1)):
        if num_counts.get(list1[i]) != None:
            counter += list1[i] * num_counts.get(list1[i])
        else:
            continue

    print(counter)

main()