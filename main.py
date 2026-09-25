"""
Демонстрация иерархии классов пошаговой стратегии:
GameObject -> Unit -> Archer
GameObject -> Building -> Fort, MobileHouse
Интерфейсы: Attacker, Moveable
"""

from game import GameObject, Unit, Building, Archer, Fort, MobileHouse


def section(title: str) -> None:
    print("\n=== " + title + " ===")


def main() -> None:
    section("Проверка абстрактности базовых классов")
    for cls in (GameObject, Unit, Building):
        try:
            cls(1, "test", 0, 0)  # type: ignore[abstract]
        except TypeError as exc:
            print(f"Создать {cls.__name__} напрямую нельзя: {exc}")

    section("Создание объектов")
    archer1 = Archer(1, "Робин", x=0, y=0, hp=50)
    archer2 = Archer(2, "Марион", x=3, y=4, hp=40)
    fort = Fort(3, "Северная крепость", x=0, y=0)
    house = MobileHouse(4, "Караван", x=10, y=10)
    for obj in (archer1, archer2, fort, house):
        print(obj)

    section("Работа интерфейса Moveable")
    archer1.move(1, 1)
    house.move(11, 10)  # ещё не построен

    section("Работа интерфейса Attacker")
    archer1.attack(archer2)
    print(f"HP {archer2.getName()}: {archer2.getHp()}, жив: {archer2.isAlive()}")
    fort.attack(archer2)  # крепость ещё не построена

    section("Строительство и повторные попытки")
    fort.build()
    house.build()
    fort.attack(archer2)
    house.move(11, 10)

    section("Полиморфизм: все объекты, умеющие атаковать / двигаться")
    attackers = [archer1, fort]
    moveables = [archer1, house]

    for a in attackers:
        a.attack(archer2)

    for m in moveables:
        m.move(m.getX() + 1, m.getY())

    section("Добиваем цель")
    while archer2.isAlive():
        archer1.attack(archer2)
    print(f"{archer2.getName()} побеждён(а): жив = {archer2.isAlive()}, HP = {archer2.getHp()}")


if __name__ == "__main__":
    main()
