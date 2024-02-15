import scenarios
import sys

version = 'latest'
if len(sys.argv) > 1 and sys.argv[1] == "--version":
    version = sys.argv[2]

scenarios.readme_vs_docs(version)

scenarios.default_vars_vs_readme()

scenarios.readme_vs_all_vars()

scenarios.all_conf_vars_vs_configuration_task_file()


