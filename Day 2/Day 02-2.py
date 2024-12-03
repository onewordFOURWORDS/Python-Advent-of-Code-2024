def check_direction(line): 
    pairs = zip(line, line[1:]) # thanks Geeks4Geeks for this

    inc = all(a < b for a, b in pairs)
    

    
            

def test_pair(a:int, b:int, increasing:bool):
    # Test that pair matches direction
    if increasing == True:



    return

def main():
    test = True

    if test:
        data = open("Day 2/test.txt", "r")
    else:
        data = open("Day 2/levels.txt", "r")

    for line in data:
        line = line.strip().split()
        line = [int(x) for x in list] # ooh a one liner im so fancy
        
        direction = check_direction(line)
        
        for reading in range(len(line) - 1):
            a = line[reading]
            b = line[reading]

            result = test_pair(a, b, increasing)


        



    # unsafe = 0
    # for line in data:
    #     line = line.strip()
    #     level = line.split(" ")
    #     flag = ""
    #     line_counter += 1
    #     bad_levels = 0
        

    #     for pos in range(len(level) - 1):
    #         a = int(level[pos])
    #         b = int(level[pos + 1])

    #         test_pair(a, b, flag)

    #     if bad_levels > 1:
    #         unsafe += 1
            
    # safe = line_counter - unsafe
    # print("The number of safe values is: ", safe)
            

if __name__ == "__main__":
    main()