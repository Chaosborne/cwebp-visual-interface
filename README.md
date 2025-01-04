# cwebp-visual-interface
Convert images to webp with visual interface for cwebp image converter for Ubuntu Linux.

If you don't feel like writing 
```
for file in *.jpg; do cwebp -q 80 "$file" -o "${file%.*}.webp"; done
```
every time you use cwebp utility, here's a visual alternative:

<img src="https://github.com/Chaosborne/cwebp-visual-interface/blob/main/gitHub-readme-screenshot.png" />

You put images in one directory, they are automatically converted to webp and put in another directory.

## Before running the converter, ensure you have the following installed:
### 1. **Install `cwebp`**
The `cwebp` utility is used to convert images to WebP format. Install it using the following command:

```
sudo apt install webp
```

### 2. **Install `Python 3` and `Tkinter`**
The cwebp-visual-interface graphical user interface (GUI) is built using Tkinter. To install Python 3 and Tkinter, run:
```
sudo apt install python3 python3-tk
```

## Setup
### 1. Download the Files
Download the ```converter.py``` and ```WebPConverter.desktop``` files and place them in the ```/home/user/converter``` directory.

### 2. Make the Desktop Shortcut Executable
Terminal:
```
cd /home/user/converter
```
```
chmod +x WebPConverter.desktop
```

## Usage
1. Place the images you want to convert in the `/home/user/converter directory`.  
The tool will only process `.jpg,` `.jpeg,` and `.png` images.
2. Double-click the `WebPConverter` shortcut to open the GUI.
3. Enter the desired quality `(0-100)` for the conversion and click `Start Conversion`.
4. The images in the current folder will be converted to WebP format and saved in a new subdirectory called `compressed_images` within the same directory.  
