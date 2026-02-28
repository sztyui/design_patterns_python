class GraphicObject:
    def __init__(self, color=None) -> None:
        self.color = color
        self.children = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        if depth != 0:
            items.append("*" * depth + " ")
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        self.items = []
        self._print(self.items, 0)
        return " ".join(self.items)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


if __name__ == "__main__":
    drawing = GraphicObject()
    drawing._name = "My Drawing"
    drawing.children.append(Square("Red"))
    drawing.children.append(Circle("Yellow"))

    group = GraphicObject()
    group.children.append(Circle("Blue"))
    group.children.append(Square("Blue"))

    drawing.children.append(group)

    print(drawing)
