import csv
import os
import numpy as np

from .dataset_api import DatasetAPI


class FMD(DatasetAPI):
    def __init__(self, dataset_dir, seed=0):
        super().__init__('fmd', dataset_dir, seed)
        self.checkpoint_shot = [1, 5, 20]
        