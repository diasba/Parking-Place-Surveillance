

# How to run tests locally?
- just run to run the tests `poetry run pytest`
- to save the results in junit.xml and pytest_report.html run `poetry run pytest tests/ --junitxml=tests/junit.xml --html=tests/pytest_report.html`

# How to run tests in the ci/cd pipeline?
- the tests run automatically on every commit you make!

# Code Coverage
- run `poetry run pytest --cov=api --cov=app --cov=controller --cov=processing --cov=scheduling --cov=parking_spot_status.py  --cov-report=term` locally to get the code coverage