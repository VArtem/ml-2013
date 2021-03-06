НИУ ИТМО, Машинное обучение (осень 2013)
================================================

Лабораторные работы по курсу [машинного обучения][ml home] студентов
четвертого курса НИУ ИТМО.

Рекомендуемые языки программирования: Python, Matlab(Octave). 
По согласованию с преподавателем возможны другие варианты.

Схема работы
-------------------

Работа с репозиторием ведется по схеме [fork & pull][fork-pull]

Структура каталогов: <имя.фамилия> - папка с личными наработками.
Внутренняя организация оставляется на личное усмотрение.

[ml home]: http://neerc.ifmo.ru/~ml
[fork-pull]: https://help.github.com/articles/using-pull-requests


Распознаванию раковых клеток
-------------------
Блок лабораторных работ по распознаванию раковых клеток [cancer].

####1. Линейный перцептрон 

Ключевые пункты:
- загрузка данных,
- разделение на обучающую и тестовую выборку,
- обучение классификатора,
- вычисление ошибки обучения на тестовых данных,
- вычисление точноcти и полноты классификации.


####2. Метод опорных векторов (SVM)
Реализуйте алгоритм. Регуляризационную константу C выберите при
помощи кросс-валидации.

Ключевые пункты:
- обучение классификатора,
- вычисление ошибки обучения на тестовых данных,
- выбор параметра алгоритма при помощи кросс-валидации.

####3. Метод опорных векторов с ядрами (SVM + Kernel trick)
Реализуйте алгоритм. Для решения задачи оптимизации используйте [SMO]. 
Сравните результаты для полиномального и гауссово ядра.

Ключевые пункты:
- решение задачи оптимизации,
- параметризация алгоритма функцией ядра.

####4. Метод логистической регрессии
Реализуйте алгоритм. Регуляризационный параметр λ подберите при помощи кросс-валидации.

Ключевые пункты:
- метод логистической регрессии,
- регуляризация.

####5. Нейронные сети
Реализуйте алгоритм. В качестве функции активации используйте [логистическую функцию][logistic].
При помоще кросс-валидации выберите оптимальные параметры сети (число слоев, вершин, λ).

Ключевые пункты:
- feedforward neural network,
- backpropagation.


[cancer]: http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29
[SMO]: http://cs229.stanford.edu/materials/smo.pdf
[logistic]: http://en.wikipedia.org/wiki/Logistic_function

(Устаревшее) Распознавание цифр
------------------

Блок лабораторные работы по распознаванию рукописных цифр архива [MNIST].

[MNIST]: http://yann.lecun.com/exdb/mnist/

####1. Метод опорных векторов (SVM)
Реализуйте алгоритм. Регуляризационную константу C выберите при
помощи кросс-валидации.

Ключевые пункты:
- загрузка данных,
- обучение классификатора,
- вычисление ошибки обучения на тестовых данных,
- выбор параметра алгоритма при помощи кросс-валидации.
