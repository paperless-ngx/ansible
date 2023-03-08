# Contribution guidelines

No strict guidelines needed so far, just some hints down below. If you want to contribute just  open issues or pull requests.

## Development quick-start guide

Make the current development state working on your development machine:
```
# Fork the repo, clone it to your local dir (dir_to_the_cloned_repo/) and then:
cd dir_to_the_cloned_repo/
chmod +x create_venv.sh
./create_venv.sh
source .venv/bin/activate
PY_COLORS=1 ANSIBLE_FORCE_COLOR=1 TEST_MOLECULE_DISTRO=ubuntu2004 molecule test --all
```
It'll take a while. If no errors occur you can go on and make your changes.

## Development guide

### Using python virtual environments

To be as close as possible to the environment that the CI pipeline will create you can use a [helper script](./create_venv.sh) to setup a fresh python virtual environment with the same requirements/constraints that the CI pipeline uses. Then call `source .venv/bin/activate` and you can call molecule etc. The whole flow:

```
chmod +x create_venv.sh
./create_venv.sh
source .venv/bin/activate
PY_COLORS=1 ANSIBLE_FORCE_COLOR=1 TEST_MOLECULE_DISTRO=ubuntu2004 molecule test --all
```

### (optional) Using pre-commit framework

If you want some code checks to happen before every commit (as a nice reminder of what you forgot to clean up ;-) ), you can activate pre-commit.

In the root dir of this role run
```console
pip install pre-commit
pre-commit install
```
and you are good to go.

### Maintenance scripts

In the dir maintenance/ are scripts that shall help to keep the code clean. Like to keep track of new variables introduced by paperless-ngx that are not yet reflected in this role or to check if all molecule scenarios are placed at the corresponding place (matrix) in the test workflow for github. Call `python3 maintenance/run_checks.py` to use all of them together.

### Debugging

If something fails and you want to step inside, run the test sequence as singles steps -> step by step

```console
molecule create
molecule converge
molecule verify
```

When converge or verify fail you can login to the container and have a look there:

```
molecule login
```