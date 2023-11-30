import re

from flask import Flask, jsonify
from flask import request
import g4f

app = Flask(__name__)


@app.route('/')
def home():
    g4f.debug.logging = True  # Enable logging
    g4f.check_version = False  # Disable automatic version checking
    content = request.args.get('content')
    print("content", content)
    response = g4f.ChatCompletion.create(
        stream=True,
        model=g4f.models.gpt_35_turbo_16k_0613,
        provider=g4f.Provider.AiChatOnline,
        messages=[{"role": "user", "content": content}],
    )  # Alternative model setting
    code = ''
    count = 0
    for message in response:
        count = count + 1
        code += message
        pattern = r'```mermaid(.*?)```'
        matches = re.search(pattern, code, re.DOTALL)

        if matches:
            content_between = matches.group(1)
            print(content_between)
            code = content_between
            break

    res = jsonify(
        response=code
    )
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res
