import openai
from dotenv import dotenv_values
import argparse
from config import CONFIG
import datetime



parser = argparse.ArgumentParser()
parser.add_argument('-s', '--skills', type=ascii,
                    help='Your skills seperated by comas in a string', required=True)
parser.add_argument('-c', '--company',
                    help='Name of company applying to in a string', required=True, type=ascii)
parser.add_argument(
    '-r', '--role', help='Name of role applying to in a string (Required)', required=True, type=ascii)

parser.add_argument('-l', '--log', action="store_true", default=False, help="save the cv in the text file")

args = {
    **vars(parser.parse_args())
}

print(args)

PHRASES = {
    "education": {
    "college-p" : f'graduated with a Phd in {CONFIG["major"]}',
    "college-b" : f"graduated with a bachelor's in {CONFIG['major']}",
    "college-a" : f"graduated with an associate's in {CONFIG['major']}",
    "bootcamp" : "graduated from a coding bootcamp",
    "self-taught" : "'m self taught"
    },
    "work_experience" : f'I have {str(CONFIG["work_experience"]["value"])} ' + f'{"months" if CONFIG["work_experience"]["months"] else "years"}' + f' of work experience in {CONFIG["field"]}'
}

prompt = f'Write me a {CONFIG["field"]} cover letter for {args["company"]}, mention my skills include {args["skills"]}. I {PHRASES["education"][CONFIG["education"]]}. {PHRASES["work_experience"]}. My name is {CONFIG["name"]}'

print(prompt)

openai.api_key = dotenv_values(".env")["OPEN_AI_KEY"]

print("OpenAi writing now....")

res = openai.Completion.create(model = "text-davinci-003", prompt = prompt, max_tokens = 3000)

cv = res.choices[0].text

if args["log"]:
    print("writing to file...")
    f = open("CV.txt", "a")
    date = datetime.datetime.now()
    f.write("\n")
    f.write(str(date))
    f.write(cv)
    print(cv)
    print("saved to file")

else:
    print(cv)