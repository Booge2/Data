class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_last(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def remove(self, value):
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
            else:
                current_node = self.head
                prev_node = None
                while current_node and current_node.value != value:
                    prev_node = current_node
                    current_node = current_node.next
                if current_node:
                    prev_node.next = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()

    def contains(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def replace(self, old_value, new_value):
        current_node = self.head
        while current_node:
            if current_node.value == old_value:
                current_node.value = new_value
                return
            current_node = current_node.next


def main():
    numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

    linked_list = LinkedList()
    for number in numbers:
        linked_list.add_last(number)

    while True:
        print("1. Додати елемент до списку")
        print("2. Видалити елемент зі списку")
        print("3. Показати вміст списку")
        print("4. Перевірити, чи є значення у списку")
        print("5. Замінити значення у списку")
        print("0. Вихід")

        choice = int(input("Введіть номер пункту меню: "))

        if choice == 0:
            break

        elif choice == 1:
            value = int(input("Введіть значення: "))
            linked_list.add_last(value)

        elif choice == 2:
            value = int(input("Введіть значення: "))
            linked_list.remove(value)

        elif choice == 3:
            linked_list.print_list()

        elif choice == 4:
            value = int(input("Введіть значення: "))
            if linked_list.contains(value):
                print("Значення", value, "є в списку")
            else:
                print("Значення", value, "немає в списку")

        elif choice == 5:
            old_value = int(input("Введіть старе значення: "))
            new_value = int(input("Введіть нове значення: "))
            linked_list.replace(old_value, new_value)

        else:
            print("Неправильний номер пункту меню")


if __name__ == "__main__":
    main()


# Завдання 2
