# Write your code here!
# FREEZE CODE BEGIN
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"


if __name__ == "__main__":
    title = input()
    director = input()
    year = input()

    movie = Movie(title, director, year)
    print(movie)