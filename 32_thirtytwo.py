'''

Aman and Jasbeer are very intelligent guys of their class.
Today they are playing a game of numbers.

Game rules: 
They will make their moves alternatively,
In one move, they can perform the following operations:
1. A player will choose a number from the table, and will replace that number with one of its divisors/
For example, 6 can be replaced with 1,2 or 3.
2. It is mandatory that the player has replaced the number. 
3. A player cannot put back the name number on the table.
4. As 1 does not have any divisor other than tself, a player cannot replace 1 with another number.
Soon a situtaion will arise when there will be only all 1s on the table.
In that situtaion, a playe will not be able to make any moves.
The player who will not be able to make any moves, loses.
5. Both the players are masters of this game so they will play the game optimally. 
6. Aman will make the first move of the game.
As you will be given the n integers that are on the table, you have to predict who will win the match.
Aman or Jasbeer?

Test case 1:
I/P: 1 6
O/P: Aman

Test case 2:     
I/P: 2 18 6
O/P: Aman

Test case 3:
I/P: 4 
24 45 45 24
O/P: Jasbeer


'''

n = int(input())
f = [int(x) for x in (input().split())]
