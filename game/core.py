"""
Базовые сущности игры: GameObject и интерфейсы Attacker / Moveable.
"""

from abc import ABC, abstractmethod


class GameObject(ABC):
    """
    Базовый класс, от которого наследуются все игровые объекты.

    Класс объявлен абстрактным: в игре не существует "обезличенных"
    объектов без конкретного типа (юнит, постройка и т.д.), поэтому
    у GameObject есть абстрактный метод get_type(), который обязаны
    реализовать все конкретные классы-наследники.
    """

    def __init__(self, obj_id: int, name: str, x: int, y: int) -> None:
        self._id = obj_id
        self._name = name
        self._x = x
        self._y = y

    def getId(self) -> int:
        """Возвращает идентификатор объекта."""
        return self._id

    def getName(self) -> str:
        """Возвращает имя объекта."""
        return self._name

    def getX(self) -> int:
        """Возвращает координату X объекта."""
        return self._x

    def getY(self) -> int:
        """Возвращает координату Y объекта."""
        return self._y

    @abstractmethod
    def get_type(self) -> str:
        """Человекочитаемое название конкретного типа объекта."""
        raise NotImplementedError

    def __str__(self) -> str:
        return (
            f"{self.get_type()} '{self._name}' "
            f"(id={self._id}, x={self._x}, y={self._y})"
        )


class Attacker(ABC):
    """Интерфейс объектов, способных атаковать другие юниты."""

    @abstractmethod
    def attack(self, unit: "Unit") -> None:  # noqa: F821  (Unit определён в units.py)
        """Наносит урон переданному юниту."""
        raise NotImplementedError


class Moveable(ABC):
    """Интерфейс объектов, способных перемещаться по карте."""

    @abstractmethod
    def move(self, new_x: int, new_y: int) -> None:
        """Перемещает объект в новые координаты."""
        raise NotImplementedError
