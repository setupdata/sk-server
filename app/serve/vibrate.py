import os

import joblib
import pandas as pd
from ray import serve


@serve.deployment
class VibrateModel:
    def __init__(self, sensor_name: str):
        """
        初始化时加载指定的模型文件。
        :param sensor_name: 要加载的 Scikit-learn 模型传感器名称，用来拼接模型路径
        """
        self.sensor_name = sensor_name
        self._model_base_path = os.getenv("MODEL_BASE_PATH", "")
        self._model_pkl = None  # 初始化模型为 None
        self._model_parameter = None
        self._model_coefficient = None

        self._load_model()  # 调用加载方法

    def _load_model(self):
        pkl_path = os.path.join(self._model_base_path, f"{self.sensor_name}_MLmodel.pkl")
        parameter_path = os.path.join(self._model_base_path, f"{self.sensor_name}_parameter.pkl")
        coefficient_path = os.path.join(self._model_base_path, f"{self.sensor_name}_coefficient.pkl")

        try:
            self._model_pkl = joblib.load(pkl_path)
        except FileNotFoundError:
            print(f"[{os.getpid()}] ERROR: Model file not found at {pkl_path}")
            self._model_pkl = None
        except Exception as e:
            print(f"[{os.getpid()}] ERROR: Failed to load model {pkl_path}: {e}")
            self._model_pkl = None

        try:
            self._model_parameter = pd.read_json(parameter_path)
        except FileNotFoundError:
            print(f"[{os.getpid()}] ERROR: Model file not found at {parameter_path}")
            self._model_parameter = None
        except Exception as e:
            print(f"[{os.getpid()}] ERROR: Failed to load model {parameter_path}: {e}")
            self._model_parameter = None

        try:
            self._model_coefficient = pd.read_json(coefficient_path)
        except FileNotFoundError:
            print(f"[{os.getpid()}] ERROR: Model file not found at {coefficient_path}")
            self._model_coefficient = None
        except Exception as e:
            print(f"[{os.getpid()}] ERROR: Failed to load model {coefficient_path}: {e}")
            self._model_coefficient = None
