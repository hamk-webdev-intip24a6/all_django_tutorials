import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from moviedb.models import Director, Genre, Movie

def populate():
    movies_data = [
        {
            "title": "The Godfather",
            "pub_date": date(1972, 3, 24),
            "directors": [("Francis Ford", "Coppola")],
            "genres": ["Crime", "Drama"],
            "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
        },
        {
            "title": "The Shawshank Redemption",
            "pub_date": date(1994, 9, 23),
            "directors": [("Frank", "Darabont")],
            "genres": ["Drama"],
            "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
        },
        {
            "title": "Schindler's List",
            "pub_date": date(1993, 12, 15),
            "directors": [("Steven", "Spielberg")],
            "genres": ["Biography", "Drama", "History"],
            "description": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis."
        },
        {
            "title": "Raging Bull",
            "pub_date": date(1980, 12, 19),
            "directors": [("Martin", "Scorsese")],
            "genres": ["Biography", "Drama", "Sport"],
            "description": "The life of boxer Jake LaMotta, whose violence and temper that led him to the top in the ring destroyed his life outside of it."
        },
        {
            "title": "Casablanca",
            "pub_date": date(1942, 11, 26),
            "directors": [("Michael", "Curtiz")],
            "genres": ["Drama", "Romance", "War"],
            "description": "A cynical American expatriate struggles to decide whether or not he should help his former lover and her fugitive husband escape French Morocco."
        },
        {
            "title": "Citizen Kane",
            "pub_date": date(1941, 5, 1),
            "directors": [("Orson", "Welles")],
            "genres": ["Drama", "Mystery"],
            "description": "Following the death of publishing tycoon Charles Foster Kane, reporters scramble to uncover the meaning of his final utterance: 'Rosebud'."
        },
        {
            "title": "Gone with the Wind",
            "pub_date": date(1939, 12, 15),
            "directors": [("Victor", "Fleming")],
            "genres": ["Drama", "History", "Romance"],
            "description": "A manipulative woman and a roguish man conduct a turbulent romance during the American Civil War and Reconstruction periods."
        },
        {
            "title": "The Wizard of Oz",
            "pub_date": date(1939, 8, 25),
            "directors": [("Victor", "Fleming")],
            "genres": ["Adventure", "Family", "Fantasy"],
            "description": "Dorothy Gale is swept away from a farm in Kansas to a magical land of Oz in a tornado and embarks on a quest with her new friends to see the Wizard who can help her return home."
        },
        {
            "title": "One Flew Over the Cuckoo's Nest",
            "pub_date": date(1975, 11, 19),
            "directors": [("Milos", "Forman")],
            "genres": ["Drama"],
            "description": "A criminal pleads insanity and is admitted to a mental institution, where he rebels against the oppressive nurse and rallies up the scared patients."
        },
        {
            "title": "Lawrence of Arabia",
            "pub_date": date(1962, 12, 10),
            "directors": [("David", "Lean")],
            "genres": ["Adventure", "Biography", "Drama"],
            "description": "The story of T.E. Lawrence, the English officer who successfully united and led the diverse, often warring, Arab tribes during World War I in order to fight the Turks."
        },
        {
            "title": "Vertigo",
            "pub_date": date(1958, 5, 9),
            "directors": [("Alfred", "Hitchcock")],
            "genres": ["Mystery", "Romance", "Thriller"],
            "description": "A former San Francisco police detective juggles wrestling with his personal demons and becoming obsessed with the hauntingly beautiful woman he has been hired to trail."
        },
        {
            "title": "Psycho",
            "pub_date": date(1960, 9, 8),
            "directors": [("Alfred", "Hitchcock")],
            "genres": ["Horror", "Mystery", "Thriller"],
            "description": "A Phoenix secretary embezzles $40,000 from her employer's client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother."
        },
        {
            "title": "The Godfather: Part II",
            "pub_date": date(1974, 12, 20),
            "directors": [("Francis Ford", "Coppola")],
            "genres": ["Crime", "Drama"],
            "description": "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate."
        },
        {
            "title": "Star Wars: Episode IV - A New Hope",
            "pub_date": date(1977, 5, 25),
            "directors": [("George", "Lucas")],
            "genres": ["Action", "Adventure", "Fantasy"],
            "description": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station."
        },
        {
            "title": "2001: A Space Odyssey",
            "pub_date": date(1968, 4, 2),
            "directors": [("Stanley", "Kubrick")],
            "genres": ["Adventure", "Sci-Fi"],
            "description": "After discovering a mysterious artifact buried beneath the Lunar surface, mankind sets off on a quest to find its origins with help from intelligent supercomputer H.A.L. 9000."
        },
        {
            "title": "Sunset Blvd.",
            "pub_date": date(1950, 8, 10),
            "directors": [("Billy", "Wilder")],
            "genres": ["Drama", "Film-Noir"],
            "description": "A screenwriter writes a screenplay for a former silent-film star who has faded into Hollywood obscurity."
        },
        {
            "title": "The Matrix",
            "pub_date": date(1999, 3, 31),
            "directors": [("Lana", "Wachowski"), ("Lilly", "Wachowski")],
            "genres": ["Action", "Sci-Fi"],
            "description": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence."
        },
        {
            "title": "Goodfellas",
            "pub_date": date(1990, 9, 19),
            "directors": [("Martin", "Scorsese")],
            "genres": ["Biography", "Crime", "Drama"],
            "description": "The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito in the Italian-American crime syndicate."
        },
        {
            "title": "Seven Samurai",
            "pub_date": date(1954, 4, 26),
            "directors": [("Akira", "Kurosawa")],
            "genres": ["Action", "Drama"],
            "description": "A poor village under attack by bandits recruits seven unemployed samurai to help them defend themselves."
        },
        {
            "title": "City Lights",
            "pub_date": date(1931, 1, 30),
            "directors": [("Charles", "Chaplin")],
            "genres": ["Comedy", "Drama", "Romance"],
            "description": "With the aid of a wealthy erratic tippler, a dewy-eyed tramp who has fallen in love with a sightless flower girl accumulates money to be able to help her medically."
        }
    ]

    for data in movies_data:
        # Create or get directors
        director_objs = []
        for fn, ln in data['directors']:
            d, created = Director.objects.get_or_create(first_name=fn, last_name=ln)
            director_objs.append(d)

        # Create or get genres
        genre_objs = []
        for g_name in data['genres']:
            g, created = Genre.objects.get_or_create(name=g_name)
            genre_objs.append(g)

        # Create or get movie
        if not Movie.objects.filter(title=data['title']).exists():
            m = Movie.objects.create(
                title=data['title'],
                pub_date=data['pub_date'],
                description=data['description']
            )
            m.directors.set(director_objs)
            m.genres.set(genre_objs)
            print(f"Added movie: {m.title}")
        else:
            print(f"Movie already exists: {data['title']}")

if __name__ == '__main__':
    print("Populating the moviedb database...")
    populate()
    print("Done!")
