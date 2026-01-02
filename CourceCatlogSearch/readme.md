Course Catalog Search
InnovativeTech wants to implement an intellegent search system powered by Azure AI Search.
    >Allow students to search across course metadata (name, description , categories, prices)
    >Extract and index content from PDF's , and Images for deeper discoverability.
    >Extract information from a Azure CosmosDB databse.

Step1: Setup the data store [setup multiple data store]   
a) Setup Azure CosmosDB with Data.
b)Setup azure storage accounts with supplemantary data.

Step2:-Configure Azure AI Search 
a)Create data sourcec,indexes and indexers
b)Apply semanntic search and cognitive skill for enrichment.

Step3:- Integrate Azure AI Video Indexer
a)Extract transcripts from Video content.
b)Use the transcripts in the search

Step4:- Mutiple Indexes [becoaz we have multiple data store]
a)Understand how to use multiple indexes
b)Here we need to index through Azure Storage AND Azure CosmosDB


## Lab ##
---------

Step1:Creation of CosmosDB --> Azure Cosmos DB for NoSQL *[First DataStore]*
[Azure Cosmos DB is a fully managed NoSQL and relational database service for building scalable, high performance applications]

Go to Data Explorer
create Database > create container > add json data !!
eg:- sample data
---
{
"courseId": "AI-102",
"name": "AI-102: Microsoft Azure AI Engineer Associate",
"description": "Design and implement AI solutions including Azure AI Services, Azure OpenAI, Azure AI Search, content moderation, and custom models.",
"price": 165.0,
"category": "Azure AI Engineer"
}
---

Step2:- Setting up a Data Store in Azure Storage Account *[Second DataStore]*
