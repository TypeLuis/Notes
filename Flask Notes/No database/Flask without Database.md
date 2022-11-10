<details>
<summary><h2>Creating a flask application</h2></summary>


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


Once virutal enviorment is activated, start by installing **Flask** module with `pip install flask flask-cors` *"pip" will be different depending on version*

<details>
<summary><h3>What is cors?</h3></summary>

cors is short for **Cross-Origin Resource**, it's a protocol that allows servers to recieve requests from different domains. Without cors, if a website doesn't have the same domain name as the api routes, the api will be blocked due to cors policy.

</details>

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
<summary><h2>Adding .env</h2></summary>

.env allows you to hide certain lines of code to not be pushed to a repository this imporoves secruity to the code.

First once you created your virtual enviorment and application, import dotenv module `pip3 install python-dotenv`

### after the module is installed, create a **.env** file and add the file in the .gitignore file (important)

inside .env, this is where we put lines of code we want to use but don't want anybody to see **(ex: api keys)**. paste the following for example.

```
ENV_EXAMPLE=This is an example
another_Example=https://www.google.com
```

before the equal sign is the name of the env variable **(case sensitive)** after the equal is the value.

in your application file, paste the following

```
import os
from dotenv import load_dotenv

# loads the env variables in application 
load_dotenv()

print(os.environ.get("ENV_EXAMPLE")) # This is an example
print(os.environ.get("another_Example")) # https://www.google.com
```

</details>


<details>
<summary><h2>Adding Blueprints to Flask</h2></summary>

Blueprints in Flask allows us to seperate the api routes into different files otherwise called **Seperation of concern**.

First create a new file, call it what you need but for now we'll call it **blueprint_example.py** and paste the following code

## blueprint_example.py
```
from flask import Blueprint


example_blueprint = Blueprint("blueprint_example", __name__)  # inside of "blueprint_example" string should be the name of the file


# It's recomended to add /example to every route as the main path of the blueprint routes to seperate the routes by path

@example_blueprint.route('/example', methods=['GET'])
def example():
    return {"message": 'This is a blueprint example'}

```

On the imports of your application.py add another import `from example import example_blueprint`. **example_blueprint** is the variable we called for the blueprint route in blueprint_example.py

The final step is to register the blueprint to the app route below the app variable `app.register_blueprint(example_blueprint)`

Your application.py currently should look something like this

## application.py
```
import os
from flask import Flask
from flask_cors import CORS

# imports from blueprint
from blueprint_example import example_blueprint

app = Flask(__name__)
CORS(app)

# connects blueprint to the app routes
app.register_blueprint(example_blueprint)

# This is how a route works
@app.route('/', methods=['GET'])
def root():
    return {"message": 'ok'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
```
After the final step, your example_blueprint route should work as normal.

</details>