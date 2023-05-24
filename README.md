# Script to remove background

### **Description**
With this script, you can upload any amount of pictures or photos and quickly cut out the object by removing the background.

### **Technology stack:**
| программа                     | версия |
|-------------------------------|--------|
| [rembg](https://github.com/danielgatis/rembg)                       | 2.0.37 |
| [Pillow](https://python-scripts.com/pillow)                       | 9.5.0 |

### **Run the project in dev mode on Windows**
Clone a repository from GitHub
```
git clone git@github.com:ValeryKorobov/img_cut.git
```

Install venv virtual environment
```
python -m venv venv
```

Activate venv virtual environment
```
source venv/Scripts/activate
```

Update pip package manager
```
python -m pip install --upgrade pip
```

Install Dependencies
```
pip install rembg
```
Or
```
pip install rembg[gpu]
```

### **Examples of processed images**
![Original photo](https://github.com/ValeryKorobov/img_cut/raw/main/input_pics/5.jpg)
