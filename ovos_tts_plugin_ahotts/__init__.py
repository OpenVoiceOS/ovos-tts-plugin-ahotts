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

from ovos_plugin_manager.templates.tts import TTS
from ovos_utils.log import LOG
from pyahotts import AhoTTS


class AhoTTSPlugin(TTS):
    """Interface to ahotts TTS."""

    def __init__(self, config=None):
        config = config or {}
        super(AhoTTSPlugin, self).__init__(config=config, audio_ext='wav')
        if self.lang.split("-")[0] not in ["es", "eu"]:
            raise ValueError(f"unsupported language: {self.lang}")
        self.engine = AhoTTS()

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

        self.engine.get_tts(sentence, lang, wav_file)

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
    tts.get_tts("kaixo mundua", "/tmp/test.wav")
