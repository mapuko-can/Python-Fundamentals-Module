import re

number = int(input())
for i in range(number):
    barcode = input()
    pattern_word = r"\@\#+([A-Z][A-Za-z\d]{4,}[A-Z])\@\#+"
    pattern_digit = r"\d+"
    words = re.findall(pattern_word, barcode)
    valid_barcodes = "".join(words)
    digits = re.findall(pattern_digit, valid_barcodes)
    product_group = "".join(digits)
    if words:
        if product_group:
            print(f'Product group: {product_group}')
        else:
            print("Product group: 00")
    else:
        print('Invalid barcode')


# import re
#
# pattern_valid_barcodes = r"(@(#{1,}))([A-Z][a-zA-Z0-9]{4,}[A-Z]\b)(@(#{1,}))"
# pattern_product_group = r"\d"
# n = int(input())
# for _ in range(n):
#     barcode = input()
#     valid = [match.group() for match in re.finditer(pattern_valid_barcodes, barcode)]
#     if valid:
#         numbers_in_barcode = [i for i in re.findall(pattern_product_group, barcode)]
#         if numbers_in_barcode:
#             product_group = ''.join(numbers_in_barcode)
#         else:
#             product_group = f"00"
#         print(f"Product group: {product_group}")
#     else:
#         print("Invalid barcode")



# import re
#
# count_of_barcodes = int(input())
#
# for value in range(count_of_barcodes):
#     barcode = input()
#     barcode_pattern = r'\@\#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+'
#     is_valid = re.findall(barcode_pattern, barcode)
#
#     if is_valid:
#         barcode = ''.join(is_valid)
#         product_group = ''.join([x for x in barcode if x.isdigit()])
#         if not product_group:
#             product_group = '00'
#         print(f'Product group: {product_group}')
#     else:
#         print('Invalid barcode')