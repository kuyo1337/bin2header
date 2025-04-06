input = input("input: ")
output = input("output:")
fontname = input("variable name: ")

with open(input, "rb") as f:
    data = f.read()

with open(output, "w") as f:
    f.write(f"#ifndef FONT_H\n#define FONT_H\n\n")
    f.write(f"unsigned char {fontname}[] = {{\n")
    for i, byte in enumerate(data):
        f.write(f"0x{byte:02X}, ")
        if (i + 1) % 12 == 0:
            f.write("\n")
    f.write("\n};\n\n")
    f.write(f"unsigned int {fontname}_len = {len(data)};\n\n")
    f.write("#endif // FONT_H\n")

print(f"done:'{output}'")
