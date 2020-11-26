class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = deque(), deque()
        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(max(radiant[-1], dire[-1]) + 1)
            else:
                dire.append(max(radiant[-1], dire[-1]) + 1)
            radiant.popleft()
            dire.popleft()
        return "Radiant" if radiant else "Dire"
