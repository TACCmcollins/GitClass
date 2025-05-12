import random

def random_color():
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
    selected_color = random.choice(colors)
    print(f"The selected color is: {selected_color}")

if __name__ == "__main__":
    random_color()
