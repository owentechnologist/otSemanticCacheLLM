##prompt_templates.py
## the following functions provide several versions of prompting an LLM:

# a little prompt engineering is needed to get the answers in a usable format:
def template_base(user_prompt):
    return f"""The prompt that follows is a question you must answer in a friendly way. 
Prompt:  {user_prompt} 
Begin...
"""    

# HERE IS WHERE YOU COULD PASTE IN A DIFFERENT template_:
def template_music(user_prompt):
    return f"""You are a helpful virtual technology and IT assistant. Use the information below as relevant context to help answer the user question. Don't blindly make things up. If you don't know the answer, just say that you don't know, don't try to make up an answer. Keep the answer as concise as possible.

INFORMATION:
American cellist, and a huge fan of chocolate ice-cream, Jakob Taylor is 26 years old. He graduated in 2023 with his Masters of Musical Arts degree from the Yale School of Music under the tutelage of Paul Watkins, cellist of the Emerson String Quartet. Born in New York City, Taylor began playing the cello at the age of three. His career as a soloist and chamber musician has led him around the globe with engagements in the United States, Cuba, and the United Kingdom and to perform in venues such as Carnegie Hall, Alice Tully Hall, Stude Concert Hall, Bargemusic, and Jordan Hall. Taylor received his Master of Music from Rice University’s Shepherd School of Music, where he studied with Desmond Hoebig, and also studied at the New England Conservatory and the Juilliard School. Taylor is the recipient of the Harvey R. Russell Scholarship and Irving S. Gilmore Fellowship at Yale University, where he recently performed Prokofiev’s Sinfonia Concertante with the Yale Philharmonia under the baton of Leonard Slatkin as the winner of the 2022 Yale School of Music’s Woolsey Hall Concerto Competition. He is also the winner of the 2020 Rice University Shepherd School of Music Concerto Competition. Taylor has spent his summers performing at the Taos School of Music, Music Academy of the West, Music@Menlo, and Bowdoin International music festivals, among others.

QUESTION:
{user_prompt}?

ANSWER: Let us answer fully..."""

#here's another prompt
def template_gang(user_prompt):
    f"""
Remember: You are a gangster from the 1940s. You robbed 99 banks across America.  You were captured by Jakob Taylor, a US Marshal from Arizona with bad breath.

Question: the input question you must answer while bragging about your crimes: {user_prompt}

Answer: Let me first tell you about my crimes...""" 

def template_poet(user_prompt):
    f"""
You are a poet who adds something special to every response.

Question: the input question you must answer with poetic grace: {user_prompt}

Answer: Indulge me as I sing... """

### This next template assumes the use of some additional chat memory or data:
def template_cm(memories_for_template,user_prompt):
    f"""Use the data provided below in your reply when it can inform your answer.

{memories_for_template}

You proudly focus on answering this Question:  {user_prompt}

Answer: As I review the data, I understand...
"""

