class Rank:
    def __init__(self, rank) -> None:
        self.rank = rank
        self.valid = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        self.check_invalid()
        self.value = self.valid.get(rank)

        
    def check_invalid(self):
        if self.rank not in self.valid:
            raise ValueError()
        
    def __eq__(self, other: object) -> bool:
        return self.value == other.value
    
    def __lt__(self, other: object) -> bool:
        return self.value< other.value
    
    def __gt__(self, other: object) -> bool:
        return self.value > other.value
    
    