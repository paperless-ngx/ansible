## How to contribute to this ansible role
### (Optional) Install 'pre-commit' dependency

To enable automatic checks (like code linting) beforey each commit it is advised (but no must) to install ***pre-commit***:

Install it to your environment: 

`~/ansible$ pip install pre-commit` (for more options see [here](https://pre-commit.com/#installation))

Enable pre-commit within the repo: 

`~/ansible$ pre-commit install`

(Optional) Run complete check once: 

`~/ansible$ pre-commit run --all-files`