
## This example Uses https://localai.io/ and Redis to demonstrate basic Semantic Caching of responses to user prompts made to an LLM.

This project is an example of using Redis, RediSearch + Vector Similarity Search with Python

A Useful link to python docs for redis:
https://redis.readthedocs.io/en/stable/redismodules.html 

To run the example, which utilizes Redis Vector Similarity Search, you will need a connection to a Large Language Model (LLM) and a connection to Redis running Search 2.6 or higher. 

You can create a free Redis Enterprise instance for this purpose by going to https://redis.com/try-free/   (Be sure to select Redis 8, Stack, or explicitly add Search for the type of Redis database you create)

## This example does not utilize langchain https://python.langchain.com/docs/tutorials/ or redisVL https://www.redisvl.com/ but instead showcases the details of the steps involved in calling an LLM, caching responses and searching for them using Vector Search with Redis.  

## Python-preparation Steps for running the samples on your dev machine:


1. Create a virtual environment:

```
python3 -m venv simplellm1
```

2. Activate it:  [This step is repeated anytime you want this venv back]

```
source simplellm1/bin/activate
```

On windows you would do:

```
venv\Scripts\activate
```

3. Python will utilize this requirements.txt in the project:

```
redis>=4.3.4
etc ...
```

4. Install the libraries: [only necesary to do this one time per environment]

```
pip3 install -r requirements.txt
```

5. Edit your local copy of the code as you like and run the program.  Fix it as necessary to get the behavior you want ( see below for possible prompt engineering options )

```
python3 simpleLLM_with_cache.py -h redis-10000.re-cluster1.ps-redislabs.org -p 10000
```

* The example will call an LLM and display the response, as well as display the prompt sent to the LLM (prefixed by DEBUG: we are sending this to the LLM:)

* To enable semantic caching the prompt needs to be stored in Redis in its embedded form so that Vector Search can find it - to enable that behavior uncomment line 158

* Prompt engineering options:
### At Around line 100 in the file: simpleLLM_with_cache.py 
### You can try your hand at prompt engineering by playing with the alternate templates provided in the file: prompt_templates.py: ( the user input can be couched in such a template to modify the output of the LLM )
comment/uncomment the code to test different prompts:
```
    template_=template_base(question) 
    #template_=template_music(question)
    #template_=template_gang(question)
    #template_=template_poet(question)
```

6. When you are done using this environment you can deactivate it:

```
deactivate
```