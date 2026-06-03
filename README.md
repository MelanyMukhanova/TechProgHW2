# TechProgHW2 - Система управления рецептами 
## Краткое описание проекта
Проект для работы с рецептами, ингредиентами и списком покупок.
Реализованы классы: `Ingredient`,`Recipe`,`DietaryRecipe`,`ShoppingList`.
Проект осуществляет:
- добавление ингредиентов в рецепт;
- изменять количество порций;
- создание списка покупок;
- удаление рецептов из списка;
- работу с диетическими рецептами;
- тестирование с помощью `pytest`.

Стурктура проекта
- `recipes.py` — реализация классов
- `test_recipes.py` — тесты
- `requirements.txt` — зависимости
- `.gitignore` — игнорируемые файлы
- `README.md` — документация

## Использование
Как запускать код - python recipes.py
Как заупскать тесты - pytest test_recipes.py -v

## Автор
Муханова Мелания Сергеевна ББИ2509

## Установка
```bash
git clone https://github.com/MelanyMukhanova/TechProgHW2.git
cd TechProgHW2
pip install -r requirements.txt
