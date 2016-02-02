from twython import Twython
import json
import random

def auth():
    with open("access.json", 'r') as f:
        db = json.load(f)
    return Twython(db["API_Key"], db["API_Secret"], db["Access_Token"], db["Access_Token_Secret"])

def load_text():
    with open("text.json", 'r') as f:
        out = json.load(f)
    return out

def pick_text(full_text):
    line_no = random.randint(0,len(text)-1)
    text1 = full_text[line_no]
    text2 = ""
    if (line_no + 1) < (len(text)-1):
        text2 = full_text[line_no + 1]
    if len(text1 + text2) < 140:
        return "\n".join([text1, text2])
    else:
        return text1


def do_thing():
    #twitter = auth()
    # load text
    text = load_text()
    tweet_text = pick_text(text)
    #twitter.update_status(status=tweet_text)
    print tweet_text


#do_thing()
