class Triangle5(object):
    def __init__(self, missing):
        # source, jumped, destination
        self.jumps = [(0, 1, 3),
                      (0, 2, 5),
                      (1, 3, 6),
                      (1, 4, 8),
                      (2, 4, 7),
                      (2, 5, 9),
                      (3, 1, 0),
                      (3, 4, 5),
                      (3, 6, 10),
                      (3, 7, 12),
                      (4, 7, 11),
                      (4, 8, 13),
                      (5, 2, 0),
                      (5, 4, 3),
                      (5, 8, 12),
                      (5, 9, 14),
                      (6, 3, 1),
                      (6, 7, 8),
                      (7, 4, 2),
                      (7, 8, 9),
                      (8, 4, 1),
                      (8, 7, 6),
                      (9, 5, 2),
                      (9, 8, 7),
                      (10, 6, 3),
                      (10, 11, 12),
                      (11, 7, 4),
                      (11, 12, 13),
                      (12, 7, 3),
                      (12, 8, 5),
                      (12, 11, 10),
                      (12, 13, 14),
                      (13, 8, 4),
                      (13, 12, 11),
                      (14, 9, 5),
                      (14, 13, 12)]

        self.pegs = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.pegs.remove(missing)
        self.moves_made = []
        self.won = False

    def can_move(self, move):
        return (move[0] in self.pegs and
                move[1] in self.pegs and
                move[2] not in self.pegs)

    def valid_moves(self):
        return filter(self.can_move, self.jumps)

    def make_move(self, move):
        if self.can_move(move):
            self.pegs.remove(move[0])
            self.pegs.remove(move[1])
            self.pegs.add(move[2])
            self.moves_made.append(move)

    def undo(self):
        move = self.moves_made.pop()
        self.pegs.add(move[0])
        self.pegs.add(move[1])
        self.pegs.discard(move[2])

    def solve(self):
        if self.won:
            return
        for move in self.valid_moves():
            self.make_move(move)
            if len(self.pegs) == 1:
                print(self.moves_made)
                self.won = True
            self.solve()
            self.undo()

    def val(self, n):
        return "x " if n in self.pegs else "- "

    def __str__(self):
        return ("     " + self.val(0) + "\n    " +
                self.val(1) + self.val(2) + "\n   " +
                self.val(3) + self.val(4) + self.val(5) + "\n  " +
                self.val(6) + self.val(7) + self.val(8) + self.val(9) + "\n " +
                self.val(10) + self.val(11) + self.val(12) + self.val(13) + self.val(14))


for i in range(0, 5):
    t = Triangle5(i)
    print("Solution for start " + str(i))
    t.solve()