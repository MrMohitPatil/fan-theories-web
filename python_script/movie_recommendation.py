import random

# Dictionary of movie recommendations
movie_recommendations = {
    "The Shawshank Redemption": ["The Green Mile", "The Godfather", "Pulp Fiction", "The Dark Knight"],
    "Inception": ["Interstellar", "Shutter Island", "The Matrix", "Fight Club"],
    "Forrest Gump": ["The Pursuit of Happyness", "The Curious Case of Benjamin Button", "Cast Away"],
    # Add more movies and their recommendations here
}

def recommend_movies(fav_movies):
    recommended_movies = []
    for movie in fav_movies:
        if movie in movie_recommendations:
            recommended_movies.extend(movie_recommendations[movie])
    # Remove duplicates from recommended movies
    recommended_movies = list(set(recommended_movies))
    # Remove user's favorite movies from recommendations
    recommended_movies = [movie for movie in recommended_movies if movie not in fav_movies]
    return recommended_movies

def main():
    print("Welcome to the Movie Recommendation Bot!")
    print("Please enter 2-3 of your favorite movies:")
    fav_movies = []
    while len(fav_movies) < 2 or len(fav_movies) > 3:
        fav_movies = input("Enter favorite movie(s) separated by comma: ").split(",")
        fav_movies = [movie.strip() for movie in fav_movies]
        if len(fav_movies) < 2 or len(fav_movies) > 3:
            print("Please enter 2-3 favorite movies.")

    recommended_movies = recommend_movies(fav_movies)
    if recommended_movies:
        print("\nBased on your favorites, I recommend you watch:")
        for movie in random.sample(recommended_movies, min(5, len(recommended_movies))):
            print("-", movie)
    else:
        print("\nSorry, we couldn't find recommendations based on your favorites.")

if __name__ == "__main__":
    main()
