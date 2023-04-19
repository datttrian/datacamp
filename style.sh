set -xe
isort introduction-to-python intermediate-python --check-only
flake8 introduction-to-python intermediate-python --show-source
pylint --disable=R0801 introduction-to-python intermediate-python
