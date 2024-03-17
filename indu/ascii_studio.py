import pickle
from image_file import ImageFile
from helpers import print_tabs, get_key_by_value

class AsciiStudio:

    def __init__(self):
        self.USER_COMMANDS: list[str] = ["quit", "load", "render", "info", "set", "save"]
        self.image_alias_DB = {
            # image alias : image object
        }

        self.current_file = None

    def render_command(self, args):

        """This method is used to render images into ascii art. Either by the user entering an alias or actuall filename it will check that it exists.
            The method is also able to save the ASCII art to a text file.    
            """

        if len(args) == 0: # If only render is entered as a command with no arguments, current file should be rendered.
            try:
                if self.current_file is None:
                    print("No current file loaded")

                else:
                    print(self.current_file.render())

            except Exception as e:
                print("Error: Could not render file")
                print(e)

        elif len(args) == 1: # renders the file which the user has entered. $ render filename
            try:
                print(self.image_alias_DB[args[0]].render())
                self.current_file = self.image_alias_DB[args[0]]

            except Exception as e:
                print(f"Error: Could not render file")
                print(e)

        elif len(args) == 3 and args[1] == "to": # render img to filename. Saves the render to a text file
            try:
                with open(f"{args[2]}.txt", "w") as f:
                    f.write(self.current_file.render())
            
            except Exception as e:
                print(f"Error: Could not write to {args[2]}")
                print(e)
                return
        
        else:
            print("Error: Not a valid input!")

    def load_command(self, args):
        """The load command is used to load load images into a session. Either saving them with an alias or by their filename.
        Given that the file is found.

        """
        try:
            if not (args[0] == "image" or args[0] == "session"): # Checking if the parameter entered with the command is either a session or image.
                raise IndexError
            
            action = args[0]

            if action == "image":
                if len(args) == 4 and args[2] == "as": # Checking if it's the right parameters
                    filename = args[1]
                    alias = args[3]
                    loaded_file = ImageFile(filename)
                    try: # To check if loaded_file is initialized 
                        if loaded_file.img:
                            self.image_alias_DB[alias] = loaded_file
                            self.current_file = self.image_alias_DB[alias]

                    except Exception:
                        pass
                
                elif len(args) == 2: # If the file has no alias the user will enter the actual filename, which is this code snippet.
                    filename = args[1]
                    loaded_file = ImageFile(filename)
                    try: # To check if loaded_file is initialized 
                        if loaded_file.img:
                            self.image_alias_DB[filename] = loaded_file
                            self.current_file = self.image_alias_DB[filename]
                    except Exception:
                        pass

                else:
                    raise IndexError


            if action == "session":
                try:
                    # Using pickle and storing varibles and dictionaries in a dictionary. This dictionary filled with data is then loaded and ready to be used
                    with open(f"./{args[1]}", "rb") as f: 
                        saved_data = pickle.load(f)
                        self.current_file = saved_data["current_file_save"]
                        self.image_alias_DB = saved_data["image_alias_DB_save"]

                except Exception as e:
                    print("Error: Could not load session")
                    print(e)
            
        except IndexError:
            print("Not a valid command")

    def info_command(self):
        """Goes through each image in the session and then using a utility function to print the results nicely.
        """
        print("=== Current session ===")
        print("Images:")
        for image_object in self.image_alias_DB:
            print(image_object)
            print_tabs(self.image_alias_DB[image_object].get_info())

        print(f"Current file: {get_key_by_value(self.image_alias_DB, self.current_file)}")

    def save_command(self, args):
        """Saving data from the sesssion in a dictonary. The data to be stored is the current file and the dictonary with all the image objects.
        """
        try:
            if not (args[0] == "session" and args[1] == "as"):
                raise IndexError
            
            filename = args[2]  
            try:
                data = {"image_alias_DB_save": self.image_alias_DB, "current_file_save": self.current_file}
                with open(f"./{filename}.pkl", "wb") as f:
                    pickle.dump(data, f)

            except Exception:
                print("Error: Could not save session")

        except IndexError:
            print("Not valid command")

        except Exception as e:
            print("Error: An unknown error occurred")
            print(e)

    def set_command(self, args):
        """This method is used by the set command. Given that the entred file exists, the user is able to change, brightness, contrast, width or height.
        """
        try:

            action = args[1]

            if action not in ["height", "width", "brightness", "contrast"]:
                raise IndexError
            
            filename = args[0]
            try:
                num = int(args[2])

            except:
                print("Must enter a integer - no decimals")
                raise IndexError

            if filename in self.image_alias_DB:
                self.current_file = self.image_alias_DB[filename]
                
                if action == "width":
                    self.image_alias_DB[filename].resize_image(new_width=num)

                if action == "height":
                    self.image_alias_DB[filename].resize_image(new_height=num)

                if action == "brightness":
                    self.image_alias_DB[filename].change_brightness(num)

                if action == "contrast":
                    self.image_alias_DB[filename].change_contrast(num)

            else:
                print(filename + " is not found")

                

        except IndexError:
            print("Not valid command!")
    
    def parse(self, user_input):

        """Accpets the user input as a argument and then splits it up into command and arguments. Checking which command is entered and then running the corresponding method

        Returns:
            boolen: This to determine whether the while loop should continue or not. False is for the program to stop.
        """

        command, *args = user_input.split()

        if command not in self.USER_COMMANDS:
            print("Not a valid command, please try again!")

        if command == "quit":
            print("Bye!")
            return False

        if command == "render":
            self.render_command(args)

        if command == "load":
            self.load_command(args)

        if command == "info":
            self.info_command()

        if command == "save":
            self.save_command(args)

        if command == "set":
            self.set_command(args)

        return True

    def run(self):
        
        print("Welcome to ASCII Art Studio!")
        
        while True:
            user_input = str(input("AAS: ")).lower()            

            if self.parse(user_input) is False:
                break

            