Задача №1.

Необходимо создать динамическую структуру данных - односвязный список (LinkedList).

Он должен поддерживать следующие операции:
1. Добавление нового узла в список (insert_node)
2. Поиск по элементам списка (search_node)
3. Удаление элемента списка (delete_node)

Поле полезной нагрузки (data) должно хранить число.

Также необходимо создать функцию (number_to_list), которая будет принимать на вход число любой длины и представлять его в виде списка. Стандартные структуры типа list etc использовать нельзя.

Задача №2.

В качестве входящих данных у вас есть два связных списка, представляющих два неотрицательных числа. Цифры хранятся в обратном порядке и каждый элемент списка хранит одну цифру. Сложите два числа и верните результат в виде связного списка. Предполагается, что оба числа не содержат лидирующих нулей, кроме случая, когда число само по себе 0. Числа могут быть сколь угодно большие.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8
