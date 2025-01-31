

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#task 1
def above(movie):
    return movie["imdb"] > 5.5
print(above(movies[0]))

#task 2
def sublist(movies):
    return[movie for movie in movies if movie["imdb"] > 5.5]

print(sublist(movies))

#task 3
def cate(movies , category):
    return [movie for movie in movies if movie["category"] == category]
print(cate(movies , "Romance"))

#task 4
def average(movies):
    score = sum(movie["imdb"] for movie in movies)
    return score / len(movies)
print(average(movies))

#task 5
def cateave(movies , category):
    score = sum(movie["imdb"] for movie in movies if movie["category"] == category)
    catecount = sum(1 for movie in movies if movie["category"] == category)
    return score / catecount
print(cateave(movies , "Thriller"))

