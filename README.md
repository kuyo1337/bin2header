---

## 📄 bin2header

**Convert any binary file into a C header file.**

### 🔧 Usage

```bash
python bin2header.py
```

You'll be prompted to enter:

* **Input file** (binary file to convert)
* **Output file** (C header file to generate)
* **Variable name** (name of the byte array in the C code)

### 📥 Example

```
input: myfont.ttf  
output: font.h  
variable name: fontData
```

### 📤 Output

Generates a `font.h` like:

```c
#ifndef FONT_H
#define FONT_H

unsigned char fontData[] = {
    0x00, 0x01, 0xFF, ...
};

unsigned int fontData_len = 1234;

#endif // FONT_H

