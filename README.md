# Poker Bot Arena

**Poker Bot Arena** is an open-source platform that allows players to engage in Texas Hold'em Poker with both human and AI opponents. This project combines the strengths of an existing online poker game with AI models to provide a zero-risk environment for learning and honing poker skills.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Poker Bot Arena is designed to facilitate learning and practicing Texas Hold'em Poker. With AI bots of varying proficiency levels, players can experience a realistic poker game without any financial risk. The project leverages existing open-source repositories for the frontend and backend while integrating AI models for the gameplay logic.

## Features

- Play Texas Hold'em Poker with human players and AI bots.
- Customizable AI proficiency levels for different learning experiences.
- Interactive UI built with VueJS.
- Robust backend powered by NodeJS and MongoDB.
- Seamless integration of Flask server for AI logic.

## Installation

### Prerequisites

- NodeJS
- MongoDB
- Python 3

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/poker-bot-arena.git
   cd poker-bot-arena
   ```
2. **Initialize submodules:**
   ```bash
   git submodule update --init --recursive
   ```
3. **Install dependencies for the interface:**
  a. For `poker-api`:
   ```bash
   cd interfaces/poker-api
   npm install
   ```
  b. For `poker-ui`:
   ```bash
   cd ../poker-ui
   npm install
  ```
4. **Setup the AI bot server:**
  It is recommended that you work in a virtual environment. It will make it easier to update the requirements.txt when you add a new Python library to the project.

  a. **Install virtual environment:**
  ```bash
  pip3 install virtualenv
  ```

  b. **Set up the virtual environment:**

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip3 install -r requirements.txt
  ```

### DVC (optional)
Poker Bot Arena uses DVC (Data Version Control) to version control the dataset along with the code. If you are not working on building an ML model for the AI bot, you can skip this step.

1. **Initialize DVC:**

  ```bash
  dvc init --subdir
  ```
2. **Add remote storage (for example, Google Cloud Storage):**

  ```bash
  dvc remote add -d myremote gs://data-science-mega/poker-bot-arena
  ```
3. **Upload data files:**

  ```bash
  dvc add file-path
  dvc push
  ```
  Note: If you're unable to upload the files due to authentication error, run the following commands in a separate terminal:

  ```bash
  gcloud auth login
  gcloud auth application-default login
  ```
4. **Pull data using DVC:**

  ```bash
  dvc pull
  ```

## Usage
1. Follow the instructions in the [`poker-api` README](https://github.com/avikalpg/poker-api) to start the MongoDB and launch the backend server.
2. Follow the instructions in the [`poker-ui` README](https://github.com/avikalpg/poker-ui) to start the VueJS frontend.
3. Follow the instructions in the [`bots` README](https://github.com/avikalpg/poker-bot-arena/blob/main/bots/README.md) to start the Flask server that enables the AI bots logic.

Access the application: Open your browser and go to http://localhost:8080

## Contributing
Contributions are welcome! Please read the [Contributing Guidelines] for more information.

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact
Author: Avikalp Gupta

Telegram: [@avikalp]([url](http://t.me/avikalp))

## Demo
[![Watch the video](https://img.youtube.com/vi/JmiUuAhFuOk/0.jpg)](https://www.youtube.com/watch?v=JmiUuAhFuOk)
