# KS_HTTPServer 

This server is using Flask. Flask is a Python module used for web applications. Below are the steps to run the server: 
1. Setting up & activating a virtual environment on Python:
  >>- [Tutorial](https://colab.research.google.com/drive/1aJqhYe31yBB47RtxrdMhzUWjaMbOdzTs?usp=sharing#scrollTo=BFk2Ax5K3CnD)
  >>- You will need the information under local installation to assist with this step
  >> - Python 3.9 will be needed to run the virtual environment
2. If you are unfamiliar with Flask, or need help installing it, the instructions can be found at [Flask Docs](https://flask.palletsprojects.com/en/2.3.x/installation/#install-flask): 
>> - Read through the Quickstart for an introduction on how to set up a basic application
>> - This will show you how to start the server
3. Once the server is running, the message "Hello World" should appear when you click this [url](http://localhost:5000/). 
4. You need to make an endpoint that reads a POST request a responds with the message that you entered.If you need assistance, the information is in the [Flask Quickstart](https://flask.palletsprojects.com/en/2.3.x/quickstart/#): 
5. By opening a terminal seperate from the one that is running a server, you have to use the curl command with the format **curl -X Post -H "content-type: application/json" -d '{"key1":"value1","key2","value2"}' http://server_url/route_name**
6. In order to make a proxy enpoint, you have to modify the first route so that the information in the link [pokeapi](https://pokeapi.co/api/v2/pokemon/eevee) shows in the web browser
>> - You may need a JSON formatter so that the information is shown in a consise manner. 
7. You will then have to modify step 5 so that when a person enters the specific name of the pokemon, the server will bring them the information about that pokemon. 

### After going through the previous steps, the server will have just completed the tasks listed above. 


