class Phone:
    """Телефон класс"""

    number = "123"
    _calls = 0

    def input_number(self, number) -> None:
        """Ввод номера"""
        self.number = number

    def output(self) -> int:
        """Вывод количества звонков"""
        return self._calls

    def add_call(self) -> None:
        """Добавление звонка"""
        self._calls += 1


one = Phone()
two = Phone()
three = Phone()

one.input_number("+432123")
two.input_number("+4567823")
three.input_number("+987230")

one.add_call()
one.add_call()

two.add_call()
two.add_call()
two.add_call()

three.add_call()
three.add_call()
three.add_call()
three.add_call()


def num_of_calls(phones: list[Phone]) -> int:
    return sum([phone.output() for phone in phones])


print(num_of_calls([one, two, three]))  # 9


class Chess_piece:
    color = "white" / "black"
    position = "0, 7"

    def change_color(self, color) -> None:
        """Изменение цвета"""
        self.color = color

    def move(self, new_position) -> None:
        """Передвижение"""
        if self._is_on_board(new_position):
            self.position = new_position
        else:
            raise ValueError("Новая позиция за пределами доски!")

    def _is_on_board(self, position) -> bool:
        """Проверка на нахождение на доске 0, 7"""
        x, y = position
        return 0 <= x <= 7 and 0 <= y <= 7

    def can_move(self, new_position) -> bool:
        """Проверка возможности хода"""
        raise NotImplementedError(
            "Этот метод должен быть переопределен в подклассах")


class Pawn(Chess_piece):
    """Пешка"""
    def can_move_to(self, new_position) -> bool:
        """Проверка возможности хода"""
        x, y = self.position
        new_x, new_y = new_position
        direction = 1 if self.color == "white" else -1
        # Пешка может двигаться на 1 клетку вперед, или на 2 клетки, на старте
        if new_x == x and (
            (new_y == y + direction)
            or (y == (1 if self.color == "white" else 6)
                and new_y == y + 2 * direction)
        ):
            return self._is_on_board(new_position)
        return False


class Knight(Chess_piece):
    """Конь"""

    def can_move_to(self, new_position) -> bool:
        """Проверка возможности хода"""
        x, y = self.position
        new_x, new_y = new_position
        # Конь может передвигаться буквой Г
        if (abs(new_x - x), abs(new_y - y)) in ((1, 2), (2, 1)):
            return self._is_on_board(new_position)
        return False
    

class Bishop(Chess_piece):
    """Слон"""

    def can_move_to(self, new_position) -> bool:
        """Проверка возможности хода"""
        x, y = self.position
        new_x, new_y = new_position
        # Слон может передвигаться по диагонали
        if abs(new_x - x) == abs(new_y - y):
            return self._is_on_board(new_position)
        return False
    

class Rook(Chess_piece):
    """Ладья"""

    def can_move_to(self, new_position) -> bool:
        """Проверка возможности хода"""
        x, y = self.position
        new_x, new_y = new_position
        # Ладья может передвигаться по вертикали или горизонтали
        if new_x == x or new_y == y:
            return self._is_on_board(new_position)
        return False
    

class Queen(Chess_piece):
    """Ферзь"""

    def can_move_to(self, new_position) -> bool:
        """Проверка возможности хода"""
        x, y = self.position
        new_x, new_y = new_position
        # Ферзь может передвигаться по диагонали, вертикали или горизонтали
        if abs(new_x - x) == abs(new_y - y) or new_x == x or new_y == y:
            return self._is_on_board(new_position)
        return False
    

class King(Chess_piece):
    """Король"""

    def can_move_to(self, new_position) -> bool:
        """Проверка возможности хода"""
        x, y = self.position
        new_x, new_y = new_position
        # Король может передвигаться по диагонали, вертикали или горизонтали
        if abs(new_x - x) <= 1 and abs(new_y - y) <= 1:
            return self._is_on_board(new_position)
        return False


def find_pieces_that_can_move(
        pieces: list[Chess_piece], target_position: tuple[int, int]
        ) -> list[Chess_piece]:
    """Нахождение фигур, которые могут ходить в заданную позицию"""
    movable_pieces = []
    for piece in pieces:
        if piece.can_move_to(target_position):
            movable_pieces.append(piece)
    return movable_pieces


# Пример использования
pieces = [
    Pawn("white", (1, 1)),
    Knight("black", (0, 0)),
    Bishop("white", (2, 0)),
    Rook("black", (0, 7)),
    Queen("white", (3, 3)),
    King("black", (4, 4)),
]

# Проверяем, какие фигуры могут добраться до клетки (2, 2)
movable_pieces = find_pieces_that_can_move(pieces, (2, 2))
for piece in movable_pieces:
    print(
        f"{piece.__class__.__name__} на {piece.position} "
        f"может двигаться к {piece.position}."
        )
