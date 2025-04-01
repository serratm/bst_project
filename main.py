# Main program to test Binary search tree.
from Node import Node
from BinarySearchTree import BinarySearchTree

tree = BinarySearchTree()

user_values = input("Enter insert values with spaces between: ")
print()

for value in user_values.split():
    new_node = Node(int(value))
    tree.insert(new_node)

print('Initial tree:')
print(tree)
print()


while True:
    new_key = int(input('Enter a new key to insert: '))
    new_node = Node(new_key)
    tree.insert(new_node)
    print(tree)
    print()

    remove_value = int(input('Enter value to remove: '))
    print()

    print('Tree after removing %d:' % remove_value)
    tree.remove(remove_value)
    print(tree)
    print()

    user_input = input('Do you want to continue? (yes/no): ')
    if user_input.lower() in ["yes", "y"]:
        continue_loop = True
    elif user_input.lower() in ["no", "n"]:
        continue_loop = False

min_value = tree.getmin()
print('Minimum Number in tree %d:'% min_value)

max_value = tree.getmax()
print('Maximum Number in tree %d:' % max_value)