import re

number = int(input())
for lines in range(number):
    barcodes = input()

    pattern1 = r"\@\#+([A-Z][A-Za-z\d]{4,}[A-Z])\@\#+"
    pattern2 = r"\d+"

    text = re.findall(pattern1, barcodes)
    valid_barcodes = "".join(text)
    digits = re.findall(pattern2, valid_barcodes)
    product_group = "".join(digits)

    if text:
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")


