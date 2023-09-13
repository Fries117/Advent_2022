# A X   Rock
# B Y   Paper
# C Z   Scissors
def main():
    list = []
    total = 0

    with open("RPS_doc.txt") as f:
        while True:
            line = f.readline()
            list.append(line.strip().split())
            if not line:
                break
    list.pop()
    for i in range(len(list)):
        for j in range(2):
            if list[i][1] == "X":
                if list[i][0] == "A":
                    list[i][1] = "C"
                elif list[i][0] == "B":
                    list[i][1] = "A"
                elif list[i][0] == "C":
                    list[i][1] = "B"

            elif list[i][1] == "Y":
                list[i][1] = list[i][0]

            if list[i][1] == "Z":
                if list[i][0] == "A":
                    list[i][1] = "B"
                elif list[i][0] == "B":
                    list[i][1] = "C"
                elif list[i][0] == "C":
                    list[i][1] = "A"
        
    # print(list)
    for i in range(len(list)):
        if list[i][0] == list[i][1]:
            total = total + (3 + rpsPoints(list[i][1]))
        elif list[i][0] == "A":
            if list[i][1] == "B":
                total = total + (6 + rpsPoints(list[i][1]))
            else:
                total = total + (0 + rpsPoints(list[i][1]))
        elif list[i][0] == "B":
            if list[i][1] == "C":
                total = total + (6 + rpsPoints(list[i][1]))
            else:
                total = total + (0 + rpsPoints(list[i][1]))
        elif list[i][0] == "C":
            if list[i][1] == "A":
                total = total + (6 + rpsPoints(list[i][1]))
            else:
                total = total + (0 + rpsPoints(list[i][1]))
        print(total)

        
def rpsPoints(choice):
    points = 0
    if choice == "A":
        points = 1
    elif choice == "B":
        points = 2
    else:
        points = 3
    return points    


if __name__ == "__main__":
    main()