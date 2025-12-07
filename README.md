# repo_1

В директории repo_1\10_lesson\ находятся тесты сайта Калькулятора и Интернет-магазина с соответствующими им классами страниц.

Все классы страниц сформированы в директории \pages и содержат в себе методы работы с необходимыми страницами сайтов, и необходимые локаторы для обозначения элементов страницы. Необходимые страницы заранее импортированы в тесты.

Список тест-кейсов:
1. ТЕСТ-КЕЙС CALC-2 (Калькулятор)
Pages: CalcPage.py

2. ТЕСТ-КЕЙС SHOP-2 (Интернет-магазин)
Pages: LoginPage.py, ShopPage.py, CartPage.py, CheckoutPage.py

---------------

Для запуска тестов и формирования отчётов:

1. Перейти в нужную директорию: cd 10_lesson

2. Запустить тесты: pytest --alluredir allure-result
или python -m pytest --alluredir allure-result

В директории 10_lesson\allure-result будут сохранятся логи о пройдённых тестах

3. Конвертация результатов теста в отчёт: allure serve allure-result

4. Для формирования результатов теста в HTML-отчёт: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

5. scoop install allure
