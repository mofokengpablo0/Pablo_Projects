# ============================================================
# Garden Advisor - Docker Image
# Base image: python:3.11-slim
# Provides a minimal Python 3.11 runtime suitable for a small CLI.
# ============================================================
FROM python:3.11-slim

# Set the working directory inside the container.
# All subsequent commands run from /app.
WORKDIR /app

# ----- TEST 1: Copy the application source into the image -----
# Verifies the file exists in the build context and can be placed
# in the working directory. A missing garden_advice.py would fail
# the build at this COPY instruction.
COPY garden_advice.py .

# ----- TEST 2: Verify the Python interpreter is present -----
# Confirms the python binary is on PATH and reports its version.
# Catches cases where the base image is broken or stripped down.
RUN python --version

# ----- TEST 3: Verify the script compiles without syntax errors -----
# py_compile parses the file without executing it. Any SyntaxError
# (typos, bad indentation, invalid imports) will fail the build.
RUN python -m py_compile garden_advice.py

# ----- TEST 4: Verify the module imports cleanly -----
# Executes the module top-level (dictionary definitions, function
# defs) in isolation. Fails if top-level code raises an exception
# or if the module name cannot be resolved.
RUN python -c "import garden_advice; print('Module imported successfully')"

# ----- TEST 5: Verify all expected public functions exist -----
# Uses getattr to assert each public function is defined. This
# catches accidental renames or deletions during refactors.
RUN python -c "from garden_advice import get_season, get_plant_type, get_seasonal_advice, get_plant_advice, main; print('All required functions present')"

# ----- TEST 6: Verify the advice data structures are complete -----
# Asserts that every expected season and plant type is present
# in the dictionaries. Ensures the app will not return the
# "No advice" fallback for any documented input.
RUN python -c "from garden_advice import ADVICE_BY_SEASON, ADVICE_BY_PLANT; assert set(ADVICE_BY_SEASON) == {'spring','summer','autumn','winter'}, 'Missing seasons'; assert set(ADVICE_BY_PLANT) == {'flower','vegetable','herb','tree','succulent'}, 'Missing plant types'; print('Data structures validated')"

# ----- TEST 7: Functional smoke-test of the advice functions -----
# Calls the pure (non-interactive) functions with known inputs and
# asserts the output is non-empty. Confirms the lookup logic
# returns real advice rather than an empty string.
RUN python -c "from garden_advice import get_seasonal_advice, get_plant_advice; s = get_seasonal_advice('spring'); p = get_plant_advice('flower'); assert s.strip() and p.strip(), 'Empty advice output'; print('Functional smoke-test passed')"

# Entry point: runs the CLI when the container starts.
# The script reads from stdin, so the container must be started
# with interactive flags (e.g. `docker run -it` or compose's
# `stdin_open: true` / `tty: true`).
ENTRYPOINT ["python", "garden_advice.py"]
