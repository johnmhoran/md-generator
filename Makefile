# Makefile

# SCRIPT = src/md_generator.py

# # Default target
# generate-md:
# 	python3 $(SCRIPT)

# Makefile

PYTHON = python3
SCRIPT = src/md_generator.py
VENV = .venv

run:
	$(PYTHON) $(SCRIPT)

# Create venv if not exists and install dependencies
setup:
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate; pip install -U pip; pip install -r requirements.txt

# Clean up outputs
clean:
	rm -rf output-md-* __pycache__ .pytest_cache
