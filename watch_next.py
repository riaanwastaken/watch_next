import spacy



def find_next_movie(movie_description, movies):
    """
    Given a movie description and a dictionary of movies, this function returns 
    the title of the most similar movie.

    Args:
        movie_description: A string containing the description of a movie.
        movies: A dictionary containing the titles and descriptions of movies.

    Returns:
        A string containing the title of the most similar movie.
    """
    highest_similarity_score = 0
    nlp = spacy.load('en_core_web_md')
    descriptive_token = nlp(movie_description)
    for title, description in movies.items():
        token = nlp(description)
        similarity_score = descriptive_token.similarity(token)
        if similarity_score > highest_similarity_score:
            highest_similarity_score = similarity_score
            movie = title
    return f"{movie} with a score of:({highest_similarity_score:.2f})"



# Input arguments
movie_description = """Will he save their world or destroy it? When the Hulk 
becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle 
and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and 
trained as a gladiator."""

movies = {}
with open('movies.txt', 'r') as file:
    for line in file:
        title, description = line.strip().split(':', 1)
        movies[title] = description.strip()



# Running the function with input arguments
next_movie_calculated = find_next_movie(movie_description, movies)
print(f"Most similar movie: {next_movie_calculated}")


# End of program.