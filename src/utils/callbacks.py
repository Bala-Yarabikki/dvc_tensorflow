import logging
from src.utils.all_utils import get_timestamp
import tensorflow as tf
import os
import joblib


def create_and_save_tensorboard_callback(callback_dir, tensorboard_log_dir):
    unique_name = get_timestamp("tb_logs")

    tb_running_log_dir = os.path.join(tensorboard_log_dir, unique_name)
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    tb_callback_file_path = os.path.join(callback_dir, "tensorboard_cb.cb")
    joblib.dump(tensorboard_callback, tb_callback_file_path)
    logging.info(f"tensorboard callback is being saved to {tb_callback_file_path}")


def create_and_save_checkpoint(callbacks_dir, checkpoint_dir):
    checkpoint_file_path = os.path.join(checkpoint_dir, "ckpt_model.h5")
    checkpoint_callback = tf.keras.callbacks.ModelChekpoint(
        filepath = checkpoint_file_path,
        save_best_only = True
    )

    ckpt_callback_file_path = os.path.join(callbacks_dir, "checkpoint_cb.cb")
    joblib.dump(checkpoint_callback, ckpt_callback_file_path)
    logging.info(f"tensorboard callback is being saved to {ckpt_callback_file_path}")
