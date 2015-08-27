"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
from __future__ import print_function, division
from Card import *


class PokerHand(Hand):
    labels = ["Royal Flush", "Straight Flush", "Four Of A Kind", "Full House","Flush",
              "Straight", "Three Of A Kind", "Two Pair", "Pair", "Highest Card"]

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        if hasattr(self, 'suits'):
            return
        self.suits = {}
        self.ranks = {}
        for card in self.cards:
            self.suits[card.suit] = sorted(self.suits.get(card.suit, []) + [card.rank])
            self.ranks[card.rank] = sorted(self.ranks.get(card.rank, []) + [card.suit])

    @staticmethod
    def is_seq(inp_lst):
        clone_list = list(inp_lst)
        if clone_list[0] == 1:
            clone_list += [14]
        for i in range(len(clone_list)-1):
            if clone_list[i+1] - clone_list[i] != 1:
                if i >= 4:
                    return True, clone_list[i]
                elif i+5 >= len(clone_list):
                    return False, None
        return True, clone_list[-1]

    def has_straight_flush(self):
        self.suit_hist()
        for suit, ranks in self.suits.iteritems():
            if len(ranks) >= 5:
                is_straight, largest = PokerHand.is_seq(ranks)
                if is_straight:
                    return True, largest
        return False, None

    def has_four_of_kind(self):
        self.suit_hist()
        for rank in sorted(self.ranks.keys(), reverse=True):
            if len(self.ranks[rank]) == 4:
                return True
        return False

    def has_full_house(self):
        self.suit_hist()
        has_3 = has_2 = False
        for rank in sorted(self.ranks.keys(), reverse=True):
            if len(self.ranks[rank]) == 3:
                has_3 = True
            elif len(self.ranks[rank]) == 2:
                has_2 = True
        return has_3 and has_2

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for ranks in self.suits.values():
            if len(ranks) >= 5:
                return True
        return False

    def has_straight(self):
        self.suit_hist()
        return PokerHand.is_seq(self.ranks.keys())[0]

    def has_three_of_kind(self):
        self.suit_hist()
        for rank in sorted(self.ranks.keys(), reverse=True):
            if len(self.ranks[rank]) >= 3:
                return True
        return False

    def has_two_pair(self):
        self.suit_hist()
        count = 0
        for rank in sorted(self.ranks.keys(), reverse=True):
            if len(self.ranks[rank]) >= 2:
                count += 1
        return count >= 2

    def has_pair(self):
        self.suit_hist()
        for rank in sorted(self.ranks.keys(), reverse=True):
            if len(self.ranks[rank]) >= 2:
                return True
        return False

    def classify(self):
        is_straight_flush, largest = self.has_straight_flush()
        if is_straight_flush and largest == 14:
            label = "Royal Flush"
        elif is_straight_flush:
            label = "Straight Flush"
        elif self.has_four_of_kind():
            label = "Four Of A Kind"
        elif self.has_full_house():
            label = "Full House"
        elif self.has_flush():
            label = "Flush"
        elif self.has_straight():
            label = "Straight"
        elif self.has_three_of_kind():
            label = "Three Of A Kind"
        elif self.has_two_pair():
            label = "Two Pair"
        elif self.has_pair():
            label = "Pair"
        else:
            label = "Highest Card"
        self.label = label


def deal(cards=7, num_hands=7):
    deck = Deck()
    deck.shuffle()
    hands = []
    for _ in range(num_hands):
        hand = PokerHand()
        deck.move_cards(hand, cards)
        hand.sort()
        hand.classify()
        hands.append(hand)
    return hands


def estimate_probability(cards, num_hands, repeats=1000):
    counts = {}
    for _ in range(repeats):
        hands = deal(cards, num_hands)
        for hand in hands:
            counts[hand.label] = counts.get(hand.label, 0) + 1
    total = num_hands * repeats
    for label in PokerHand.labels:
        count = counts.get(label, 0)
        prob = count / total
        print("Probability of '%s' is %f " % (label, prob))


if __name__ == '__main__':
    estimate_probability(7, 7, 1000)

