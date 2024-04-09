# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add_last(self, value):
#         new_node = Node(value)
#         if not self.head:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next:
#                 current_node = current_node.next
#             current_node.next = new_node
#
#     def remove(self, value):
#         if self.head:
#             if self.head.value == value:
#                 self.head = self.head.next
#             else:
#                 current_node = self.head
#                 prev_node = None
#                 while current_node and current_node.value != value:
#                     prev_node = current_node
#                     current_node = current_node.next
#                 if current_node:
#                     prev_node.next = current_node.next
#
#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.value, end=" ")
#             current_node = current_node.next
#         print()
#
#     def contains(self, value):
#         current_node = self.head
#         while current_node:
#             if current_node.value == value:
#                 return True
#             current_node = current_node.next
#         return False
#
#     def replace(self, old_value, new_value):
#         current_node = self.head
#         while current_node:
#             if current_node.value == old_value:
#                 current_node.value = new_value
#                 return
#             current_node = current_node.next
#
#
# def main():
#     numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
#
#     linked_list = LinkedList()
#     for number in numbers:
#         linked_list.add_last(number)
#
#     while True:
#         print("1. Додати елемент до списку")
#         print("2. Видалити елемент зі списку")
#         print("3. Показати вміст списку")
#         print("4. Перевірити, чи є значення у списку")
#         print("5. Замінити значення у списку")
#         print("0. Вихід")
#
#         choice = int(input("Введіть номер пункту меню: "))
#
#         if choice == 0:
#             break
#
#         elif choice == 1:
#             value = int(input("Введіть значення: "))
#             linked_list.add_last(value)
#
#         elif choice == 2:
#             value = int(input("Введіть значення: "))
#             linked_list.remove(value)
#
#         elif choice == 3:
#             linked_list.print_list()
#
#         elif choice == 4:
#             value = int(input("Введіть значення: "))
#             if linked_list.contains(value):
#                 print("Значення", value, "є в списку")
#             else:
#                 print("Значення", value, "немає в списку")
#
#         elif choice == 5:
#             old_value = int(input("Введіть старе значення: "))
#             new_value = int(input("Введіть нове значення: "))
#             linked_list.replace(old_value, new_value)
#
#         else:
#             print("Неправильний номер пункту меню")
#
#
# if __name__ == "__main__":
#     main()


# Завдання 2
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert(self, data, index):
        if index < 0:
            raise IndexError("Індекс повинен бути невід'ємним")
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(index):
                if current is None:
                    raise IndexError("Індекс поза діапазоном")
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

    def delete(self, index):
        if index < 0:
            raise IndexError("Індекс повинен бути невід'ємним")
        if index == 0:
            if self.head is None:
                raise IndexError("Список порожній")
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    raise IndexError("Індекс поза діапазоном")
                current = current.next
            if current == self.tail:
                self.tail = current.prev
                self.tail.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def contains(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def replace(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
            current = current.next


def main():
    dll = DoublyLinkedList()

    numbers = input("Введіть числа для створення списку (через пробіл): ").split()
    for num in numbers:
        dll.append(int(num))

    while True:
        print("Меню:")
        print("1. Додати елемент до списку.")
        print("2. Видалити елемент зі списку.")
        print("3. Показати вміст списку.")
        print("4. Перевірити, чи є значення у списку.")
        print("5. Замінити значення у списку.")
        print("6. Вийти з програми.")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            data = input("Введіть елемент для додавання: ")
            dll.append(data)
            print("Елемент додано до списку.")
        elif choice == "2":
            index = int(input("Введіть індекс елемента для видалення: "))
            try:
                dll.delete(index)
                print("Елемент видалено зі списку.")
            except IndexError as e:
                print(e)
        elif choice == "3":
            print("Вміст списку:")
            dll.display()
        elif choice == "4":
            value = int(input("Введіть значення для перевірки: "))
            if dll.contains(value):
                print(f"Значення {value} присутнє у списку.")
            else:
                print(f"Значення {value} відсутнє у списку.")
        elif choice == "5":
            old_value = int(input("Введіть значення, яке потрібно замінити: "))
            new_value = int(input("Введіть нове значення: "))
            dll.replace(old_value, new_value)
            print(f"Значення {old_value} було замінено на {new_value}.")
        elif choice == "6":
            print("Програма завершена.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
