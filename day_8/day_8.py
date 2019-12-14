import enum


def read_input(file):
    f = open(file)
    a = list(map(int, f.readlines()[0]))
    f.close()
    return a


def read_layer(image, layer, layer_len):
    return image[layer_len * layer : (layer + 1) * layer_len]


def find_least_zeros_layer():
    image = read_input("input")
    layer_len = 25 * 6
    layer_count = int(len(image) / layer_len)
    number_of_zeros = layer_len
    result = 0
    for l in range(0, layer_count):
        layer = read_layer(image, l, layer_len)
        count = {}
        for c in layer:
            count[c] = count.get(c, 0) + 1
        if count.get(0, 0) < number_of_zeros:
            number_of_zeros = count.get(0, 0)
            result = count.get(1, 0) * count.get(2, 0)

    return result


print("Part 1:", find_least_zeros_layer())


class Colors(enum.Enum):
    Black = 0
    White = 1
    Transparent = 2


def find_decoded_image(file, width, height):
    image = read_input(file)
    layer_len = width * height
    layer_count = int(len(image) / layer_len)
    output = read_layer(image, 0, layer_len)

    for l in range(1, layer_count):
        next_layer = read_layer(image, l, layer_len)

        for i in range(0, layer_len):
            c = next_layer[i]
            if output[i] == Colors.Transparent.value:
                output[i] = c

    return ''.join([str(elem) for elem in output])


def render_image(decoded_image, width):
    result = ""
    for i in range(0, len(decoded_image)):
        if int(decoded_image[i]) == Colors.Black.value:
            result += " "
        elif int(decoded_image[i]) == Colors.White.value:
            result += "#"
        if (i + 1) % width == 0:
            result += "\n"

    return result


assert(find_decoded_image("test_input", 2, 2) == "0110")


print("Part 2:")
print(render_image(find_decoded_image("input", 25, 6), 25))

