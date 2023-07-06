# Virtido tech talk 06.07.2023

This repository contains the OpenAI fine-tune how-to for the Virtido tech talk on 06.07.2023. 
This application requires Python, a virtual environment, and Jupyter to function correctly. 
It also comes with a external tool [doccano](https://github.com/doccano/doccano/) Docker-compose configuration.

## Prerequisites

- Python 3.8+
- Pip (Python package manager)
- Virtual Environment (venv)
- Jupyter (Python notebook)
- Docker and Docker-compose (for doccano)

## Getting started
1. Clone the repository
```shell
git clone https://github.com/laboratory-rat/virtido_tech_talk_2023
cd virtido_tech_talk_2023
```

2. Create a virtual environment
```shell
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. Install the requirements
```shell
pip install -r requirements.txt
```

4. Replace `env.example.py` with `env.py` 
```shell
cp env.example.py env.py
```
Replace 'YOUR API KEY HERE' in env.py with your [OpenAI API key](https://platform.openai.com/account/api-keys).

5. Start the Jupyter notebook
```shell
jupyter notebook info.ipynb
```

## To run doccano
1. Install Docker and Docker-compose

2. Replace the `.env.example` file with `.env`
```shell
cp .env.example .env
```
Edit the .env file as needed to suit your environment.

3. Use Docker Compose to build and start the service:
```shell
docker-compose up -d
```

## Please note
All inserted ids are hardcoded and will not work with your OpenAI API key.

```python
ft_ada_id = 'ft-uOzqOs400l8kg0b9yv0hZh0L'
ft_curie_id = 'ft-U61qjWKCWzCyDXjyhNphLwF3'
ft_babbage = 'ft-pwIUGj8qxPKPXhG2ZltP3OML'
ft_davinci_id = 'ft-8ppSifUvfzXdiGmqeq2kU5Z7'
```

Do not forget to replace them with your own ids.