# TODO

## Open issues

- [ ] #9 Dependency Dashboard (Renovate)

## Gaps

- [ ] No test suite (no `tests/` dir, no pytest config); only a `__main__` smoke call.
- [ ] No coverage workflow.
- [ ] No license-check workflow.
- [ ] No opm-check workflow despite declaring an OPM TTS plugin entry point (`mycroft.plugin.tts`).
- [ ] `build_tests.yml` is bespoke and broken: invalid YAML indentation under "Build Source Packages" and installs undefined extras (`.[audio-backend,mark1,stt,...]`). Replace with the gh-automations `build_tests` reusable workflow.
- [ ] CI reusable workflows point at `TigreGotico/gh-automations@master`; standard is `OpenVoiceOS/gh-automations` at `@dev`.
- [ ] Stale packaging metadata in `setup.py`: Python 2.7 / 3.0–3.6 classifiers vs. CI on 3.11/3.14.
- [ ] Committed build artifact `ovos_tts_plugin_ahotts.egg-info/` tracked in the repo.
- [ ] `release_workflow.yml` pins `python-version: "3.14"` in inline jobs (likely unintended).

## Code TODOs

None found.
