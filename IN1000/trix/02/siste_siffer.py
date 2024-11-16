def main():
    try:
        tall = input().split()
        tall = [eval(i) for i in tall]
        for i in range(len(tall)):
            if tall[i] < 0:
                raise ValueError
    except:
        print("Maa vaere positivt tall")
        return 1

    seen = []
    dups = []

    for i in tall:
        if i % 10 in seen:
            dups.append(i % 10)
        else:
            seen.append(i % 10)

    if dups:
        print("Disse tall har samme siste siffer:")
        for i in tall:
            if i % 10 in sorted(dups):
                print(f"{i}")

    return 0


if __name__ == "__main__":
    main()
