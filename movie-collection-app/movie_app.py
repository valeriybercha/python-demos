# Movie Collection App
# Author: Valeriy B.

# Description: basic app written on Python to store the favourite movies into a collection with the possibility to add, view or delete a movie.


# Importing modules
import os
import csv


# # Welcome Message
# def welcome_message():
#     return "Hello and welcome to 'Movie Collection App'. Type 'add' to add a new movie into collection, 'info' for more information or 'q' to quit the app"


# # Good bye message
# def good_bye_message():
#     return "Good bye!"

def in_app_messages(msg):
    if msg == 'welcome':
        return "Hello and welcome to 'Movie Collection App'. Type 'add' to add a new movie into collection, 'info' for more information or 'q' to quit the app"
    elif msg == 'bye':
        return "Good bye!"
    elif msg == "no_movies":
        return "No movies in collection yet! Type 'add' to add a movie to collection"

# Readme information
def app_info():
    with open('info.txt') as f:
        info = f.read()
    return info


# Commands dictionary
def app_commands(command):
    commands_dict = {
        # Add new control commands here
        "yes": ["yes", "y"],
        "no": ["no", "n", "nope"],
        "end": ["quit", "q", "end", "exit"],
        "info": ["info", "i"],
        "add": ["add", "a"],
        "display": ["display", "d"],
        "del": ["delete", "del"]
    }
    return commands_dict[command]


# Create a .csv file (as a database)
def create_csv_file():
    with open('movie_data.csv', "w") as file:
        file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow(["Movie", "Year", "Genre"])


# Adding movies to .csv file
def adding_movies():
    
    # Add a movie inputs by name, year and genre
    movie_title = input("Enter a movie title: ")
    movie_year = input("Enter movie release year: ")
    movie_genre = input("Enter movie genre: ")
    added_movie = [movie_title.title(), movie_year, movie_genre.title()]
    print(f'>>> "{added_movie[0]}" ({added_movie[1]}), {added_movie[2]}')
    
    # Save input into .csv file
    save = input("Do you want to save the movie (y/n): ")
    if save.lower() == "y":
        with open('movie_data.csv', 'a+', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(added_movie)
            print(f'"{added_movie[0]}" ({added_movie[1]}) movie was successfully added to your collection')


# Display the movies collection
def display_movies():
    with open('movie_data.csv', 'r') as read_file:
        movie_list = []
        csv_reader = csv.DictReader(read_file)
        line_count = 0
        for row in csv_reader:
            movie_list.append(row)
            if line_count == 0:
                print("")
                print('========== Your movie collection ==========')
                print("")
                line_count += 1
            print(f'\t #{line_count}. "{row["Movie"]}" ({row["Year"]}), {row["Genre"]}')
            line_count += 1
        if len(movie_list) == 0:
            print(in_app_messages("no_movies"))
        print("")
        print("_" * 45)
        print("")



# Delete movies
def delete_movies():
    lines = []
    movie_delete = input("Type a movie you want to delete?: ")
    with open('movie_data.csv', 'r') as del_file:
        reader = csv.reader(del_file)
        for row in reader:
            lines.append(row)
            for i in row:
                if i == movie_delete.title():
                    try:
                        lines.remove(row)
                        print(f'"{movie_delete.title()}" movie was successfully deleted')
                    except:
                        print("Movie not found")
    with open('movie_data.csv', 'w', newline='') as add_file:
        writer = csv.writer(add_file)
        writer.writerows(lines)
            

# General app menu
def movie_app(run_commands):

    # Welcome message
    print(in_app_messages("welcome"))

    while run_commands.lower() not in app_commands("end"):
        run_commands = input("Enter a command: ")
        if run_commands.lower() in app_commands("info"):
            print(app_info())
        elif run_commands.lower() in app_commands("add"):
            
            # Verifying if the .csv file exists
            if not os.path.isfile('./movie_data.csv'):
                create_csv_file()

            # Adding movies to the collection
            adding_movies()

        # Display the movies collection
        elif run_commands.lower() in app_commands("display"):
            display_movies()
        
        # Delete movie from collection
        elif run_commands.lower() in app_commands("del"):
            delete_movies()
    
    # Good bye message
    print(in_app_messages("bye"))


movie_app("")
