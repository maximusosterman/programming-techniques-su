from PIL import Image

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

        
    def __str__(self):    
        return f"Filename: {self.filename}, size: {self.image_size} (width, height)"
    
    def greyify(self):
        self.img = self.img.convert(mode="L")
    
    def resize_image(self, new_width=50):
        self.width = new_width
        self.height = int(self.ratio * self.width)
        self.img = self.img.resize((self.width, self.height))
    
    def convert_to_ascii(self):
        pixels = self.img.getdata()
        return "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    
    def render(self):
        self.resize_image()
        self.greyify()
        image_data = self.convert_to_ascii()
        count_pixels = len(image_data)
        ascii_image = "\n".join(image_data[i:(i+self.width)] for i in range(0, count_pixels, self.width))
        print(ascii_image)
        
            
def main():
    print("Welcome to ASCII Art Studio!")
    USER_COMMANDS: list[str] = ["quit", "load", "render", "info"]
    current_file = None
    
    while True:
        user_input = str(input("AAS: "))

        try:
            command, filename = user_input.split(" ")

        except:
            command, filename = user_input, None

        if command not in USER_COMMANDS:
            print("Not a valid command, please try again!")
            continue

        if command == "quit":
            print("Bye!")
            break

        if command == "render" and current_file:
            current_file.render()

        if command == "load":
            if not filename:
                print("Please enter a filename!")
                break

            current_file = ImageFile(filename)

        if command == "info":
            if not current_file:
                print("No image loaded")
            else:
                print(current_file)




if __name__ == '__main__':
    main()