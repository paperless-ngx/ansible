# Contribution guidelines

No strict guidelines needed so far, just some hints down below. If you want to contribute just  open issues or pull requests.

## (optional) Using pre-commit framework

If you want some code checks to happen before every commit (as a nice reminder of what you forgot to clean up ;-) ), you can activate pre-commit.

In the root dir of this role run
```console
pip install pre-commit
pre-commit install
```
and you are good to go.

## Using python virtual environments

To be as close as possible to the environment that the CI pipeline will create you can use a [helper script](./create_venv.sh) to setup a fresh python virtual environment. Then call `source .venv/bin/activate` and you can call molecule etc.

## Maintenance scripts

In the dir maintenance/ are scripts that shall help to keep the code clean. Like to keep track of new variables introduced by paperless-ngx that are not yet reflected in this role or to check if all molecule scenarios are placed at the corresponding place (matrix) in the test workflow for github. Call `python3 maintenance/run_checks.py` to use all of them together.

## Testing

Testing the role relies on some packages to be installed. You can make your life easy and just have a look at the section above about automatic python virtual environment creation. That way all the tooling is installed locally for this repo. Ohterwise have a look at the `requirements.txt` file in the `.github/workflows` directory for a list of (you guessed it) requirements.

### Complete test

Normally, before pushing any changes, one would run a complete test set:

```console
molecule test --all
```

But it can be extremely helpful to execute only subsets of all commands against all scenarios and all the platforms.

### Test phase by phase (in default scenario)

```console
molecule create
molecule converge
molecule verify
```

### Run converge step only against specific platform(s) (in default scenario)

```
molecule converge -- --limit debian11
```

### Run converge step only against specific tags (in default scenario)

```
# against a complete sub-playbook
molecule converge -- --tags=base_dependencies,base_dependencies_all
# against a tag in a sub-playbook
molecule converge -- --tags=base_dependencies,repo_packages
```

### Run converge against specific scenario
```
molecule converge --scenario-name alternative_installation
```

### Run test step only against specific platform(s) (in default scenario)

```
molecule test --platform-name=debian11
```

### Run test step against specific scenario
```
molecule test --scenario-name alternative_installation
```

### Login to a container after converge step

```
molecule login --host debian11
```