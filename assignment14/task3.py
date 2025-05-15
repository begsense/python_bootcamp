book1 = {
    "სათაური": "ოსტატი და მარგარიტა",
    "ავტორი": "ბულგაკოვი",
    "წელი": 1967
}
book2 = {
    "სათაური": "1984",
    "ავტორი": "ორუელი",
    "წელი": 1949
}
book3 = {
    "სათაური": "მარტოობა",
    "ავტორი": "კამიუ",
    "წელი": 1942
}

books = [book1, book2, book3]
filtered_books = [book for book in books if book["წელი"] > 1950]
print("Filtered books:", filtered_books)


for book in books:
    book["ჟანრი"] = "ფანტასტიკა"