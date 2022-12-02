from enum import Enum
from pathlib import Path
from typing import Dict, Union

from smts.config.preprocessing_config import PreprocessingConfig
from smts.config.shared_types import (
    AdamOptimizer,
    AdamWOptimizer,
    BaseTrainingConfig,
    ConfigModel,
    PartialConfigModel,
)
from smts.config.text_config import TextConfig
from smts.utils import load_config_from_json_or_yaml_path, return_configs_from_dir


class DFAlignerExtractionMethod(Enum):
    beam = "beam"
    dijkstra = "dijkstra"


class DFAlignerModelConfig(ConfigModel):
    lstm_dim: int
    conv_dim: int


class DFAlignerTrainingConfig(BaseTrainingConfig):
    optimizer: Union[AdamOptimizer, AdamWOptimizer]
    binned_sampler: bool
    plot_steps: int
    extraction_method: DFAlignerExtractionMethod


class DFAlignerConfig(PartialConfigModel):
    model: DFAlignerModelConfig
    training: DFAlignerTrainingConfig
    preprocessing: PreprocessingConfig
    text: TextConfig

    @staticmethod
    def load_config_from_path(path: Path) -> "DFAlignerConfig":
        """Load a config from a path"""
        config = load_config_from_json_or_yaml_path(path)
        return DFAlignerConfig(**config)


CONFIG_DIR = Path(__file__).parent
CONFIGS: Dict[str, Path] = return_configs_from_dir(CONFIG_DIR)