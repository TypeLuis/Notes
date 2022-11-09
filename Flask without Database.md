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

