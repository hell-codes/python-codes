#Function to insert a new rating in the correct position
def insert_rating(ratings, new_rating):
    
    i = len(ratings) - 1
    while i >= 0 and ratings[i] > new_rating:
        i -= 1

    ratings.insert(i + 1, new_rating)

ratings = [1.5, 2.0, 3.5, 4.0, 4.8]  
print("Current Ratings:", ratings)

new_rating = float(input("Enter new rating: "))

insert_rating(ratings, new_rating)

print("Updated Ratings:", ratings)
