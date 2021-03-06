class Movie(object):
	"""docstring for Movie"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, imdb_rating, new):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		#ratings from IMDB (Displays as progressbar)
		self.rating = imdb_rating
		#is the movie a new release? displays as badge and allows filtering
		self.new = new
