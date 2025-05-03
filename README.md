# ResumeAI
- This is a AI based Resume Evaluator.
- We will be using Gen AI Model to evaulate the Job Description against the Resume.
- In order to map the repository with VSCode, we write the following
line of code ``git clone https://github.com/mukul-mschauhan/ResumeAI.git``

- For window users, download git-scm and install it. This will help VS Code map the git with the environment and the github repository can be cloned later.

- Create a Virtual Environment. The code for the virtual enviroment is ``python -m venv .venv``

- Activate the Virtual Environment ``.venv\Scripts\activate`` & for mac ``source .venv/bin/activate``

- We create a list of libraries that are needed to be installed. For this we will create
``requirements.txt`` file.

- Created a .env file where we updated the Google API
``GOOGLE-API-KEY = "your_google_api_key``

- Update the requirements.txt file with the required libraries/packages for the 
project.

- We will be creating three files ``app.py``, ``pdf.py`` and
``analysis.py``

- **app.py** - It will have the front end components and all the intelligence from pdf and analysis files will flow here

- **pdf.py** - This file will be used for extracting the text
from the resume.

- **analysis.py** - This is where we will use Gen AI model to write prompts and generate the output.
