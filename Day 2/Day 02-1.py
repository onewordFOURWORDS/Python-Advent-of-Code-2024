def main():
    test = False

    if test:
        data = open("Day 2/test.txt", "r")
    else:
        data = open("Day 2/levels.txt", "r")

    unsafe = 0
    counter = 0
    for line in data:
        level = line.split(" ")
        flag = ""
        counter += 1

        for pos in range(len(level) - 1):
            a = int(level[pos])
            b = int(level[pos + 1])

            if a == b: # Level MUST increase or decrease or it is unsafe
                unsafe += 1
                break

            if abs(a - b) > 3: # Check difference between positions, if over 3 level unsafe
                unsafe += 1
                break

            if b > a:
                if flag == "-": 
                    unsafe += 1
                    break
                elif flag == "+":
                    continue
                else: # if increasing flag isn't set set it
                    flag = "+"

            if b < a:
                if flag == "+": 
                    unsafe += 1
                    break
                elif flag == "-":
                    continue
                else: # if decreasing flag isn't set set it
                    flag = "-"
            
    safe = counter - unsafe
    print("The number of safe values is: ", safe)
            

if __name__ == "__main__":
    main()