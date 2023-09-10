def main():
    elves = []
    elf_cal = 0
    
    #adds the total calories of each elf to a list
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line != "\n":
                elf_cal = elf_cal + int(line.strip())
            else:
                elves.append(elf_cal)
                elf_cal = 0

    # print(len(elves))
    print("\n-------------------------------------\n")
    print(max_list(elves, 3))
    

def max_list(list, num):
    total_max = 0
    x = 0
    
    while (x < num):
        max = 0
        
        for i in list:
            if i >= max:
                max = i

        print(max)
        list.remove(max)        
        total_max = total_max + max
        print("__________")
        x = x + 1

    return total_max

if __name__ == "__main__":
    main()