from typing import Any


class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text="") -> None:
        self.text = text
        self.name = name
        self.elements: list[Any] = []

    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def add_element(self, element):
        self.elements.append(element)

    def __str__(self) -> str:
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.add_element(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name, child_text):
        self.__root.add_element(HtmlElement(child_name, child_text))
        return self

    def __str__(self) -> str:
        return str(self.__root)


builder = HtmlElement.create("uld")

# builder.add_child("li", "hello")
# builder.add_child("li", "world")

builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")

print("Ordinary builder:")
print(builder)
