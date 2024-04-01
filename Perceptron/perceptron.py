weights = [0, 0]
bias = 0

def training():

    sum_error = 1
    global bias

    input_values_AND = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 1]
    ]

    input_values_OR = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    input_values_XOR = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]

    print("1 - AND\n2 - OR\n3 - XOR")

    initial_value = int(input("Enter a option: "))

    if initial_value == 1:
        main_values = input_values_AND
    elif initial_value == 2:
        main_values = input_values_OR
    else:
        main_values = input_values_XOR

    max_iterations = 1000
    learning_rate = 1.00

    for i in range(max_iterations):
        if sum_error > 0:
            sum_error = 0
            for j in range(4):
                output = weights[0] * main_values[j][0] + weights[1] * main_values[j][1] + bias

                if output >= 0:
                    output = 1
                else:
                    output = 0

                error = main_values[j][2] - output
                weights[0] = weights[0] + learning_rate * error * main_values[j][0]
                weights[1] = weights[1] + learning_rate * error * main_values[j][1]
                bias = bias + learning_rate * error
                if error != 0:
                    sum_error += 1
        i += 1
        if sum_error > 0:
            print("Training failed")
        else:
            print("Training successful")


def prediction():
    global bias
    input_values = [0, 0]

    while 2 > int(input_values[0]) >= 0 and 2 > int(input_values[1]) >= 0:

        value_one = input("Enter the values separated by (-): ")
        input_values = value_one.split('-')

        if 2 <= int(input_values[0]) or int(input_values[0]) < 0:
            print("Value one is invalid please try again")
            break

        if 2 < int(input_values[1]) or int(input_values[1]) < 0:
            print("Value one is invalid please try again")
            break

        output = weights[0] * float(input_values[0]) + weights[1] * float(input_values[1]) + bias

        if output >= 0:
            output = 1
        else:
            output = 0

        print("" + input_values[0] + "  " + input_values[1] + " = " + output.__str__())


training()
prediction()
