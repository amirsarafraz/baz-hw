def spaces(input_str):
    result_str = input_str.replace(" ", "")
    return result_str


input_str = input()
output_str = spaces(input_str)

print(output_str)