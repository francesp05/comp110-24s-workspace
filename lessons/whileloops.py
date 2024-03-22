"""demonstrates while loops by finding low value in string"""

cards = str="5235"

card_idx: int = 0
#look at each number in string
low_card: int = int(cards[0])

while card_idx < 4:
    # print(cards[card_idx])
    # check if current card is less than low card
    current_card: int = int(cards[card_idx])
    if (current_card < low_card):
        low_card = current_card
    card_idx = card_idx + 1 #update variable so program prints out each element

print(low_card)

