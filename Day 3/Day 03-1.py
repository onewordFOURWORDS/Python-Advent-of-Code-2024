import re

def main():
    test = False

    if test:
        inst = open("Day 3/test.txt", "r")
    else:
        inst = open("Day 3/instructions.txt", "r")

    valid = []
    for line in inst:
        pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
        results = re.findall(pattern, line)
        
        valid.extend(results)

    print("Number of valid operations found:", len(valid))

    result = 0
    
    counter = 0
    for operation in valid:
        counter += 1
        nums = operation.strip("mul()").split(",")
        math = (int(nums[0]) * int(nums[1]))
        result += math

    print(result)

if __name__ == "__main__":
    main()