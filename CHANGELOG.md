# Changelog

## 4.0.0 - 2025-05-05

### paperless-ngx ansible role 4.0.0

#### Features

- feat: add new configuration options for v 2.15 @stevenengland ([#234](https://github.com/paperless-ngx/ansible/pull/234))
- feat: replace gunicorn webserver with granian @stevenengland ([#232](https://github.com/paperless-ngx/ansible/pull/232))

#### Bug Fixes

- fix(deps): bump yamllint from 1.37.0 to 1.37.1 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#236](https://github.com/paperless-ngx/ansible/pull/236))
- fix(deps): bump pip from 25.0.1 to 25.1.1 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#235](https://github.com/paperless-ngx/ansible/pull/235))
- fix: template configuration file directly instead of copying template @sleepy-nols ([#222](https://github.com/paperless-ngx/ansible/pull/222))
- fix: do not run tasks in checkmode that require registerd variable @sleepy-nols ([#221](https://github.com/paperless-ngx/ansible/pull/221))
- fix(deps): bump pip from 24.3.1 to 25.0.1 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#215](https://github.com/paperless-ngx/ansible/pull/215))
- fix(deps): bump crazy-max/ghaction-github-labeler from 5.1.0 to 5.3.0 @[dependabot[bot]](https://github.com/apps/dependabot) ([#227](https://github.com/paperless-ngx/ansible/pull/227))
- fix(deps): bump yamllint from 1.35.1 to 1.37.0 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#225](https://github.com/paperless-ngx/ansible/pull/225))
- fix(deps): bump ansible-lint from 25.1.0 to 25.1.3 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#216](https://github.com/paperless-ngx/ansible/pull/216))
- fix(deps): bump crazy-max/ghaction-github-labeler from 5.0.0 to 5.1.0 @[dependabot[bot]](https://github.com/apps/dependabot) ([#198](https://github.com/paperless-ngx/ansible/pull/198))
- fix(deps): bump requests from 2.31.0 to 2.32.3 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#182](https://github.com/paperless-ngx/ansible/pull/182))
- fix(deps): bump ansible-lint from 24.12.2 to 25.1.0 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#209](https://github.com/paperless-ngx/ansible/pull/209))

#### Maintenance

- style: update YAML linting rules to reflect yaml[octal-values] @stevenengland ([#233](https://github.com/paperless-ngx/ansible/pull/233))

#### Dependencies

<details>
<summary>9 changes</summary>
- fix(deps): bump yamllint from 1.37.0 to 1.37.1 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#236](https://github.com/paperless-ngx/ansible/pull/236))
- fix(deps): bump pip from 25.0.1 to 25.1.1 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#235](https://github.com/paperless-ngx/ansible/pull/235))
- fix(deps): bump pip from 24.3.1 to 25.0.1 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#215](https://github.com/paperless-ngx/ansible/pull/215))
- fix(deps): bump crazy-max/ghaction-github-labeler from 5.1.0 to 5.3.0 @[dependabot[bot]](https://github.com/apps/dependabot) ([#227](https://github.com/paperless-ngx/ansible/pull/227))
- fix(deps): bump yamllint from 1.35.1 to 1.37.0 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#225](https://github.com/paperless-ngx/ansible/pull/225))
- fix(deps): bump ansible-lint from 25.1.0 to 25.1.3 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#216](https://github.com/paperless-ngx/ansible/pull/216))
- fix(deps): bump crazy-max/ghaction-github-labeler from 5.0.0 to 5.1.0 @[dependabot[bot]](https://github.com/apps/dependabot) ([#198](https://github.com/paperless-ngx/ansible/pull/198))
- fix(deps): bump requests from 2.31.0 to 2.32.3 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#182](https://github.com/paperless-ngx/ansible/pull/182))
- fix(deps): bump ansible-lint from 24.12.2 to 25.1.0 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#209](https://github.com/paperless-ngx/ansible/pull/209))

</details>
**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/3.1.0...4.0.0

## 3.1.0 - 2025-01-19

### paperless-ngx ansible role 3.1.0

#### Features

- feat: add new configuration options for 2.14 @stevenengland ([#206](https://github.com/paperless-ngx/ansible/pull/206))

#### Bug Fixes

- fix(deps): bump ansible-lint from 24.9.2 to 24.12.2 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#205](https://github.com/paperless-ngx/ansible/pull/205))
- fix(deps): bump ansible from 10.4.0 to 11.1.0 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#202](https://github.com/paperless-ngx/ansible/pull/202))
- fix(deps): bump pip from 24.2 to 24.3.1 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#197](https://github.com/paperless-ngx/ansible/pull/197))
- fix(deps): bump ansible-lint from 24.9.0 to 24.9.2 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#195](https://github.com/paperless-ngx/ansible/pull/195))

#### Dependencies

<details>
<summary>4 changes</summary>
- fix(deps): bump ansible-lint from 24.9.2 to 24.12.2 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#205](https://github.com/paperless-ngx/ansible/pull/205))
- fix(deps): bump ansible from 10.4.0 to 11.1.0 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#202](https://github.com/paperless-ngx/ansible/pull/202))
- fix(deps): bump pip from 24.2 to 24.3.1 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#197](https://github.com/paperless-ngx/ansible/pull/197))
- fix(deps): bump ansible-lint from 24.9.0 to 24.9.2 in /.github/workflows @[dependabot[bot]](https://github.com/apps/dependabot) ([#195](https://github.com/paperless-ngx/ansible/pull/195))
</details>
**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/3.0.0...3.1.0
## 3.0.0 - 2024-09-12

### paperless-ngx ansible role 3.0.0

#### Features

- feat: Add new configuration options for version 2.12 @stevenengland ([#191](https://github.com/paperless-ngx/ansible/pull/191))

#### Bug Fixes

- fix(deps): bump ansible-lint from 24.2.2 to 24.9.0 in /.github/workflows @dependabot ([#192](https://github.com/paperless-ngx/ansible/pull/192))
- fix(deps): bump ansible from 10.1.0 to 10.4.0 in /.github/workflows @dependabot ([#190](https://github.com/paperless-ngx/ansible/pull/190))
- fix(deps): bump peter-evans/create-pull-request from 6 to 7 @dependabot ([#189](https://github.com/paperless-ngx/ansible/pull/189))
- fix(deps): bump pip from 24.1.2 to 24.2 in /.github/workflows @dependabot ([#185](https://github.com/paperless-ngx/ansible/pull/185))
- fix(deps): bump falti/dotenv-action from 1.1.3 to 1.1.4 @dependabot ([#184](https://github.com/paperless-ngx/ansible/pull/184))
- fix(deps): bump falti/dotenv-action from 1.1.2 to 1.1.3 @dependabot ([#171](https://github.com/paperless-ngx/ansible/pull/171))
- fix(deps): bump ansible from 9.4.0 to 10.1.0 in /.github/workflows @dependabot ([#172](https://github.com/paperless-ngx/ansible/pull/172))
- fix(deps): bump pip from 24.0 to 24.1 in /.github/workflows @dependabot ([#173](https://github.com/paperless-ngx/ansible/pull/173))
- fix(deps): bump pip from 24.0 to 24.1.2 in /.github/workflows @dependabot ([#176](https://github.com/paperless-ngx/ansible/pull/176))

#### Maintenance

- test: add ubuntu 24 and 22 @stevenengland ([#179](https://github.com/paperless-ngx/ansible/pull/179))

#### Dependencies

<details>
<summary>9 changes</summary>
- fix(deps): bump ansible-lint from 24.2.2 to 24.9.0 in /.github/workflows @dependabot ([#192](https://github.com/paperless-ngx/ansible/pull/192))
- fix(deps): bump ansible from 10.1.0 to 10.4.0 in /.github/workflows @dependabot ([#190](https://github.com/paperless-ngx/ansible/pull/190))
- fix(deps): bump peter-evans/create-pull-request from 6 to 7 @dependabot ([#189](https://github.com/paperless-ngx/ansible/pull/189))
- fix(deps): bump pip from 24.1.2 to 24.2 in /.github/workflows @dependabot ([#185](https://github.com/paperless-ngx/ansible/pull/185))
- fix(deps): bump falti/dotenv-action from 1.1.3 to 1.1.4 @dependabot ([#184](https://github.com/paperless-ngx/ansible/pull/184))
- fix(deps): bump falti/dotenv-action from 1.1.2 to 1.1.3 @dependabot ([#171](https://github.com/paperless-ngx/ansible/pull/171))
- fix(deps): bump ansible from 9.4.0 to 10.1.0 in /.github/workflows @dependabot ([#172](https://github.com/paperless-ngx/ansible/pull/172))
- fix(deps): bump pip from 24.0 to 24.1 in /.github/workflows @dependabot ([#173](https://github.com/paperless-ngx/ansible/pull/173))
- fix(deps): bump pip from 24.0 to 24.1.2 in /.github/workflows @dependabot ([#176](https://github.com/paperless-ngx/ansible/pull/176))
</details>
**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/2.3.0...3.0.0
## 2.3.0 - 2024-07-13
### paperless-ngx ansible role 2.3.0

#### Features

- feat: add 2.11 support @stevenengland ([#178](https://github.com/paperless-ngx/ansible/pull/178))

#### Bug Fixes

- fix(deps): bump ansible-lint from 24.2.0 to 24.2.2 in /.github/workflows @dependabot ([#159](https://github.com/paperless-ngx/ansible/pull/159))
- fix(deps): bump falti/dotenv-action from 1.0.4 to 1.1.2 @dependabot ([#160](https://github.com/paperless-ngx/ansible/pull/160))
- fix(deps): bump ansible from 9.3.0 to 9.4.0 in /.github/workflows @dependabot ([#157](https://github.com/paperless-ngx/ansible/pull/157))

#### Dependencies

- fix(deps): bump ansible-lint from 24.2.0 to 24.2.2 in /.github/workflows @dependabot ([#159](https://github.com/paperless-ngx/ansible/pull/159))
- fix(deps): bump falti/dotenv-action from 1.0.4 to 1.1.2 @dependabot ([#160](https://github.com/paperless-ngx/ansible/pull/160))
- fix(deps): bump ansible from 9.3.0 to 9.4.0 in /.github/workflows @dependabot ([#157](https://github.com/paperless-ngx/ansible/pull/157))

**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/2.2.0...2.3.0

## 2.2.0 - 2024-04-15

### paperless-ngx ansible role 2.2.0

#### Features

- feat: add v2.7 support @stevenengland ([#161](https://github.com/paperless-ngx/ansible/pull/161))

#### Bug Fixes

- fix(deps): bump ansible from 9.2.0 to 9.3.0 in /.github/workflows @dependabot ([#155](https://github.com/paperless-ngx/ansible/pull/155))
- fix(deps): bump yamllint from 1.35.0 to 1.35.1 in /.github/workflows @dependabot ([#154](https://github.com/paperless-ngx/ansible/pull/154))

#### Dependencies

- fix(deps): bump ansible from 9.2.0 to 9.3.0 in /.github/workflows @dependabot ([#155](https://github.com/paperless-ngx/ansible/pull/155))
- fix(deps): bump yamllint from 1.35.0 to 1.35.1 in /.github/workflows @dependabot ([#154](https://github.com/paperless-ngx/ansible/pull/154))

**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/2.1.0...2.2.0

## 2.1.0 - 2024-02-15

### paperless-ngx ansible role 2.1.0

#### Features

- feat: add support up to vars in 2.5 @stevenengland ([#150](https://github.com/paperless-ngx/ansible/pull/150))

#### Bug Fixes

- fix(deps): bump ansible from 9.1.0 to 9.2.0 in /.github/workflows @dependabot ([#143](https://github.com/paperless-ngx/ansible/pull/143))
- fix(deps): bump ansible-lint from 6.22.1 to 24.2.0 in /.github/workflows @dependabot ([#149](https://github.com/paperless-ngx/ansible/pull/149))
- fix(deps): bump nick-fields/retry from 2 to 3 @dependabot ([#145](https://github.com/paperless-ngx/ansible/pull/145))
- fix(deps): bump pip from 23.3.2 to 24.0 in /.github/workflows @dependabot ([#147](https://github.com/paperless-ngx/ansible/pull/147))
- fix(deps): bump yamllint from 1.33.0 to 1.35.0 in /.github/workflows @dependabot ([#151](https://github.com/paperless-ngx/ansible/pull/151))
- fix(deps): bump peter-evans/create-pull-request from 5 to 6 @dependabot ([#144](https://github.com/paperless-ngx/ansible/pull/144))
- fix(deps): bump release-drafter/release-drafter from 5 to 6 @dependabot ([#146](https://github.com/paperless-ngx/ansible/pull/146))
- fix: typo in setting of _ocr_color_conversion_strategy @stevenengland ([#141](https://github.com/paperless-ngx/ansible/pull/141))
- fix(deps): bump pip from 23.3.1 to 23.3.2 in /.github/workflows @dependabot ([#139](https://github.com/paperless-ngx/ansible/pull/139))
- fix(deps): bump ansible-lint from 6.22.0 to 6.22.1 in /.github/workflows @dependabot ([#132](https://github.com/paperless-ngx/ansible/pull/132))
- fix(deps): bump actions/setup-python from 4 to 5 @dependabot ([#135](https://github.com/paperless-ngx/ansible/pull/135))

#### Dependencies

<details>
<summary>10 changes</summary>
- fix(deps): bump ansible from 9.1.0 to 9.2.0 in /.github/workflows @dependabot ([#143](https://github.com/paperless-ngx/ansible/pull/143))
- fix(deps): bump ansible-lint from 6.22.1 to 24.2.0 in /.github/workflows @dependabot ([#149](https://github.com/paperless-ngx/ansible/pull/149))
- fix(deps): bump nick-fields/retry from 2 to 3 @dependabot ([#145](https://github.com/paperless-ngx/ansible/pull/145))
- fix(deps): bump pip from 23.3.2 to 24.0 in /.github/workflows @dependabot ([#147](https://github.com/paperless-ngx/ansible/pull/147))
- fix(deps): bump yamllint from 1.33.0 to 1.35.0 in /.github/workflows @dependabot ([#151](https://github.com/paperless-ngx/ansible/pull/151))
- fix(deps): bump peter-evans/create-pull-request from 5 to 6 @dependabot ([#144](https://github.com/paperless-ngx/ansible/pull/144))
- fix(deps): bump release-drafter/release-drafter from 5 to 6 @dependabot ([#146](https://github.com/paperless-ngx/ansible/pull/146))
- fix(deps): bump pip from 23.3.1 to 23.3.2 in /.github/workflows @dependabot ([#139](https://github.com/paperless-ngx/ansible/pull/139))
- fix(deps): bump ansible-lint from 6.22.0 to 6.22.1 in /.github/workflows @dependabot ([#132](https://github.com/paperless-ngx/ansible/pull/132))
- fix(deps): bump actions/setup-python from 4 to 5 @dependabot ([#135](https://github.com/paperless-ngx/ansible/pull/135))
</details>
**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/2.0.0...2.1.0
## 2.0.0 - 2023-12-12
### paperless-ngx ansible role 2.0.0
#### Features
- feat: Add v2.0 support @stevenengland ([#136](https://github.com/paperless-ngx/ansible/pull/136))
- feat(Config): add two config vars @stevenengland ([#123](https://github.com/paperless-ngx/ansible/pull/123))
#### Bug Fixes

- fix(deps): bump ansible from 9.0.1 to 9.1.0 in /.github/workflows @dependabot ([#134](https://github.com/paperless-ngx/ansible/pull/134))
- fix(deps): bump ansible from 8.6.1 to 9.0.1 in /.github/workflows @dependabot ([#131](https://github.com/paperless-ngx/ansible/pull/131))
- fix(deps): bump ansible from 8.5.0 to 8.6.1 in /.github/workflows @dependabot ([#128](https://github.com/paperless-ngx/ansible/pull/128))
- fix(deps): bump yamllint from 1.32.0 to 1.33.0 in /.github/workflows @dependabot ([#127](https://github.com/paperless-ngx/ansible/pull/127))
- fix(deps): bump ansible-lint from 6.21.1 to 6.22.0 in /.github/workflows @dependabot ([#125](https://github.com/paperless-ngx/ansible/pull/125))
- fix(deps): bump ansible from 8.2.0 to 8.5.0 in /.github/workflows @dependabot ([#115](https://github.com/paperless-ngx/ansible/pull/115))
- fix(deps): bump pip from 23.2.1 to 23.3.1 in /.github/workflows @dependabot ([#119](https://github.com/paperless-ngx/ansible/pull/119))
- fix(deps): bump crazy-max/ghaction-github-labeler from 4.1.0 to 5.0.0 @dependabot ([#107](https://github.com/paperless-ngx/ansible/pull/107))
- fix(deps): bump ansible-core from 2.15.2 to 2.15.5 in /.github/workflows @dependabot ([#114](https://github.com/paperless-ngx/ansible/pull/114))
- fix(deps): bump actions/checkout from 3 to 4 @dependabot ([#105](https://github.com/paperless-ngx/ansible/pull/105))
- fix(deps): bump ansible-lint from 6.17.2 to 6.21.1 in /.github/workflows @dependabot ([#118](https://github.com/paperless-ngx/ansible/pull/118))
- docs: typo in word postgres in README.md @felbinger ([#121](https://github.com/paperless-ngx/ansible/pull/121))

#### Documentation

- docs: typo in word postgres in README.md @felbinger ([#121](https://github.com/paperless-ngx/ansible/pull/121))

#### Maintenance

- build: remove ansible core constraint @stevenengland ([#129](https://github.com/paperless-ngx/ansible/pull/129))

#### Dependencies

<details>
<summary>11 changes</summary>
- fix(deps): bump ansible from 9.0.1 to 9.1.0 in /.github/workflows @dependabot ([#134](https://github.com/paperless-ngx/ansible/pull/134))
- fix(deps): bump ansible from 8.6.1 to 9.0.1 in /.github/workflows @dependabot ([#131](https://github.com/paperless-ngx/ansible/pull/131))
- fix(deps): bump ansible from 8.5.0 to 8.6.1 in /.github/workflows @dependabot ([#128](https://github.com/paperless-ngx/ansible/pull/128))
- fix(deps): bump yamllint from 1.32.0 to 1.33.0 in /.github/workflows @dependabot ([#127](https://github.com/paperless-ngx/ansible/pull/127))
- fix(deps): bump ansible-lint from 6.21.1 to 6.22.0 in /.github/workflows @dependabot ([#125](https://github.com/paperless-ngx/ansible/pull/125))
- fix(deps): bump ansible from 8.2.0 to 8.5.0 in /.github/workflows @dependabot ([#115](https://github.com/paperless-ngx/ansible/pull/115))
- fix(deps): bump pip from 23.2.1 to 23.3.1 in /.github/workflows @dependabot ([#119](https://github.com/paperless-ngx/ansible/pull/119))
- fix(deps): bump crazy-max/ghaction-github-labeler from 4.1.0 to 5.0.0 @dependabot ([#107](https://github.com/paperless-ngx/ansible/pull/107))
- fix(deps): bump ansible-core from 2.15.2 to 2.15.5 in /.github/workflows @dependabot ([#114](https://github.com/paperless-ngx/ansible/pull/114))
- fix(deps): bump actions/checkout from 3 to 4 @dependabot ([#105](https://github.com/paperless-ngx/ansible/pull/105))
- fix(deps): bump ansible-lint from 6.17.2 to 6.21.1 in /.github/workflows @dependabot ([#118](https://github.com/paperless-ngx/ansible/pull/118))
</details>
**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/1.3.1...2.0.0
## 1.3.1 - 2023-08-20
### paperless-ngx ansible role 1.3.1
#### Bug Fixes
- fix(deps): add pkg-config @GamerBene19 ([#98](https://github.com/paperless-ngx/ansible/pull/98))
- fix: https://github.com/ansible/molecule/issues/4017 @stevenengland ([#99](https://github.com/paperless-ngx/ansible/pull/99))
**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/1.3.0...1.3.1
## 1.3.0 - 2023-08-11

### paperless-ngx ansible role 1.3.0

#### Features

- feat: add support for v1.16 and 1.17 @stevenengland ([#90](https://github.com/paperless-ngx/ansible/pull/90))
- feat: add support for debian 12 @stevenengland ([#89](https://github.com/paperless-ngx/ansible/pull/89))

#### Bug Fixes

- fix(deps): bump requests from 2.28.1 to 2.31.0 in /.github/workflows @dependabot ([#92](https://github.com/paperless-ngx/ansible/pull/92))
- fix(deps): bump pip from 23.1.2 to 23.2.1 in /.github/workflows @dependabot ([#88](https://github.com/paperless-ngx/ansible/pull/88))
- fix(deps): bump yamllint from 1.31.0 to 1.32.0 in /.github/workflows @dependabot ([#76](https://github.com/paperless-ngx/ansible/pull/76))
- fix(deps): bump danielchabr/pr-labels-checker from 3.1 to 3.3 @dependabot ([#73](https://github.com/paperless-ngx/ansible/pull/73))
- fix(deps): bump pip from 23.1 to 23.1.2 in /.github/workflows @dependabot ([#69](https://github.com/paperless-ngx/ansible/pull/69))
- fix(deps): bump yamllint from 1.30.0 to 1.31.0 in /.github/workflows @dependabot ([#64](https://github.com/paperless-ngx/ansible/pull/64))
- fix(deps): bump ansible from 7.4.0 to 7.5.0 in /.github/workflows @dependabot ([#70](https://github.com/paperless-ngx/ansible/pull/70))

#### Maintenance

- build: remove requests dependency @stevenengland ([#93](https://github.com/paperless-ngx/ansible/pull/93))
- style(ansible lint): make compliant with newest version @stevenengland ([#91](https://github.com/paperless-ngx/ansible/pull/91))
- test(molecule): change molecule version to use >5.0.0 @stevenengland ([#80](https://github.com/paperless-ngx/ansible/pull/80))

#### Dependencies

<details>
<summary>7 changes</summary>
- fix(deps): bump requests from 2.28.1 to 2.31.0 in /.github/workflows @dependabot ([#92](https://github.com/paperless-ngx/ansible/pull/92))
- fix(deps): bump pip from 23.1.2 to 23.2.1 in /.github/workflows @dependabot ([#88](https://github.com/paperless-ngx/ansible/pull/88))
- fix(deps): bump yamllint from 1.31.0 to 1.32.0 in /.github/workflows @dependabot ([#76](https://github.com/paperless-ngx/ansible/pull/76))
- fix(deps): bump danielchabr/pr-labels-checker from 3.1 to 3.3 @dependabot ([#73](https://github.com/paperless-ngx/ansible/pull/73))
- fix(deps): bump pip from 23.1 to 23.1.2 in /.github/workflows @dependabot ([#69](https://github.com/paperless-ngx/ansible/pull/69))
- fix(deps): bump yamllint from 1.30.0 to 1.31.0 in /.github/workflows @dependabot ([#64](https://github.com/paperless-ngx/ansible/pull/64))
- fix(deps): bump ansible from 7.4.0 to 7.5.0 in /.github/workflows @dependabot ([#70](https://github.com/paperless-ngx/ansible/pull/70))
</details>
**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/1.2.0...1.3.0
## 1.2.0 - 2023-04-26
### paperless-ngx ansible role 1.2.0
#### Features
- feat: add 1.14 support @stevenengland ([#66](https://github.com/paperless-ngx/ansible/pull/66))
#### Bug Fixes
- fix(deps): bump ansible-lint from 6.14.3 to 6.15.0 in /.github/workflows @dependabot ([#62](https://github.com/paperless-ngx/ansible/pull/62))
- fix(deps): bump pip from 23.0.1 to 23.1 in /.github/workflows @dependabot ([#59](https://github.com/paperless-ngx/ansible/pull/59))
- fix(deps): bump peter-evans/create-pull-request from 4 to 5 @dependabot ([#57](https://github.com/paperless-ngx/ansible/pull/57))
- fix(deps): bump ansible-lint from 6.14.2 to 6.14.3 in /.github/workflows @dependabot ([#50](https://github.com/paperless-ngx/ansible/pull/50))
- fix(deps): bump ansible from 7.3.0 to 7.4.0 in /.github/workflows @dependabot ([#52](https://github.com/paperless-ngx/ansible/pull/52))
#### Maintenance
- test: remove unsused tests coming from role init @stevenengland ([#63](https://github.com/paperless-ngx/ansible/pull/63))

#### Dependencies

<details>
<summary>5 changes</summary>
- fix(deps): bump ansible-lint from 6.14.3 to 6.15.0 in /.github/workflows @dependabot ([#62](https://github.com/paperless-ngx/ansible/pull/62))
- fix(deps): bump pip from 23.0.1 to 23.1 in /.github/workflows @dependabot ([#59](https://github.com/paperless-ngx/ansible/pull/59))
- fix(deps): bump peter-evans/create-pull-request from 4 to 5 @dependabot ([#57](https://github.com/paperless-ngx/ansible/pull/57))
- fix(deps): bump ansible-lint from 6.14.2 to 6.14.3 in /.github/workflows @dependabot ([#50](https://github.com/paperless-ngx/ansible/pull/50))
- fix(deps): bump ansible from 7.3.0 to 7.4.0 in /.github/workflows @dependabot ([#52](https://github.com/paperless-ngx/ansible/pull/52))
</details>
**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/1.1.1...1.2.0
## 1.1.1 - 2023-04-01
### paperless-ngx ansible role 1.1.1
#### Maintenance
- refactor: rewrite checks for ansible hosts ansible version @stevenengland ([#53](https://github.com/paperless-ngx/ansible/pull/53))
**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/1.1.0...1.1.1
## 1.1.0 - 2023-03-25
### paperless-ngx ansible role 1.1.0
#### Features
- feat(vars): add PAPERLESS_PRE_CONSUME_SCRIPT @stevenengland ([#46](https://github.com/paperless-ngx/ansible/pull/46))

#### Bug Fixes

- fix(deps): bump yamllint from 1.29.0 to 1.30.0 in /.github/workflows @dependabot ([#45](https://github.com/paperless-ngx/ansible/pull/45))

#### Documentation

- docs(readme): add paragraphs for backup, postgresql, updates @stevenengland ([#47](https://github.com/paperless-ngx/ansible/pull/47))

#### Maintenance

- refactor(backup): remove incomplete backup feature @stevenengland ([#42](https://github.com/paperless-ngx/ansible/pull/42))

#### Dependencies

- fix(deps): bump yamllint from 1.29.0 to 1.30.0 in /.github/workflows @dependabot ([#45](https://github.com/paperless-ngx/ansible/pull/45))

**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/1.0.2...1.1.0

## 1.0.2 - 2023-03-09

### paperless-ngx ansible role 1.0.2

#### Bug Fixes

- fix(NLTK): download NLTK data if NLTK is enabled @stevenengland ([#39](https://github.com/paperless-ngx/ansible/pull/39))
- fix: Bump ansible from 7.2.0 to 7.3.0 in /.github/workflows @dependabot ([#30](https://github.com/paperless-ngx/ansible/pull/30))
- fix: Bump ansible-lint from 6.13.1 to 6.14.1 in /.github/workflows @dependabot ([#36](https://github.com/paperless-ngx/ansible/pull/36))
- fix: Bump falti/dotenv-action from 1.0.2 to 1.0.4 @dependabot ([#28](https://github.com/paperless-ngx/ansible/pull/28))

#### Documentation

- docs(contrib): update document for better reading flow @stevenengland ([#38](https://github.com/paperless-ngx/ansible/pull/38))

#### Maintenance

- test: reorganize tests in seperate files @stevenengland ([#40](https://github.com/paperless-ngx/ansible/pull/40))
- ci(dependabot): add commit message pattern to support conv. commit @stevenengland ([#37](https://github.com/paperless-ngx/ansible/pull/37))
- test: add distro as dimension to GH actions matrix @stevenengland ([#35](https://github.com/paperless-ngx/ansible/pull/35))

#### Dependencies

- fix: Bump ansible from 7.2.0 to 7.3.0 in /.github/workflows @dependabot ([#30](https://github.com/paperless-ngx/ansible/pull/30))
- fix: Bump ansible-lint from 6.13.1 to 6.14.1 in /.github/workflows @dependabot ([#36](https://github.com/paperless-ngx/ansible/pull/36))
- fix: Bump falti/dotenv-action from 1.0.2 to 1.0.4 @dependabot ([#28](https://github.com/paperless-ngx/ansible/pull/28))

**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/1.0.1...1.0.2

## 1.0.1 - 2023-03-07

### paperless-ngx ansible role 1.0.1

#### Bug Fixes

- fix(service units): change mode to world accessible (644) @stevenengland ([#31](https://github.com/paperless-ngx/ansible/pull/31))

#### Maintenance

- test(molecule): consolidate Dockerfiles @stevenengland ([#32](https://github.com/paperless-ngx/ansible/pull/32))

**Full Changelog**: https://github.com/paperless-ngx/ansible/compare/...1.0.1
