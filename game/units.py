"""
Юниты: абстрактный класс Unit и конкретный класс Archer.
"""

from .core import GameObject, Attacker, Moveable


class Unit(GameObject):
    """
    Юнит — управляемый игровой объект (подразделение, человек, рабочий).

    Класс абстрактный: в игре создаются только конкретные типы юнитов
    (например, Archer), а не "юнит вообще" — поэтому наследует
    нереализованный get_type() из GameObject и сам не становится
    конкретным.
    """

    def __init__(self, obj_id: int, name: str, x: int, y: int, hp: float) -> None:
        super().__init__(obj_id, name, x, y)
        self._hp = hp

    def isAlive(self) -> bool:
        """Возвращает, жив ли юнит."""
        return self._hp > 0

    def getHp(self) -> float:
        """Возвращает количество здоровья у юнита."""
        return self._hp

    def receiveDamage(self, damage: float) -> None:
        """Уменьшает здоровье юнита на величину полученного урона."""
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._hp = max(0.0, self._hp - damage)


class Archer(Unit, Attacker, Moveable):
    """Лучник: юнит, умеющий атаковать стрелами и передвигаться."""

    ATTACK_DAMAGE = 15.0
    ATTACK_RANGE = 5

    def __init__(self, obj_id: int, name: str, x: int, y: int, hp: float = 50.0) -> None:
        super().__init__(obj_id, name, x, y, hp)

    def get_type(self) -> str:
        return "Лучник"

    def attack(self, unit: Unit) -> None:
        if not self.isAlive():
            print(f"{self.getName()} мёртв и не может атаковать")
            return
        distance = max(abs(self.getX() - unit.getX()), abs(self.getY() - unit.getY()))
        if distance > self.ATTACK_RANGE:
            print(f"{self.getName()}: цель {unit.getName()} вне радиуса стрельбы ({distance} > {self.ATTACK_RANGE})")
            return
        print(f"{self.getName()} стреляет из лука в {unit.getName()} (урон {self.ATTACK_DAMAGE})")
        unit.receiveDamage(self.ATTACK_DAMAGE)

    def move(self, new_x: int, new_y: int) -> None:
        print(f"{self.getName()} перемещается из ({self.getX()}, {self.getY()}) в ({new_x}, {new_y})")
        self._x = new_x
        self._y = new_y
