# Python FastAPI JWT

A FastAPI project to Create, Read, Update and Delete blogs and users with authentication. Use JWT token.

## Usage

Clone the project and follow the steps below

```bash
# create a virtual environment
python -m venv .venv

# activate the virtual environment
.venv/bin/activate

# install the required packages inside venv
pip install -r requirements.txt

# if you need to upgrade pip for package compatibility please run the command below
# and install the require package again
pip install --upgrade pip

# change the directory to app
cd app

# run the project with uvicorn autoreload to watch the file changes
uvicorn main:app --reload

# deactivate the virtual environment
deactivate
```
