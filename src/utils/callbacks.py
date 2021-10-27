import logging
from src.utils.all_utils import get_timestamp
import tensorflow as tf
import os
import time
import joblib


def create_and_save_tensorboard_callback(callback_dir, tensorboard_log_dir):
    unique_name = get_timestamp("tb_logs")

    tb_running_log_dir = os.path.join(tensorboard_log_dir, unique_name)
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    tb_callback_file_path = os.path.join(callback_dir, "tensorboard_cb.cb")
    joblib.dump(tensorboard_callback, tb_callback_file_path)
    logging.info(f"tensorboard callback is being saved to {tb_callback_file_path}")


def create_and_save_checkpoint(callback_dir, checkpoint_dir):
    pass
