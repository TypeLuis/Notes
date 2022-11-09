<details>
<summary>Creating a flask application</summary>


First we will need to create a **virtual-enviornment** for our python file. The virtual-enviorment creates a contained location where the modules we install with **pip** are stored, set to the project only. 

`$ python3 -m venv venv`    The last word of this line is the name of the virtual enviorment folder. *"python3" will be different depending on what version you're using*

Next step is to **activate** the virtual enviorment. There's different ways to activate the enviorment depending on the platform and shell you're using.

## Windows:

### **cmd.exe:** `<venv>\Scripts\activate.bat`

### **PowerShell:**   `<venv>\Scripts\Activate.ps1`

## POSIX:
### **bash/zsh:**   `$ source <venv>/bin/activate`

### **PowerShell:**   `$ <venv>/bin/Activate.ps1`

### *To Deactivate*  `deactivate`


If project is being used in a git repository, add the virtual enviorment folder to **.gitignore**.


Once virutal enviorment is activated, start by installing **Flask** module with `pip install flask` *"pip" will be different depending on version*

After Flask is installed, create a file for the application *(application.py)*. In the file, paste the following flask template below.


```
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This is how a route works
@app.route('/', methods=['GET'])
def root():
    return {"message": 'ok'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

```


</details>

<details>
<summary>Adding .env (optional)</summary>

.env allows you to hide certain lines of code to not be pushed to a repository


</details>
