# Лабораторная работа №2 — Основы ООП

Иерархия классов для пошаговой стратегии: `GameObject`, `Unit`, `Building`,
интерфейсы `Attacker` и `Moveable`, конкретные классы `Archer`, `Fort`,
`MobileHouse`.

## Структура проекта

```
game/
    __init__.py
    core.py       # GameObject, Attacker, Moveable
    units.py      # Unit, Archer
    buildings.py  # Building, Fort, MobileHouse
main.py           # демонстрация работы иерархии
```

## Запуск

```bash
python3 main.py
```
