def les(file_name):
    file = open(file_name, "r")
    info = {}
    cnt = 0
    for line in file:
        if cnt == 0:
            names = line.strip("\n").split(",")
            cnt += 1
            pass
        else:
            hours = line.strip("\n").split(",")
            for i in range(len(hours)):
                if names[i] in info:
                    info[names[i]].append(int(hours[i]))
                else:
                    info[names[i]] = [int(hours[i])]
    file.close()
    return info 


def combine(dict1, dict2):
    remove = set()
    rem = False
    for name in dict2:
        if name in dict1:
            for i in range(len(dict2[name])):
                dict1[name][i] += dict2[name][i]
                remove.add(name)
                rem = True

    if rem:
        for name in remove:
            dict2.pop(name)

    dict1.update(dict2)
    return dict1


def writefile(info, file_name):
    file = open(file_name, "w")

    names = list(info.keys())
    file.write(",".join(names) + "\n")
    
    for i in range(len(info["Anna"])):
        line = []
        for value in info:
            line.append(str(info[value][i]))
        file.write(",".join(line) + "\n")

    file.close()


def main():
    file1 = "timeliste1.txt"
    file2 = "timeliste2.txt"
    file_write = "timeliste3.txt"
    dict1 = les(file1)
    dict2 = les(file2)
    combined = combine(dict1, dict2)
    writefile(combined, file_write)


if __name__ == "__main__":
    main()
