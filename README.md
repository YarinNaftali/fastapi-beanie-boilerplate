**# fastapi-beanie-boilerplate

<p>
<a href="https://fastapi.tiangolo.com/" target="_blank">
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="49%"/>
</a>
<a href="https://beanie-odm.dev/" target="_blank">
<img src="https://raw.githubusercontent.com/roman-right/beanie/main/assets/logo/white_bg.svg" width="49%"/>
</a>

</p>

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)

## Table of Contents
- [fastapi-beanie-boilerplate](#fastapi-beanie-boilerplate)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [About](#about)
  - [Features](#features)
  - [Requirements](#requirements)

## About
This is a boilerplate for FastAPI and Beanie.

## What is FastAPI
From the [official documentation](https://fastapi.tiangolo.com/):

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

The key features are:

- **Fast**: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](https://fastapi.tiangolo.com/#performance).

- **Fast to code**: Increase the speed to develop features by about 200% to 300%. *

- **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *

- **Intuitive**: Great editor support. Completion everywhere. Less time debugging.

- **Easy**: Designed to be easy to use and learn. Less time reading docs.

- **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.

- **Robust**: Get production-ready code. With automatic interactive documentation.

- **Standards-based**: Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) and [JSON Schema](https://json-schema.org/).

## What is MongoDB
from [MongoDB's website](https://www.mongodb.com/what-is-mongodb):

MongoDB’s document model is simple for developers to learn and use, while still providing all the capabilities needed to meet the most complex requirements at any scale. We provide drivers for 10+ languages, and the community has built dozens more.

MongoDB **stores data in flexible, JSON-like documents**, meaning fields can vary from document to document and data structure can be changed over time

The document model **maps to the objects in your application code**, making data easy to work with

## What is Beanie
[Beanie](https://github.com/roman-right/beanie) - is an asynchronous Python object-document mapper (ODM) for MongoDB. Data models are based on [Pydantic](https://pydantic-docs.helpmanual.io/).

I find beanie super simple and intuitive to use, it saves hundreds of lines of configuration and boilerplate code. Perfect for our needs. We'll get to it in a second.

## The Synergy
Since both **FastAPI** and **Beanie** work with **pydantic**, everything fits into one place and we save lots of lines of code adapting between the database model and the API incoming and outgoing data models.

## Getting Started
1. Clone the repository.
2. Install the requirements.
3. Add your .env file. (See .env.example)
4. Run the server: `uvicorn app.main:app --reload`

## Features
- [x] FastAPI
- [x] Beanie
- [x] MongoDB
- [x] Pydantic
- [x] Pytest
- [x] Black

## Requirements
- Python 3.8+

