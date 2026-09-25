"""
Постройки: абстрактный класс Building и конкретные классы Fort, MobileHouse.
"""

from .core import GameObject, Attacker, Moveable
from .units import Unit


class Building(GameObject):
    """
    Постройка.

    Класс абстрактный по тем же причинам, что и Unit: в игре есть
    только конкретные постройки (Fort, MobileHouse и т.д.), а не
    "постройка вообще".
    """

    def __init__(self, obj_id: int, name: str, x: int, y: int, built: bool = False) -> None:
        super().__init__(obj_id, name, x, y)
        self._built = built

    def isBuilt(self) -> bool:
        """Возвращает, построена ли постройка."""
        return self._built

    def build(self) -> None:
        """Завершает строительство (вспомогательный метод для демонстрации)."""
        self._built = True
        print(f"{self.getName()} построен(а) и готов(а) к использованию")


class Fort(Building, Attacker):
    """Крепость: постройка, способная стрелять из пушек по противникам."""

    ATTACK_DAMAGE = 40.0
    ATTACK_RANGE = 10

    def get_type(self) -> str:
        return "Крепость"

    def attack(self, unit: Unit) -> None:
        if not self.isBuilt():
            print(f"{self.getName()} ещё не построена и не может стрелять")
            return
        distance = max(abs(self.getX() - unit.getX()), abs(self.getY() - unit.getY()))
        if distance > self.ATTACK_RANGE:
            print(f"{self.getName()}: цель {unit.getName()} вне радиуса действия пушек ({distance} > {self.ATTACK_RANGE})")
            return
        print(f"{self.getName()} стреляет из пушек в {unit.getName()} (урон {self.ATTACK_DAMAGE})")
        unit.receiveDamage(self.ATTACK_DAMAGE)


class MobileHouse(Building, Moveable):
    """Дом на колёсах: постройка, способная передвигаться."""

    def get_type(self) -> str:
        return "Дом на колёсах"

    def move(self, new_x: int, new_y: int) -> None:
        if not self.isBuilt():
            print(f"{self.getName()} ещё не построен, перемещение невозможно")
            return
        print(f"{self.getName()} едет из ({self.getX()}, {self.getY()}) в ({new_x}, {new_y})")
        self._x = new_x
        self._y = new_y
