from api.config import ia

def get_movie_by_id(movie_id):
    """
    Read one movie data
    """
    movie = ia.get_movie(movie_id)
    output = {}
    output['movie_id'] = movie.movieID
    output['title'] = movie.get('title')
    output['cast'] = []
    for m in movie['cast']:
        output['cast'].append(m['name'])

    return output

def get_movie_by_name(movie_name):
    """
    Read one movie data
    """
    movie = ia.search_movie_advanced(movie_name, adult=True)[0]
    output = {}
    output['movie_id'] = movie.movieID
    output['title'] = movie.get('title')
    output['cast'] = []
    for m in movie['cast']:
        output['cast'].append(m['name'])

    return output