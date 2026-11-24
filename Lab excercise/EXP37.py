# Recommendation System using Collaborative Filtering

ratings = {
    'A': {'Movie1': 5, 'Movie2': 3, 'Movie3': 0},
    'B': {'Movie1': 4, 'Movie2': 5, 'Movie3': 4},
    'C': {'Movie1': 1, 'Movie2': 2, 'Movie3': 5}
}

user = 'A'

# Find recommendations
recommendations = {}

for other in ratings:
    if other != user:
        for movie, rating in ratings[other].items():
            if ratings[user][movie] == 0 and rating > 0:
                recommendations[movie] = rating

if recommendations:
    best = max(recommendations, key=recommendations.get)
    print("Recommended Movie:", best)
else:
    print("No recommendations available")