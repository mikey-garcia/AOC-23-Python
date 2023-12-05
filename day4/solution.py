def part1(cases):
    import math
    part1=0
    for hand_string in cases:
        matches=0
        lhs, rhs = hand_string.split("|")
        winning_cards =[ int(i) for i in lhs.split(":")[1].split(" ")[1::] if i!='' ]
        hand =[ int(i) for i in rhs.split(" ") if i!='' ]

        for number in hand:
            if number in winning_cards:
                matches+=1

        handscore = 2**(matches-1)
        part1+=math.floor(handscore) # whoops i included 2^-1 and am too lazy to change it
    return part1

def part2(cases):
    save = []
    CARDS = []
    for i,hand_string in enumerate(cases):
        lhs, rhs = hand_string.split("|")
        winning_cards =[ int(i) for i in lhs.split(":")[1].split(" ")[1::] if i!='' ]
        hand =[ int(i) for i in rhs.split(" ") if i!='' ]
        save.append((i+1,winning_cards,hand))
        CARDS.append(1)

    for card, winning_cards, hand in save:
        matches=0
        for number in hand:
            if number in winning_cards:
                CARDS[card+1+matches]+= CARDS[card]
                matches+=1
    return sum(CARDS)
