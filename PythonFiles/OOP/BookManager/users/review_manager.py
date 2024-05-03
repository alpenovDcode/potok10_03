class ReviewManager:
    def __init__(self):
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def display_reviews(self):
        for review in self.reviews:
            print(review)
