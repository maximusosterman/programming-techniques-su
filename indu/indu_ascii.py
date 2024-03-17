from PIL import Image, ImageEnhance
import pickle

# The user should be able to run following commands:
#   - Load filename
#   - Render the image in ASCII
#   - Print the info of the file
#   - Quit

ASCII_CHARS = ["", ".", ":", "i", "j", "x", "o", "O", "h", "X", "%", "@"][::-1]

class ImageFile:

    def __init__(self, filename):

        if not filename:
            raise ValueError

        try:
            
            with Image.open(filename) as loaded_image:
                loaded_image.load()
                self.img = loaded_image

            self.image_size = self.img.size
            self.filename = filename
            self.width, self.height = self.img.size
            self.ratio = self.height / self.width

        except Exception as e:
            print("Error loading image: " + filename)
            print(e)
        
    def get_info(self):    
        return f"filename: {self.filename}\nsize: ({self.width, self.height})"
    
    def greyify(self):
        self.img = self.img.convert(mode="L")
    
    def resize_image(self, new_width=None, new_height=None):
        """
        Resizes the image based on the provided width or height.

        Args:
            new_width (int, optional): The new width for the image. Defaults to None.
            new_height (int, optional): The new height for the image. Defaults to None.

        Raises:
            ValueError: If neither width nor height is provided.
        """

        if new_width is None and new_height is None:
            self.width = 50
            self.height = int(self.ratio * self.width)
        # Maintain aspect ratio if only one dimension is provided
        elif new_width is not None and new_height is None:
            self.width = new_width
            self.height = int(self.ratio * self.width)
        elif new_width is None and new_height is not None:
            self.height = new_height
            self.width = int(self.ratio * self.height)
        else:
            # If both width and height are provided, use them directly
            self.width = new_width
            self.height = new_height

        self.img = self.img.resize((self.width, self.height))
    
    def convert_to_ascii(self):
        pixels = self.img.getdata()
        return "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    
    def change_brightness(self, change_factor):
        enhancer = ImageEnhance.Brightness(self.img)
        self.img = enhancer.enhance(change_factor)
        self.img.show()

    def change_contrast(self, change_factor):
        self.img = ImageEnhance.Contrast(self.img).enhance(change_factor)
        self.img.show()
    
    def render(self):
        self.greyify()
        image_data = self.convert_to_ascii()
        count_pixels = len(image_data)
        ascii_image = "\n".join(image_data[i:(i+self.width)] for i in range(0, count_pixels, self.width))
        return ascii_image
    
def print_tabs(str):
    for str in str.split("\n"):
        print("\t" + str)

def get_key_by_value(my_dict, value):
  for key, val in my_dict.items():
    if val == value:
      return key
  return None  # If no key is found
            
def main():
    print("Welcome to ASCII Art Studio!")
    USER_COMMANDS: list[str] = ["quit", "load", "render", "info", "set", "save"]
    image_alias_DB = {
        # Alias : Object
    }
    current_file = None
    
    while True:
        user_input = str(input("AAS: "))

        command, *args = user_input.split()

        if command not in USER_COMMANDS:
            print("Not a valid command, please try again!")
            continue

        if command == "quit":
            print("Bye!")
            break

        if command == "render":

            if len(args) == 0: # render
                try:
                    print(current_file.render())

                except Exception as e:
                    print("Error: Could not render file")
                    print(e)

            elif len(args) == 1: # render img
                try:
                    print(image_alias_DB[args[0]].render())
                    current_file = image_alias_DB[args[0]]

                except Exception as e:
                    print(f"Error: Could not render file")
                    print(e)

            elif len(args) == 3 and args[1] == "to": # render img to filename
                try:
                    with open(f"{args[2]}.txt", "w") as f:
                        f.write(current_file.render())
                
                except Exception as e:
                    print(f"Error: Could not write to {args[2]}")
                    print(e)
                    break
            
            else:
                print("Error: Not a valid input!")

        if command == "load":

            try:
                if not (args[0] == "image" or args[0] == "session"):
                    raise IndexError
                
                action = args[0]

                if action == "image":
                    if len(args) == 4 and args[2] == "as":
                        filename = args[1]
                        alias = args[3]
                        loaded_file = ImageFile(filename)
                        try: # To check if loaded_file is initialized 
                            if loaded_file.img:
                                image_alias_DB[alias] = loaded_file
                                current_file = image_alias_DB[alias]

                        except Exception:
                            pass
                    
                    elif len(args) == 2:
                        filename = args[1]
                        loaded_file = ImageFile(filename)
                        try: # To check if loaded_file is initialized 
                            if loaded_file.img:
                                image_alias_DB[filename] = loaded_file
                                current_file = image_alias_DB[filename]
                        except Exception:
                            pass

                    
                    else:
                        raise IndexError


                if action == "session":
                    try:
                        with open(f"./sessions/{args[1]}", "rb") as f:
                            saved_data = pickle.load(f)
                            current_file = saved_data["current_file_save"]
                            image_alias_DB = saved_data["image_alias_DB_save"]

                    except Exception as e:
                        print("Error: Could not load session")
                        print(e)
                
            except IndexError:
                print("Not a valid command")

        if command == "info":
            print("=== Current session ===")
            print("Images:")
            for image_object in image_alias_DB:
                print(image_object)
                print_tabs(image_alias_DB[image_object].get_info())

            print(f"Current file: {get_key_by_value(image_alias_DB, current_file)}")

            

        if command == "save":
            try:
                if not (args[0] == "session" and args[1] == "as"):
                    raise IndexError
                
                filename = args[2]  
                try:
                    data = {"image_alias_DB_save": image_alias_DB, "current_file_save": current_file}
                    with open(f"./sessions/{filename}.pkl", "wb") as f:
                        pickle.dump(data, f)

                except Exception:
                    print("Error: Could not save session")

            except IndexError:
                print("Not valid command")

            except Exception as e:
                print("Error: An unknown error occurred")
                print(e)

        if command == "set":
            try:

                action = args[1]

                if action not in ["height", "width", "brightness", "contrast"]:
                    raise IndexError
                
                filename = args[0]
                num = int(args[2])

                if filename in image_alias_DB:
                    current_file = image_alias_DB[filename]
                    
                    if action == "width":
                        image_alias_DB[filename].resize_image(new_width=num)

                    if action == "height":
                        image_alias_DB[filename].resize_image(new_height=num)

                    if action == "brightness":
                        image_alias_DB[filename].change_brightness(num)

                    if action == "contrast":
                        image_alias_DB[filename].change_contrast(num)

                else:
                    print(filename + " is not found")

            except IndexError:
                print("Not valid command")

                

if __name__ == '__main__':
    main()