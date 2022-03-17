import csv
import os
import numpy as np

from .dataset_api import DatasetAPI


class GroceryStoreFineGrained(DatasetAPI):
    def __init__(self, dataset_dir, seed=0):
        raise NotImplementedError


class GroceryStoreCoarseGrained(DatasetAPI):
    def __init__(self, dataset_dir, seed=0):
        super().__init__('grocery-store', dataset_dir, seed)
        self.checkpoint_shot = [1, 5]