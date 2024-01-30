class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        # n = len(player1) = len(player2)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        player1_score = 0
        player2_score = 0

        p1_count = 0
        p2_count = 0

        for score1, score2 in zip(player1, player2):
            player1_score += score1 if not p1_count else score1 * 2
            player2_score += score2 if not p2_count else score2 * 2

            if p1_count:
                p1_count -= 1

            if p2_count:
                p2_count -= 1

            if score1 == 10:
                p1_count = 2

            if score2 == 10:
                p2_count = 2

        if player1_score > player2_score:
            return 1
        elif player1_score == player2_score:
            return 0
        else:
            return 2