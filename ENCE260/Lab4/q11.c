#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef enum {
    HEARTS,
    DIAMONDS,
    SPADES,
    CLUBS
} Suit_t;

typedef enum {
    ACE = 1,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    EIGHT,
    NINE,
    TEN,
    JACK,
    QUEEN,
    KING
} Rank_t;

typedef struct {
    Rank_t rank;
    Suit_t suit;
} Card_t;

Card_t makeCard(Rank_t rank, Suit_t suit)
{
    Card_t card = {rank, suit};
    return card;
}

bool isSnap(Card_t card1, Card_t card2)
{
    return card1.rank == card2.rank;
}

bool isTrump(Card_t card, Suit_t trumpSuit)
{
    return card.suit == trumpSuit;
}

int main(){
    Card_t card1 = makeCard(THREE, CLUBS);
    Card_t card2 = makeCard(SEVEN, DIAMONDS);
    Card_t card3 = makeCard(THREE, HEARTS);
    puts(isSnap(card1, card2) ? "Snap!" : "No snap");
    puts(isSnap(card1, card3) ? "Snap!" : "No snap");
    puts(isTrump(card3, HEARTS) ? "Trump!" : "No Trump");
}