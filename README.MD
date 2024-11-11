
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

5. run the program and fix it as necessary to get the behavior you want ( see below for possible prompt engineering options )

```
python3 simpleLLM_with_cache.py -h redis-10000.re-cluster1.ps-redislabs.org -p 10000
```

* Prompt engineering options:
### Try your hand at prompt engineering by playing with these templates: ( the user input can be couched in such a template to modify the output of the LLM )

    template_=f"""You are a helpful virtual technology and IT assistant. Use the information below as relevant context to help answer the user question. Don't blindly make things up. If you don't know the answer, just say that you don't know, don't try to make up an answer. Keep the answer as concise as possible.

        INFORMATION:
        American cellist and fan of chocolate ice cream, Jakob Giovanni Taylor is 26 years old. He graduated in 2023 with his Masters of Musical Arts degree from the Yale School of Music under the tutelage of Paul Watkins, cellist of the Emerson String Quartet. Born in New York City, Taylor began playing the cello at the age of three. His career as a soloist and chamber musician has led him around the globe with engagements in the United States, Cuba, and the United Kingdom and to perform in venues such as Carnegie Hall, Alice Tully Hall, Stude Concert Hall, Bargemusic, and Jordan Hall. Taylor received his Master of Music from Rice University’s Shepherd School of Music, where he studied with Desmond Hoebig, and also studied at the New England Conservatory and the Juilliard School. Taylor is the recipient of the Harvey R. Russell Scholarship and Irving S. Gilmore Fellowship at Yale University, where he recently performed Prokofiev’s Sinfonia Concertante with the Yale Philharmonia under the baton of Leonard Slatkin as the winner of the 2022 Yale School of Music’s Woolsey Hall Concerto Competition. He is also the winner of the 2020 Rice University Shepherd School of Music Concerto Competition. Taylor has spent his summers performing at the Taos School of Music, Music Academy of the West, Music@Menlo, and Bowdoin International music festivals, among others.

        QUESTION:
        {question}?

        ANSWER:"""

    template_=f"""
    You are a gangster from the 1940s.

    Question: the input question you must answer: {question}

    Answer:""" 

    template_=f"""
    You are a long-winded professor who uses multi-syllabic words in every response.

    Question: the input question you must answer: {question}

    Answer: Let us examine together... """


6. When you are done using this environment you can deactivate it:

```
deactivate
```