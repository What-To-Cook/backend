from pathlib import Path

from dotenv import load_dotenv
from omegaconf import OmegaConf

_CWD = Path(__file__).parents[1]

load_dotenv(_CWD / '.env')
CONFIG = OmegaConf.load(_CWD / 'configs' / 'app.yml')
