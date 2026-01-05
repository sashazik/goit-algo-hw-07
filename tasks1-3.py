class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, key):
        if self.val:
            if key < self.val:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key > self.val:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.val = key

# --- Завдання 1: Знаходження найбільшого значення ---
def get_max_value(node):
    current = node
    # У BST найбільше значення завжди знаходиться в крайньому правому вузлі
    while current.right is not None:
        current = current.right
    return current.val

# --- Завдання 2: Знаходження найменшого значення ---
def get_min_value(node):
    current = node
    # У BST найменше значення завжди знаходиться в крайньому лівому вузлі
    while current.left is not None:
        current = current.left
    return current.val

# --- Завдання 3: Знаходження суми всіх значень ---
def get_sum(node):
    if node is None:
        return 0
    # Рекурсивно додаємо значення поточного вузла + сума лівого піддерева + сума правого
    return node.val + get_sum(node.left) + get_sum(node.right)

# --- Перевірка роботи ---
if __name__ == "__main__":
    root = Node(15)
    root.insert(10)
    root.insert(20)
    root.insert(5)
    root.insert(12)
    root.insert(25)

    print(f"Максимальне значення: {get_max_value(root)}")  # 25
    print(f"Мінімальне значення: {get_min_value(root)}")    # 5
    print(f"Сума всіх значень: {get_sum(root)}")            # 15+10+20+5+12+25 = 87
