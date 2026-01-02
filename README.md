# AI-102-Full_Project_Building

--------------------------------
Step1:- Building Knowledge Base 
---------------------------------
1)Create a set of 20+ FAQs about platform and cources.

2)Azure Language Studio -->Host and Publisj the knowledge Base.

3)Python Chatbot -->Build a simple interface to interact with Knowledge base.


## Key Learning ##
------------------
1) Understand Azure AI Language to Build the Knowledge Base  [Q-A].

2) Build Knowledge Base 
    >Collect and Organize FAQs into a structured format.
    >Import questions and answers into AZURE Language Studio using a file. 

3)Build a Chatbot 
    >Build a Python program that can interact witht the knowledge base.
    >Create a bot like interface for users.
    >Build the interface in React.js that will call the Python program.
 
4)Deploy the Solution -->Azure
    >Deploy the python module that interacts with the Knowledge Base using Azure Functions
    >Host the Chatbot interface as a Static Website. We wil use Az Storage Accounts.


# Go to AZURE PORTAL 
------------------

1)Create -->L=AI Language  [Language Service] -->select -->Custom question answering
       -->as part of this --->  Azure AI Search "will also be created"  [just bcoz we l=selected Custom Q&A]

```
Go to -->Language Studio 
Sign In >> Select Subscription >> Resource Type >> Resource Name >> Done
Click -->Understand Question and Conversational Language  -->Select -->Custom question answering  -->Create a New Project ---> Select Language --> 
    >Name :- CourseKnowledgebase 
    Next -->Create Project 
```

#### Note #####
## We have a 2 ways of doing this

1st way:- - from the portal itself --> Edit Knowledge Base --> + -->Add a New Question Answer Pair 
    >Question :- 
    >Answer :- 

2nd way:- we have a file in our laptop [course_support_qna.tsv file ]
            we can >> import this Q&A 

GoTo --> Manage Sources --->Add Sources [URLs / Files / ChitChat]

-------------------------------------------------------
Step2 :- Adding Follow up Question in terms of Exsting Q&A 
--------------------------------------------------------
```
1)Do you provide training packages for corporates and Business? 
Yes, we provide trainings for teams and organizations
```

# We want a Follow-Up  =>May Be -->Knowledge will ask more Follow up Questions

```
Q)Would u like more details on Corporate Training Pricing Options
```
its like linking existing questions together in a follow up fashion.

-----------------------------------------------------------------------------
Step3 :- Save and Deploy our Knowlede Base --> this can be accessible via API 
-----------------------------------------------------------------------------
Deploy Knowledge Base  --->Click --> Deploy

Normally we would have programs that can call --->Knowledge Base
i.e Send Question from Customer--->Get the Anser from Knowledge Base --->Give the Answers to the Customers accordingly.

Click on --> Get Prediction URL ---> 

https://ailanguage3300.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=CourseKnowledgebase&api-version=2021-10-01&deploymentName=production

Sample Request:
---------------
```
curl -X POST "https://ailanguage3300.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=CourseKnowledgebase&api-version=2021-10-01&deploymentName=production" -H "Ocp-Apim-Subscription-Key: "xxxxxxxxxxxxxxxxxxx" -H "Content-Type: application/json" -d "{\"top\":3,\"question\":\"YOUR_QUESTION_HERE\",\"includeUnstructuredSources\":true,\"confidenceScoreThreshold\":\"YOUR_SCORE_THRESHOLD_HERE\",\"answerSpanRequest\":{\"enable\":true,\"topAnswersWithSpan\":1,\"confidenceScoreThreshold\":\"YOUR_SCORE_THRESHOLD_HERE\"},\"filters\":{\"metadataFilter\":{\"logicalOperation\":\"YOUR_LOGICAL_OPERATION_HERE\",\"metadata\":[{\"key\":\"YOUR_ADDITIONAL_PROP_KEY_HERE\",\"value\":\"YOUR_ADDITIONAL_PROP_VALUE_HERE\"}]}}}"
```

# Here, we can use the 
```
curl --> command, 
POST --->REQUEST, 
Against the url -->https://ailanguage3300.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=CourseKnowledgebase&api-version=2021-10-01&deploymentName=production,
Against our project --->projectName=CourseKnowledgebase,
Against our deployment name -->deploymentName=production,
Using Subscription Key -->For Authentication --->Apim-Subscription-Key. 
```

----------------------------------------------------------------------------------
Step4:- Develop a Simple Python Programm that can interact with the Knowledge Base
----------------------------------------------------------------------------------
This can be used to Send a REQUST to the above URL 
To our Knowledge Base --> Send Question from the USER --->Get the Answer Back !!

