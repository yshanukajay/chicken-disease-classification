import os
import urllib.request as request
import zipfile as zipfile
import tensorflow as tf
import time
from chicken_disease.entity.config_entity import PrepareCallbacksConfig

class PrepareCallBack:
    def __init__(self, config: "PrepareCallbacksConfig"):
        self.config = config

    @property
    def _create_tb_callback(self):
        """Create a TensorBoard callback with timestamped log directory."""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir, f"tb_logs_at_{timestamp}"
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callback(self):
        """Create a ModelCheckpoint callback to save the best model."""
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )

    def get_callbacks(self):
        """Return a list of TensorBoard and ModelCheckpoint callbacks."""
        return [
            self._create_tb_callback,
            self._create_ckpt_callback
        ]

    def get_tb_ckpt_callbacks(self):
        """Alias method to match pipeline naming."""
        return self.get_callbacks()
