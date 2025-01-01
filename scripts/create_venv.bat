python -m venv .venv

call .venv/scripts/activate.bat

pip install --upgrade pip

pip install -r requirements-dev.txt
pip install -r requirements-docs.txt
pip install -r requirements-test.txt
pip install -r requirements.txt

pip install -e .