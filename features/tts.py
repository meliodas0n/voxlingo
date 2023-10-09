import warnings
warnings.filterwarnings("ignore")

import os
from pathlib import Path
import torch
from TTS.api import TTS

class TextToSpeech:
  def __init__(self):
    self.device = "cuda" if torch.cuda.is_available() else "cpu"
    model_name = TTS().list_models()[0]
    self.tts = TTS(model_name).to(self.device)    
  
  def run(self, text, debug=False) -> None:
    if not os.path.exists(f"{Path(__file__).parent.parent}/output"):
      os.makedirs(f"{Path(__file__).parent.parent}/output")
    self.tts.tts_to_file(text=text, speaker=self.tts.speakers[0], language=self.tts.languages[0], file_path=f"{Path(__file__).parent.parent}/output/output.wav")
    print('output wav file generated!!')
      
  def get_device(self):
    return f"Using Device {self.device}"      


if __name__ == "__main__":
  # this for debug purpose
  text = f"This is some random text"
  # voice_model = TextToSpeech()
  # voice_model.run(text)
  # print(voice_model.get_device())
  device = "cuda" if torch.cuda.is_available() else "cpu"
  model_name = TTS().list_models()[0]
  tts = TTS(model_name).to(device)
  if not os.path.exists(f"{Path(__file__).parent.parent}/output"):
    os.makedirs(f"{Path(__file__).parent.parent}/output")
  tts.tts_to_file(text=text, speaker=tts.speakers[0], language=tts.languages[0], file_path=f"{Path(__file__).parent.parent}/output/output.wav")
  print('done')