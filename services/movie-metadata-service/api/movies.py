from api.config import ia

def list_movies(movie_name):
    """
    Get list of movies by name with ID
    """
    movies = ia.search_movie_advanced(movie_name, adult=True)
    output = {}
    output['movies'] = []
    
    for movie in movies:
        m = {}
        m['movie_id'] = movie.movieID
        m['title'] = movie.get('title')
        output['movies'].append(m)

    return output