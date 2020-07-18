while True:
    print('Height: ', end='');
    user_input = input()

    if user_input.is_numeric():
        pyramid_height = int(user_input)
        if pyramid_height >= 1 and pyramid_height <= 8:
           break

for i in range(pyramid_height):
    spaces = (pyramid_height - 1 - i) * " "
    bricks = (i + 1) * "#"
    print(spaces + bricks)
