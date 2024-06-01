class UF3:
    def __init__(self):
        self.reps = []  # Now just 'immediate' representative.
        self.rank = []  # The rank, i.e., length of longest chain below a representative
        self.groups = 0

    def make(self, n):
        self.reps = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.groups = n

    def find(self, x):
        while x != self.reps[x]:
            x = self.reps[x]
        return x

    def union(self, x, y):
        self.root_union(self.find(x), self.find(y))

    def size(self):
        return len(self.reps)

    def __str__(self):
        return "UF3" + str(self.reps)

    def root_union(self, x, y):  # x and y are known to be representatives
        if x == y:
            return
        self.groups -= 1
        if self.rank[x] > self.rank[y]:
            self.reps[y] = x
        elif self.rank[y] > self.rank[x]:
            self.reps[x] = y
        else:  # ranks are equal
            self.reps[x] = y
            self.rank[y] += 1

    def groups(self):
        return self.groups

    def name(self):
        return "UF3"