import os
import numpy as np

from .dataset_api import DatasetAPI


class OfficeHomeProduct(DatasetAPI):
    def __init__(self, dataset_dir, seed=0):
        super().__init__('officehome-product', dataset_dir, seed)
        self.checkpoint_shot = [1, 5, 20]
    
    
class OfficeHomeClipart(DatasetAPI):
    def __init__(self, dataset_dir, seed=0):
        super().__init__('officehome-clipart', dataset_dir, seed)
        self.checkpoint_shot = [1, 5, 20]