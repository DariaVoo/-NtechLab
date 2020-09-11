# NtechLab_test
Тестовое задание на осеннюю стажировку в NtechLab

## Задание 1.
Найти непрерывный подмассив в массиве, содержащий хотя бы одно число,
который имеет наибольшую сумму.

[Решение](https://github.com/DariaVoo/NtechLab_test/blob/master/task1/findMaxSubArray.py)

## Задание 2.
Необходимо обучить нейросеть, способную по входному изображению лица
определять пол человека на изображении.
* [Описание решения](https://github.com/DariaVoo/NtechLab_test/blob/master/task2/task2.ipynb) (подготовки данных, используемой нейросети, параметров обучения и
полученных результатов)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DariaVoo/NtechLab_test/blob/master/task2/task2.ipynb)
* [API](https://github.com/DariaVoo/NtechLab_test/blob/master/task2/predict_model.py) для работы с готовой моделью 

*Usage:* 

Перед использованием API скачайте [модель](https://drive.google.com/file/d/1-EsN6zXVwyneZm4faYoaKCzDyNp0r0yC/view?usp=sharing) и  укажите в переменной PATH_MODEL путь до модели.

Затем запустите программу, выполнив команду

`python3 predict_model.py folder/to/process/`

где  _folder/to/process/_ путь до папки с данными, для которых вы хотите получить предсказания.


* [Модель](https://drive.google.com/file/d/1-EsN6zXVwyneZm4faYoaKCzDyNp0r0yC/view?usp=sharing)
