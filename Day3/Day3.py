def main():
    num = 0
    count_flag = 0
    line_list = []

    with open("Input.txt") as f:
        while True:

            count_flag += 1
            line = f.readline()
            line_list.append(line)
            
            if not line:
                break
            
            if(count_flag % 3 == 0):
                print(line_list)

                for x in range(len(line_list[0])):
                    if(line_list[1].find(line_list[0][x]) != -1  and line_list[2].find(line_list[0][x]) != -1):
                        print(line_list[0][x])
                        num+= priNum(line_list[0][x])
                        break

                line_list.clear()
                print(num)
        

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