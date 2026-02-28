class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


if __name__ == "__main__":
    bmp = LazyBitmap("facepalm.jpg")
    draw_image(bmp)
    draw_image(bmp)
