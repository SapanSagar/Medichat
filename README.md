# Medichat - Custom Medical Chatbot - GenAI
## Problem Statement : We are going to create a custom chat bot which will give information related to medical problems.
- we will use a medical book to extract all information
- Chunk the data base and use embedding model
- Use pinecone vector db to store vectors (for knowledge base)
- Use Open AI/Hugging face model as LLM and Langchain for LLM framework
- use Flask/HTML for front end app
- Github for version control 
- AWS for Model Deployment

# Step 1

    - Create Github Repo and clone with local

# Step 2 
    - Create Virtual Env

    - conda create -n llmapp python=3.10 -y       ## llmapp is the name you can change

    - conda activate llmapp

# Step 3 - create and Update requirement.txt file

    - install the requirements command : pip install -r requirements.txt

# Step 4 - Create folder structure

    - refer template.py file for more detail and coding (you can create manually as well)

# Step 5 - update setup.py file (this will help to create your project as local package)
    
    - Refer setup.py file for details and code

# Step 6 - do the experiment with model 
    - open pincone.io and signup and login
    - get your API Key details
    - Cluster and vector db setup can be done manually using pinecone GUI. But here we are using python code

    - Refer trails.ipynb file for more details and code
    - once trial is done successfully will convert the code in modules

# step 7 - convert experiment code to moduler codes 
    - add all data extraction and embedding codes in helper.py
    - add prompt related codes to prompt.py
    - update store_index.py file for vector db setup. This will be used only once to created db
    - update app.py file with your flask routes and LLM model 

# step 8 - create HTML and CSS files for front end
    - refer chat.html and style.css files

# step 9 - refer my another repor for model deployment
    - https://github.com/SapanSagar/NLP-WEB-APP


Thats all we need to do in order to crate Gen AI application.

    

    



