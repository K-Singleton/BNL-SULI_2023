# KS_HTTPServer 

This server is using Flask. Flask is a Python module used for web applications. Below are the steps to run the server: 
1. Setting up & activating a virtual environment on Python:   
```install python3```   
```python3 --version```   
```python3 -m venv .server_name```  
```source .server_name/bin/activate```  

To stop the virtual environment, enter : ```deactivate```  

2. Create a Python file and enter:  
```
From flask import Flask  
app = Flask(__name__)  

@app.route("/")
def name(): 
    return 'Hello, World!'


if __name__ == '__main__':```  
    app.run(debug=True, host='0.0.0.0')
```
3. To start server enter: ```python file_name.py```