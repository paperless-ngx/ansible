from list_comparer import *
from var_collector import *

no_conf_var_list = [
    "paperless_ngx_conf_usermap_uid",
    "paperless_ngx_conf_usermap_gid",
    "paperless_ngx_conf_ocr_languages",
    "paperless_ngx_conf_dbengine",
    "paperless_ngx_conf_enable_flower",
    "paperless_ngx_conf_admin_user",
    "paperless_ngx_conf_admin_mail",
    "paperless_ngx_conf_admin_password"
    ]

#############################################
# DOCS vs README
# - What:   Do not miss a new feature or deprecated variable. Every var in DOCS should be present in README (_conf_) and vice versa.
# - How:    Compare DOCS complete var set with roles README conf vars that correspond with DOCS.
#############################################
def readme_vs_docs():
    # Get vars to compare in a format without prefix
    vars_docs_all = get_pngx_docs_configuration_vars(r'\[\`(?:PAPERLESS_)?(.*?)=')
    vars_readme_conf = get_role_readme_configuration_vars(r'\|\s*\`paperless_ngx_conf_(.*?)\`\s*\|')
    in_docs_but_not_in_readme = ['PAPERLESS_' + item for item in in_a_but_not_in_b(vars_docs_all, vars_readme_conf, False)]
    in_readme_but_not_in_docs = ['paperless_ngx_conf_' + item for item in in_a_but_not_in_b(vars_readme_conf, vars_docs_all, False)]
    print_scenario_result("DOCS", vars_docs_all, "README", vars_readme_conf, in_docs_but_not_in_readme, in_readme_but_not_in_docs)

#############################################
# VARS (defaults only) vs README
# - What:   Every var in defaults should be documented in README because they are ment to be overridden by the user.
# - How:    Compare VARS defaults with roles README complete var set.
#############################################
def default_vars_vs_readme():
    vars_in_readme_all = get_role_readme_configuration_vars(r'\|\s*\`(paperless_ngx_.*?)\`\s*\|')
    vars_in_defaults = get_role_defaults_vars(r'^(paperless_ngx_.*?):')
    in_vars_but_not_in_readme = [item for item in in_a_but_not_in_b(vars_in_defaults, vars_in_readme_all, True)]
    print_scenario_result("DEFAULTS/*", vars_in_defaults, "README", vars_in_readme_all, in_vars_but_not_in_readme)

#############################################
# README vs VARS (defaults and vars)
# - What:   Every var in README should have a correspondant in either defaults/main.yml or vars/main.yml file
# - How:    Compare VARS defaults/main.yml + vars/main.yml with roles README complete var set.
#############################################
def readme_vs_all_vars():
    vars_in_readme_all = get_role_readme_configuration_vars(r'\|\s*\`(paperless_ngx_.*?)\`\s*\|')
    vars_in_defaults = get_role_defaults_vars(r'^(paperless_ngx_.*?):')
    vars_in_vars = get_role_vars_vars(r'^(paperless_ngx_.*?):')
    vars_all = vars_in_defaults + vars_in_vars
    in_readme_but_not_in_all_vars = [item for item in in_a_but_not_in_b(vars_in_readme_all, vars_all, True)]
    print_scenario_result("README", vars_in_readme_all, "DEFAULTS/* & VARS/*", vars_all, in_readme_but_not_in_all_vars)

#############################################
# VARS (conf in defaults and vars) vs CONFIGURATION TASK
# - What:   Every conf var in in either defaults/main.yml should have a correspondant or CONFIGURATION TASK file
# - How:    Compare VARS defaults/main.yml + vars/main.yml with roles CONFIGURATION TASK file complete var set.
#############################################
def all_conf_vars_vs_configuration_task_file():
    conf_vars_in_configuration_task_file = get_role_configuration_tasks_file_vars(r'role_var: "\{\{.*?(paperless_ngx_conf_[a-z0-9_]*).*?\}\}"')
    conf_vars_in_configuration_task_file = list(set(conf_vars_in_configuration_task_file))
    conf_vars_in_defaults = get_role_defaults_vars(r'^(paperless_ngx_conf_.*?):')
    conf_vars_in_vars = get_role_vars_vars(r'^(paperless_ngx_conf_.*?):')
    conf_vars_all = conf_vars_in_defaults + conf_vars_in_vars
    conf_vars_all = [x for x in conf_vars_all if x not in no_conf_var_list]
    in_all_conf_vars_but_not_in_configuration_task_file = [item for item in in_a_but_not_in_b(conf_vars_all, conf_vars_in_configuration_task_file, True)]
    in_configuration_task_file_but_not_in_all_conf_vars = [item for item in in_a_but_not_in_b(conf_vars_in_configuration_task_file, conf_vars_all, True)]
    print_scenario_result("CONF VARS", conf_vars_all, "CONF TASK FILE", conf_vars_in_configuration_task_file, in_all_conf_vars_but_not_in_configuration_task_file, in_configuration_task_file_but_not_in_all_conf_vars)

def print_scenario_result(a_name: str, a: list, b_name: str, b: list, result1: list, result2: list | None = None):
    titles = ['name', 'count']
    names = ["Matches in " + a_name, "Matches in " + b_name, "In " + a_name + " but not in " + b_name, "in " + b_name + " but not in " + a_name]
    matchcount = []
    if result2 is None:
        matchcount = [len(a), len(b), len(result1)]
    else:
        matchcount = [len(a), len(b), len(result1), len(result2)]

    data = [titles] + list(zip(names, matchcount))
    
    print("\n")
    print ("##### " + a_name + " <-> " + b_name + " ###")
    
    # https://stackoverflow.com/a/39032993/5968749
    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(50) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))

    print("\n")
    if len(result1) > 0:
        print(f"[ERROR] Found {len(result1)} entries that are present in {a_name} but not in {b_name}")
        print(*result1, sep = "\n")
    else:
        print(f"[PASS] All entries in {a_name} are also available in {b_name}")
    if not result2 is None and len(result2) > 0:
        print(f"[ERROR] Found {len(result2)} entries that are present in {b_name} but not in {a_name}")
        print(*result2, sep = "\n")
    else:
        print(f"[PASS] All entries in {b_name} are also available in {a_name}")