# Now we have a Knowledge Base In Azure AI Language 
# We have a Python Module that can be used to Invoke the Language Service -->Go aginst the Knowledge Base URL 
# ask a Question to Knowledge Base & get a Answer Back !!!

# NOTE :- THIS IS RUNNING ON LOCAL MACHINE !!!

# We want to Deploy this Python Module Somewhere.......so that any application , any USER can invoke it.
# Companies will take this Solution and Host it somewhere .....
# We can have Multiple Applications calling this module.

# Deploying Solutions : What do we need to Deploy this Python Module.
# We would need Compute Machine hosted on Azure Cloud.
## Option1: 
# On this VM we would need to Install Python
# Install the required Module 

## Option2: 
# Instead of using VM we can use Azure Functions 
# Benifits is that we dont have to Maintain Compute Infrastructure
# All we need to do is Publish Code to --->Azure Functions 

# Step1: Take Python Module -->Deploy to -->AZURE Functions --> 
#        we can have -->Az Web APP -->This could be sitting on its own compute service.
#        This Application can call the Module. 


Go to Azure Portal 
Create Azure Functions -->Function App 
                            >Flex Consumption : 
                            >Consumption : pay as u go model, only charged till the time function runs.takes time
                            >App Service : Provides us with compute infra. we can host web app / function app ...for quick invocation of azure functions.
                             here, its always running...its quick!!!   

Go inside Azure Functions    
Create HTTP Trigger 
---
import azure.functions as func
import logging,json,os,requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOS)

@app.route(route="ask1")
def ask(req: func.HttpRequest) -> func.HttpResponse:
    endpoint="https://ailanguage3300.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=CourseKnowledgebase&api-version=2021-10-01&deploymentName=production"
    api_key=os.environ["LANGUAGE_API_KEY"]
    headers={
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
    }

    logging.info(api_key)
    logging.info(endpoint)

    req_body=req.get_json()
    question=req_body.get('question)

    data={
              "question": question,
              "top": 1
       } 

    response = requests.post(endpoint, headers=headers, json=data) 

    result=response.json()

    answers = result.get("answers", [])
    answer=answers[0]
    out = { "answer": answer}

    logging.info(out)
    return func.HttpResponse(json.dumps(out), mimetype="application/json")



----

# Step 
We need to set this -->  "LANGIAGE_API_KEY" --> we are not embedding the secret in the code
we can define the variable within Azure Functions that would contain this Key info and then we can pick it up from our code 

Go to Language Service -->Resource Management --> keys 

Go to Function App --> Settings -->Environment Variables
                                    >App settings --> Add >> 
                                    >Connection string 
        
        App Settings:
            Name: LANGIAGE_API_KEY
            Value: <key1 from Language Service>
            <Apply>

# Step 
# We need to make sure : json & os [Libary] should already be avilable in the Python Environment
    >Azure Function -->Providing us with Linux Based Environment
                    >That will have -->Python 
                    >At the same time some basic Libaries like --> OS & json would be availabe, but "requests" libary wont be avaialable.
       
        We need to Explicitly tell Azure Functions to Install -->request libary
We can do it in Visual Studio Code itself But we are doing it via Portal 

Go to Azure Function
    >Development Tool --> Advanced Tools --> Click --->G0 --> This will opne up a new Interface

 Click on Bash 
> cd /home/site/wwwroot
>ls
__pycache__  function_app.py   host.json 

we want to create a file --> requirements.txt   [what are the packages required for function to run]

cat > requirements.txt << EOF
>requests
>EOF 

ls 
__pycache__  function_app.py   host.json  requirements.txt 

# Run this below command 
pip install -r requirements.txt --target .python_packages/lib/site-packages

# will get this result:
Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@fbeadc95d95b:/# cd /home/site/wwwroot
root@fbeadc95d95b:~/site/wwwroot# pip install -r requirements.txt --target .python_packages/lib/site-packages

[notice] A new release of pip is available: 25.2 -> 25.3
[notice] To update, run: /opt/python/3.13.5/bin/python3 -m pip install --upgrade pip
---

