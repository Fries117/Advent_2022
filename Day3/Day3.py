def main():
    num = 0

    with open("Input.txt") as f:
        while True:

            line = f.readline()
            half1 = line[:len(line)//2]
            half2 = line[len(line)//2:]
            
            if not line:
                break

            for x in range(len(half1)):
                if(half2.find(half1[x]) != -1):
                    num = num + priNum(half1[x])
                    # print(half1[x])
                    print(num)
                    break
        

def priNum(item):
    unic = ord(item)
    pri_num = 0
    
    if(unic >= 97 and unic <=122):
        pri_num = unic - 96
    elif(unic >= 65 and unic <= 90):
        pri_num = unic - 38
    
    return pri_num

if __name__ == "__main__":
    main()