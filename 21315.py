import math

N = int(input())
mixedCards = list(map(int,input().split()))
initCards = [(x+1)for x in range(N)]
k_max=1
for x in range(1,11):
    if math.pow(2,x)>=N:
        k_max=x-1
        break
def mixCard(cards, k):
    two_k = int(math.pow(2,k))
    tempCard = cards[len(cards)-two_k:]
    remainCard = cards[:len(cards)-two_k]
    if k == 0:
        return tempCard + remainCard
    else:
        return mixCard(tempCard,k-1)+remainCard

for x in range(1,k_max+1):
    cards = mixCard(initCards,x)
    print(cards)
    for y in range(1,k_max+1):
        cards_tmp = mixCard(cards,y)
        print(cards_tmp)
        if(cards_tmp == mixedCards):
            print(x,y)
            break