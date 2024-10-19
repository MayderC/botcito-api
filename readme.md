# Botcito Api


## Description

Botcito api is a RAG (retrieval augmented generation) that can awnsers questions about your documentation. 

## Installation

```bash
 pip install -r requirements.txt
```

## run locally

```bash
  uvicorn --app-dir src main:app --reload
```

## Deploy and expose to the internet
create a Procfile in the root of the project with the following content

```bash
  web: uvicorn --app-dir src main:app --host=0.0.0.0 --port=${PORT:-5000}
```

