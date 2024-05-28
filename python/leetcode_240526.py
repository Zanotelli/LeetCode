# OBS
# O método 1 foi a solução mais intuitiva encontrada, mas teve uma desempenho
# mediano em velocidade e memória em relação aos outros envios.
# O método 2 é mais complexo e complexo, porem tem um tempo de execução terrível,
# mas um uso de memória excelente.


#Método 1
class Solution:

    MOD = 0
    MEMO = [[[]]]

    def checkRecord(self, n: int) -> int:
        self.MOD = 1000000007
        self.MEMO = [[[None] * 3 for _ in range(2)] for _ in range(n+1)]
        return self.verify_record(n, 0, 0)

    def verify_record(self, n: int, total_a: int, late_streak: int):

        if total_a >= 2 or late_streak >= 3:
            return 0
        if n == 0:
            return 1
        if self.MEMO[n][total_a][late_streak] is not None:
            return self.MEMO[n][total_a][late_streak]

        valid_combinations = self.verify_record(n-1, total_a, 0)                        #P
        valid_combinations = (valid_combinations + self.verify_record(n-1, total_a + 1, 0)) % self.MOD        #A
        valid_combinations = (valid_combinations + self.verify_record(n-1, total_a, late_streak + 1)) % self.MOD  #L
        self.MEMO[n][total_a][late_streak] = valid_combinations

        return valid_combinations

# Método 2

class Solution:

    MOD = 0
    MEMO_CURR = [[]]
    MEMO_NEXT = [[]]

    def checkRecord(self, n: int) -> int:
        self.MOD = 1000000007
        self.MEMO_CURR = [[0] * 3 for _ in range(2)]
        self.MEMO_NEXT = [[0] * 3 for _ in range(2)]
        self.MEMO_CURR[0][0] = 1
        return self.verify_record(n)

    def verify_record(self, n: int) -> int:
        count = 0
        for _ in range(n):
            for absences in range(2):
                for late in range(3):
                    self.MEMO_NEXT[absences][0] = (self.MEMO_NEXT[absences][0] + self.MEMO_CURR[absences][late]) % self.MOD
                    if absences < 1:
                        self.MEMO_NEXT[absences+1][0] = (self.MEMO_NEXT[absences+1][0] + self.MEMO_CURR[absences][late]) % self.MOD
                    if late < 2:
                        self.MEMO_NEXT[absences][late+1] = (self.MEMO_NEXT[absences][late+1] + self.MEMO_CURR[absences][late]) % self.MOD
            self.MEMO_CURR = self.MEMO_NEXT[:][:]
            self.MEMO_NEXT = [[0] * 3 for _ in range(2)]
            count = sum(sum(line) for line in self.MEMO_CURR) % self.MOD
        return count


print(Solution().checkRecord(2))
#183236316




