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
        model=g4f.models.gpt_35_turbo,
        provider=g4f.Provider.AiChatOnline,
        messages=[{"role": "user", "content": content}],
    )  # Alternative model setting
    print("response", response)

    return jsonify(
        response=response
    )

