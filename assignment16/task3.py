# როგორც დავარესერჩე კლასია შესაქმნელი, რომელის იქნება კონტექსტ მენეჯერის პროტოკოლის მიმღები და ექნება ენტერ/ეგზით ფუნქციები.
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to the database...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing the database connection...")

with DatabaseConnection():
    print("Performing database operations")

# როცა კონტექსტ მენეჯერის კოდის ბლოკი დასრულდება ავტომატურად exit იძახებს და ბაზასთან კავშირი მთავრდება