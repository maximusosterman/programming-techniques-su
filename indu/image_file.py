
from PIL import Image, ImageEnhance


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
            self.brightness = 1.0
            self.contrast = 1.0

        except Exception as e:
            print("Error loading image: " + filename)
            print(e)
        
    def get_info(self):
        """Prints all of the information and attributes of the image object

        Returns:
            string: string with all the info
        """
        return f"filename: {self.filename}\nsize: ({self.width, self.height})\nbrightness: {self.brightness}\ncontrast: {self.contrast}"
    
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
        """Converting a image to ascii by getting the brightness from each pixel and the asining it to a charachter from the ASCII representation.

        Returns:
            string: Return a string representation of the image in the ASCII representation.
        """
        pixels = self.img.getdata()
        return "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    
    def change_brightness(self, change_factor):
        enhancer = ImageEnhance.Brightness(self.img)
        self.img = enhancer.enhance(change_factor)
        self.brightness = change_factor # This number is used when using the info command

    def change_contrast(self, change_factor):
        self.img = ImageEnhance.Contrast(self.img).enhance(change_factor)
        self.contrast = change_factor # This number is used when using the info command
    
    def render(self):
        """The method turns the image gray, getting a string representation of the image in ASCII, splitting it up into rows and columns based in the width and height.

        Returns:
            str: Returns a string representation of the image, but with line breaks creating a ASCII representation.
        """
        self.greyify()
        image_data = self.convert_to_ascii()
        count_pixels = len(image_data)
        ascii_image = "\n".join(image_data[i:(i+self.width)] for i in range(0, count_pixels, self.width))
        return ascii_image