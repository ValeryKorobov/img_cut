# Script to remove the background from an image

### **Description**
With this script, you can upload any amount of pictures or photos and quickly cut out the object by removing the background.

### **Technology stack:**
| program                     | version |
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
#### **Original photo**
![Original photo](https://github.com/ValeryKorobov/img_cut/raw/main/input_pics/5.jpg)

#### **Edited photo**
![Edited photo](https://github.com/ValeryKorobov/img_cut/raw/main/output_pics/5_output.png)

### **Author**
[Korobov Valery](https://github.com/ValeryKorobov) - Python-developer
