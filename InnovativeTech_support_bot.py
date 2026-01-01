# This is a Python Module 
# The Purpose of this is to Take a Question from USER --->Send Q -->Knowledge Base ==>Get Answer Back !!

import requests

# This is the Endpoint that our Knowledge Base is listing on...
endpoint="https://ailanguage3300.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=CourseKnowledgebase&api-version=2021-10-01&deploymentName=production"
api_key=""
headers={
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

def ask_question_answer(question: str):
       data={
              "question": question,
              "top": 1  # please return the top most answer from the Knowledge base
       } 


       response = requests.post(endpoint, headers=headers, json=data) 
       result = response.json()
       return result["answers"][0]

print("InnovativeTech Support Bot (type 'exit' to quit)")
while True:
       user_input = input("You: ")
       if user_input.lower() in ["exit","quit"]:
            print("Bot: Goodbye!")
            break
       answer = ask_question_answer(user_input)
       print(f"Bot: {answer}")