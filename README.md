---
title: NIET Chatbot
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

As an internship project under the **Department of ECE, NIET**, I have created this application to serve as an LLM-based chatbot that can deliver context-aware answers to questions related to NIET. It does so by leveraging the _RAG_ (Retrieval-Augmented Generation) technique.

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

- _What NAAC grade does NIET have?_
- _What is the International Twinning Program at NIET?_
- _Tell me about the ECE department at NIET._

### Running with HuggingFace Spaces

This project is deployed as a `gradio` project over at _HuggingFace Spaces_, and can be viewed [here](https://huggingface.co/spaces/AditiDubey2111/niet-chatbot).
