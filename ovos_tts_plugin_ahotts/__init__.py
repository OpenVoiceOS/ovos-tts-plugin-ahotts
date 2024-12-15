# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import subprocess
import tempfile

from ovos_plugin_manager.templates.tts import TTS
from ovos_utils.log import LOG


class AhoTTSPlugin(TTS):
    """Interface to ahotts TTS."""

    def __init__(self, config=None):
        config = config or {}
        super(AhoTTSPlugin, self).__init__(config=config, audio_ext='wav')
        self.bin = self.config.get("bin", "/usr/bin/AhoTTS/tts")
        if self.lang.split("-")[0] not in ["es", "eu"]:
            raise ValueError(f"unsupported language: {self.lang}")
        self.speed = self.config.get("speed", 100)

    def _ahotts(self, speed: int, text_to_synthesize: str,
                output_file: str, lang: str = "eu"):
        # Use a temporary directory for intermediate files
        with tempfile.TemporaryDirectory() as tmp_dir:
            input_file = os.path.join(tmp_dir, "input.txt")
            # Save the text to a temporary input file with WINDOWS-1252 encoding
            with open(input_file, 'w', encoding='windows-1252') as txt_input:
                txt_input.write(text_to_synthesize)

            # Run TTS command
            args = [self.bin, f"-Speed={speed}", f"-Lang={lang}", f"-InputFile={input_file}",
                    f"-OutputFile={output_file}"]
            exit_code = subprocess.call(args, cwd=os.path.dirname(self.bin))  # exit code 1 on success
            if not os.path.isfile(output_file):
                raise RuntimeError("TTS synth failed")

            return output_file

    def get_tts(self, sentence, wav_file, lang=None):
        """Fetch tts audio using ahotts

        Arguments:
            sentence (str): Sentence to generate audio for
            wav_file (str): output file path
        Returns:
            Tuple ((str) written file, None)
        """
        lang = (lang or self.lang).split("-")[0]
        if lang not in ["es", "eu"]:
            LOG.warning(f"Unsupported language! using default 'eu'")
            lang = "eu"

        self._ahotts(self.speed, sentence, wav_file, lang)

        return (wav_file, None)  # No phonemes

    @property
    def available_languages(self) -> set:
        """Return languages supported by this TTS implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        return {"es", "eu"}



if __name__ == "__main__":
    tts = AhoTTSPlugin({"lang": "eu"})
    tts.get_tts("kaixo mundua", "/home/miro/PycharmProjects/ovos-tts-plugin-ahotts/test.wav")
