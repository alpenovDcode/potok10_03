class Review:
    def __init__(self, book, rating, comment):
        self.book = book
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"Review for {self.book}: Rating - {self.rating}, Comment - {self.comment}"
