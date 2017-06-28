input("Woah you want more math with your numbers? ")
i = int(input("Gimmie some more then: "))


def facts(i):
    if i == 0:
        return 1
    return i * facts(i - 1)

results = facts(i)
print("Here you go: ", facts(i))
