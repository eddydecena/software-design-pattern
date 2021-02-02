from typing import Any

class Memento():
    def __init__(self, file: str, content: Any) -> None:
        self.file = file
        self.content = content

class FileWriter():
    def __init__(self) -> None:
        self.file: str = ''
        self.content: Any = ''
        self.memento: Memento = Memento(self.file, self.content)
    
    def write(self, content: str) -> None:
        self.content += content
    
    def undo(self) -> None:
        self.file = self.memento.file
        self.content = self.memento.content
    
    def save(self) -> None:
        self.memento.file = self.file
        self.memento.content = self.content

if __name__ == '__main__':
    writer = FileWriter()
    
    writer.write('Some content!!')
    print(writer.content)
    writer.save()
    print(writer.content)
    writer.write('More content!!')
    print(writer.content)
    writer.undo()
    print(writer.content)