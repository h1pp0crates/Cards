# Власник репозиторія: Підмогильний Микита

# Гра "Черви" на Python

Цей проект створений у рамках марафону з програмування гри "Черви" на мові програмування Python.

## Опис гри

Здає в першому турі виділяється серед гравців в результаті жеребкування, потім гравці здають карти по черзі.
Кожному учаснику гри лунає 13 карт. Першим ходить той гравець, якому роздали трефова двійку, з цієї карти і починається 
гра. Далі за годинниковою стрілкою гравці кладуть карти такий же масті або будь-які інші, якщо одномасною немає. 
При першому ході не можна покласти червового карту або даму пік. Хабар бере гравець, що поклав найстаршу карту, 
одномасних з першої. В результаті розігрується 13 хабарів. Якщо у хабарі присутня карта Червової масті, гравець отримує 
за неї одне очко. Той, хто візьме пікову даму, отримає відразу 13 очок. Гравцеві, що зумів зібрати всі карти Червової
масті і даму пік, не нараховуються окуляри, зате всі інші учасники отримують по 26 очок. Коли один з гравців набере 100 
очок, він програє.

# Домашнє завдання. День 1

## Завдання 1

* написати функцію якам приймає рядок і повертає словник у якому
* ключами є всі символи, які зустрічаються в цьому рядку, а значення - відповідні
* вірогідності зустріти цей символ в цьому рядку.
* № код повинен бути структурований за допомогою конструкції if name == "main":,
* всі аргументи і значення що функція повертає повинні бути типізовані, функція має рядок документації
> Приклади:
> 
> print(get_symbols_frequency("")) = {}
> 
>print(get_symbols_frequency("123")) = {'1': 0.3333333333333333, '2': 0.3333333333333333, '3': 0.3333333333333333}
> 
> print(get_symbols_frequency("123331")) = {'3': 0.5, '1': 0.3333333333333333, '2': 0.16666666666666666}
