nCards = 1

while nCards > 0:
    nCards = int(input())
    cardsStack = [i for i in range(1, nCards + 1)]
    disCards = []

    while len(cardsStack) >= 2:
        disCard, baseCard = cardsStack.pop(0), cardsStack.pop(0)
        disCards.append(disCard)
        cardsStack.append(baseCard)

    if nCards > 0:
        print("Discarded cards:", end = "")
        toText = ", ".join([str(num) for num in disCards])
        print(f" {toText}" if len(disCards) else "") 
        print(f"Remaining card: {cardsStack[0]}")
