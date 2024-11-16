import sys

def main(argv):
    if len(argv) == 2:
        try:
            temp = float(argv[1])
        except:
            print("Not a valid temperature")
            return 2
    else:
        print("Invalid arguments")
        return 1

    if temp > 36.5 and temp < 37.5:
        print("Within normal body temperature")
    elif temp < 36.5:
        print("Below normal body temperature")
    else:
        print("Above normal body temperature")
    
    return 0

if __name__ == "__main__":
    main(sys.argv)
