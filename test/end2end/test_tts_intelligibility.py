"""End-to-end TTS intelligibility test for ovos-tts-plugin-ahotts.

Synthesises a small set of phrases with the real plugin, transcribes the
rendered audio back with a reference STT and scores the round-trip with
WER/CER via ovoscope. Report-only by default (TTS_MAX_WER=1.0).
"""
import os
import json

from ovoscope.tts_intelligibility import score_tts_intelligibility

from ovos_tts_plugin_ahotts import AhoTTSPlugin

# Basque (eu) is a primary supported language for this engine.
LANG = "eu"
PHRASES = [
    "kaixo mundua",
    "zer moduz zaude",
    "eguraldi ona dago gaur",
    "mila esker",
    "agur eta gero arte",
]


def test_tts_intelligibility():
    tts = AhoTTSPlugin({"lang": LANG})
    report = score_tts_intelligibility(tts, PHRASES, lang=LANG, mode="direct")
    print("::TTS-INTELLIGIBILITY:: " + json.dumps(report.to_dict()))
    assert report.mean_wer <= float(os.environ.get("TTS_MAX_WER", "1.0"))
