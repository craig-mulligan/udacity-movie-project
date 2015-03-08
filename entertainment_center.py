import media
import movie_generator

toy_story = media.Movie("Toy Story", "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", "http://www.rotoscopers.com/wp-content/uploads/2013/10/Toy-Story-Poster.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio", 8.3, 'false')

avatar = media.Movie("avatar",	"A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world", "http://www.writingfordesigners.com/wp-content/uploads/2014/09/Avatar-Poster-blue-people.jpg", "https://www.youtube.com/watch?v=uA8SG4Yea7s", 7.9, 'false')

gone_girl = media.Movie("Gone Girl",	"With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent.", "http://s3-ec.buzzfed.com/static/2014-08/1/2/enhanced/webdr11/enhanced-buzz-wide-384-1406873867-8.jpg", "https://www.youtube.com/watch?v=esGn-xKFZdU", 8.3, 'true')

bird_man = media.Movie("Birdman",	"A washed up actor, who once played an iconic superhero, battles his ego and attempts to recover his family, his career and himself in the days leading up to the opening of a Broadway play.", "http://www.impawards.com/2014/thumbs/sq_birdman.jpg", "https://www.youtube.com/watch?v=uJfLoE6hanc", 8.2, 'true')

slumdog_millionare = media.Movie("Slumdog Millionaire",	"A Mumbai teen who grew up in the slums, becomes a contestant on the Indian version of 'Who Wants To Be A Millionaire?' He is arrested under suspicion of cheating, and while being interrogated, events from his life history are shown which explain why he knows the answers.", "https://www.movieposter.com/posters/archive/main/110/MPW-55462", "https://www.youtube.com/watch?v=kuSTr48P9mc", 8.0, 'false')

butch_cassidy_and_the_sundance_kid = media.Movie("Butch Cassidy and the Sundance Kid",	"Two Western bank/train robbers flee to Bolivia when the law gets too close.", "http://www.impawards.com/1969/posters/butch_cassidy_and_the_sundance_kid.jpg", "https://www.youtube.com/watch?v=501Afs54cso", 8.2, 'false')

saving_christmas = media.Movie("Saving Christmas",	"Kirk is enjoying the annual Christmas party extravaganza thrown by his sister until he realizes he needs to help out Christian, his brother-in-law who has a bad case of the bah-humbugs.", "http://www.impawards.com/2014/thumbs/sq_saving_christmas.jpg", "https://www.youtube.com/watch?v=z5-yA66kaVc", 1.5, 'false')

# Create a dict of the movies 
movies = [toy_story, avatar, bird_man, slumdog_millionare, butch_cassidy_and_the_sundance_kid, saving_christmas]

# pass list of movies to the generator
movie_generator.open_movies_page(movies)