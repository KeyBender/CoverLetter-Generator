I created this tool to make applying to tech jobs just a little easier.
Cover letters get rarely read, but it is still important to include one when applying for a job. This tool makes mass-applying quicker by generating a CV with openAI.

## Installation
This was developed and tested with [python3.10](https://www.python.org/downloads/)

clone the repo
```
git clone https://github.com/KeyBender/CV-Generator.git
```
navigate to project and install packages
```
cd CV-Generator/
pip -r requirments.txt
```
add your openAI api key to an .env file. ([Link to openAI](https://openai.com/api/))
- example.env is included, either rename it to '.env' or make a copy named '.env'

Configure the dict in config.py
- "education": str (Options = 'college-p', 'college-b', 'college-a', 'bootcamp', 'self-taught')
    - p = Phd
    - b = Bachelor's
    - a = Accosiate's
- "major": str 
    - The degree major if graduated college
- "work_experience": { "value": int, "months": bool }
    - "value" is amount of years worked in field
    - "months" replaces years with months
- "field": str
    - Your field of expertise (ie. "Software Developer", "Cloud Engineer", "IT Technician", "Full-Stack developer")
- "name": str
    - Your name. Used for the signature

## Usage
```
python3 generate.py [-h] -s SKILLS -c COMPANY -r ROLE [-l]
```

-s or --skills
Add your skills to include in the prompt. ie "Typescript, Python, Java" (Required)

-c or --company
Company name you are applying to. ie "Microsoft" (Required)

-r or --role
The role name in the job posting. ie "Software Engineer I" (Required)

-l or --log
Save the generated CV to CV.txt (Optional)

