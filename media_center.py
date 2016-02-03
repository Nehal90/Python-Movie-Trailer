# This file is part of the Intro to python course but not needed for 
# actual movie-trailer project to run
import media
import content_controller

# Adding my favourite movie details

toy_story = media.Movie("Toy Story", 
						"A story about toys who come to life",
						"http://www.hesaidshesaidreviewsite.com/img/posters/toystory.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_ootry.title), ":", (toy_sotry.storyline) 

avatar = media.Movie("Avatar",
					 "About the Na'vi living in Pandora",
					 "http://avatarblog.typepad.com/.a/6a0120a6b2c140970c013480eb9042970c-pi",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.title), ":", (avatar.storyline)
# avatar.show_trailer()

transformers = media.Movie("Transformers",
						   "Alien robots from Cybertron being refugee on earth",
						   "http://ia.media-imdb.com/images/M/MV5BMTQwNjU5MzUzNl5BMl5BanBnXkFtZTYwMzc1MTI3._V1_SX640_SY720_.jpg",
						   "https://www.youtube.com/watch?v=XnwmUZuF5OY")
# print(transformers.title), ":", (transformers.storyline)

hunger_games = media.Movie("Hunger Games",
			  			   "About the girl from District 12 who survives the hunger games",
			  			   "http://ia.media-imdb.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SX640_SY720_.jpg",
			  			   "https://www.youtube.com/watch?v=4S9a5V9ODuY")

avengers = media.Movie("Avergers",
			           "Bunch of superheros who team up to save the world",
			           "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SX640_SY720_.jpg",
			           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

bourne_identity = media.Movie("Bourne Identity",
			                  "A former spy who goes after the authority for their illegal actions",
			                  "http://static.flickr.com/39/100950547_b9bab1a800_o.jpg",
			                  "https://www.youtube.com/watch?v=FpKaB5dvQ4g")

# declaring array that holds all the movies

movies = [toy_story, avatar, transformers, hunger_games, avengers, bourne_identity]
content_controller.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)  
# print(media.Movie.__doc__)			#doc written in the class
# print(media.Movie.__name__)       	#Class name
print(media.Movie.__module__)		    #Name of the module where the class resides