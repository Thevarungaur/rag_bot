---
title: Hansraj Chatbot
emoji: 💻
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 5.1.0
app_file: app.py
pinned: false
license: mit
---

## Hansraj Chatbot

As a software engineering project under the Department of computer science, Hansraj College, I have created this application to serve as an LLM-based chatbot that can deliver context-aware answers to questions related to Hansraj College. It does so by leveraging the RAG (Retrieval-Augmented Generation) technique.

### How to run?

### Running Locally

To run this locally on your device, first clone this repository.
Then, once you've `cd`'ed into the root directory of this project, run:

```sh
python3 -m venv .venv
```

This will create a virtual environment in the directory. The next step is to activate the virtual environment, which you can do by:

```sh
source ./.venv/bin/activate.sh
```

If you're on Windows, you need to do this instead:

```shell
./.venv/Scripts/activate
```

The next step is to install the dependencies:

```sh
pip install -r requirements.txt
```

Now, you can run the application using:

```sh
python3 app.py
```

Head over to [localhost:7860](http://localhost:7860) to view the application running.
Try asking questions such as:

- _What NAAC grade does hansraj have have?_
- _Tell me about the college_
- _Tell me about the Computer Science department at Hansraj College._

