## Designing Data Source ##

We will store our data in Azure Storage account using Blob Service.
Basically taking in Data from different sources 

1)Azure blob storage 
2)Azure Data Lake Storage Gen2
3)Azure Cosmos DB
4)Azure SQL Database
5)Azure Table Storage
6)Microsoft OneLake

## How do be Build Index ? | Indexer | SkillSet via JSON

1.Imagine that there are reviews being left by customer on a website.
2.We have a utility that is scraping those reviews, putting it within a centralized file this file is residing within Azure Blob Storage
3.There are different ways in which you can store your reviews from your site 

## Lab ##
----------

1. Go to Azure Portal 
```
Create a Storage Account 
Create a Container --> document 
In docoment -->Upload "reviews.txt" file 
```
Now, we meed this reviews to be Indexed via Azure Search
We want to add enrichment pipeline that can analyse these reviews,
Understand the sentiments accordingly.

2. Creating a resource based on Azure AI Search 
```
Create Search Service 
Go to > Search Management   > Indexes 
                            > Indexers
                            > Data Sources  --> We need to define our Data Source
                            > Aliases
                            >Skillsets 
                            >Debus sessions


Data Sources > Add data source >

    >Data source :- Azure blob storage
    >Name:- <Name auto pop >
    >Subscription:- <your subscription name>
    >Storage Account:- datastore3300
    >Blob Container:- documents
    >Blob Folder:-
    <Create>

NOTE: This now points on to the Container within Azure Blob Storage.

``` 


3. Build Index

Reference Link :- "https://learn.microsoft.com/en-us/azure/search/search-what-is-an-index"

Index :- What makes ur content searchable in nature. "Field attributes"
i.e searchable | filterable | sortable | retrievable| key

we are focusing on :- Index | Indexer | Skillset based on JSON

via Portal 
----------
Go to Search Service
Overview > Import Data > we have >azureblob-datasource > select --> click Next
Add Cognitive Skills > Add enrichments [based on data that is comming we can use diff AI Skills within azure]
Create and Index > content field name is imp --> This maps on to the content based on reviews.txt file 
Create Indexer > [This is kind of pipeline that reads data from the datasource]
                 [It extracts the text from the data source]
                 [It porforms an action called Docment Tracking ]
                 Apply the SkillSet  and Push Data unto Index.

# Via Portal But JSON 

```
Go to Azure Search Service
Go to Search Management >
    >Indexes -->Add Index > JSON >  
    >Indexers
    >Data Source
    >Aliases
    >Skillsets

>Indexes -->Add Index > JSON >  
---
{
  "name": "sentiment-index",
  "fields": [
    {
      "name": "id",
      "type": "Edm.String",
      "key": true,
      "filterable": false,
      "sortable": false,
      "facetable": false,
      "searchable": false
    },
    {
      "name": "content",
      "type": "Edm.String",
      "filterable": false,
      "sortable": false,
      "facetable": false,
      "searchable": true,
      "retrievable": true
    },
    {
      "name": "metadata_storage_name",
      "type": "Edm.String",
      "filterable": true,
      "sortable": true,
      "facetable": false,
      "searchable": false,
      "retrievable": true
    },
    {
      "name": "metadata_storage_path",
      "type": "Edm.String",
      "filterable": true,
      "sortable": false,
      "facetable": false,
      "searchable": false,
      "retrievable": true
    }          
  ]
}
---
Note: Index is in place now !!!!

```

 # Build Indexer  [We need a Indexer --> that will pull out the documents from data source] > It will perform a act of Document Crackung that is Extracting the Text...It can Enrish the data by using a Skillset, and then it can push the results onto the Search Index. 
 
```
Go to Search Services 
Go to > Search Management 
select --> Indexers -->Add Indexer (JSON)

---
{
  "name": "sentiment-indexer",
  "dataSourceName": "azureblob-1767338744365-datasource",
  "targetIndexName": "sentiment-index",
  "schedule": {
    "interval": "PT2H",
    "startTime": "2025-12-31T00:00:00Z"
  },
  "parameters": {
    "configuration": {
      "dataToExtract": "contentAndMetadata",
      "parsingMode": "default"
    }
  },
  "fieldMappings": [
    {
      "sourceFieldName": "metadat_storage_name",
      "targetFieldName": "id",
      "mappingFunction": {"name": "base64Encode"}
    }
  ],
  "outputFieldMappings": [
    {
      "sourceFieldName": "/document/content",
      "targetFieldName": "content"
    },
    {
      "sourceFieldName": "/document/metadata_storage_name",
      "targetFieldName": "metadata_storage_name"
    },
    {
      "sourceFieldName": "/document/metadata_storage_path",
      "targetFieldName": "metadata_storage_path"
    }
  ]
}
---
    click on <Save>

```

# Build Skillset in Azure AI Search 

Reference: https://learn.microsoft.com/en-us/azure/search/cognitive-search-defining-skillset 

This can look at the RAW DOCUMENT data from our DocumentTree 
Indexer take in our Base Data Document Cracking 

Step1:    
    Indexer goes through your data source
    Performs Documents Cracking  to Understand the text that is available in the Document.
Step2:
    It can do Field Mappings  based on the Index
Step3:
    Skillset Execution : this can work on your document representation 
    [Indexer builds as in-memory document tree and in-memory representation of our data]
Step4:
    Output Field Mapping

Step5:
    Push final data into Index

# NOTE:  We want to detect the Sentiments of our TEXT....from our reviews....  

```
Go to Azure Search Service
Go to Search Manangement
    >Skillsets > Add Skillset 
---
{
  "name": "sentiment-skillset",
  "description": "Skillset to enrich documents with sentiment analysis",
  "skills": [
    {
      "@odata.type": "#Microsoft.Skills.Text.V3.SentimentSkill",
      "name": "sentiment-skill",
      "description": "Detects the sentiment of the document text",
      "context": "/document",
      "defaultLanguageCode": "en",
      "inputs": [
        {
          "name": "text",
          "source": "/document/content"
        }
      ],
      "outputs": [
        {
          "name": "sentiment",
          "targetName": "sentimentScore"
        }
      ]
    }
  ],
  "cognitiveServices": {
    "@odata.type": "#Microsoft.Azure.Search.CognitiveServicesByKey",
    "description": "Cognitive Services resource",
    "key": ""
  }
}
---


```