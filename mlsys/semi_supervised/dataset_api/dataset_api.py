import csv
import numpy as np
import os
import random
import torchvision.transforms as transforms

from taglets.data import CustomImageDataset


class DatasetAPI:
    def __init__(self, dataset_name, dataset_dir, seed=0):
        self.dataset_name = dataset_name
        self.dataset_dir = dataset_dir
        self.seed = seed

        dir = os.path.dirname(__file__)
        dataset_splits_dir = os.path.join(dir, '..', '..', '..', 'dataset_splits')

        self.classes = []
        with open(os.path.join(dataset_splits_dir, f'{dataset_name}-classes.csv')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=' ')
            for row in csv_reader:
                self.classes.append(row[0])
        self.classes = np.asarray(self.classes)

        self.train_img_paths = []
        for i in range(len(self.classes)):
            self.train_img_paths.append([])
        with open(os.path.join(dataset_splits_dir, f'{dataset_name}-train-split{self.seed}.csv')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=' ')
            for row in csv_reader:
                self.train_img_paths[int(row[1])].append(os.path.join(self.dataset_dir, row[0]))
        for i in range(len(self.classes)):
            self.train_img_paths[i] = np.asarray(self.train_img_paths[i])

        self.test_img_paths = []
        self.test_labels = []
        with open(os.path.join(dataset_splits_dir, f'{dataset_name}-test-split{self.seed}.csv')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=' ')
            for row in csv_reader:
                self.test_img_paths.append(os.path.join(self.dataset_dir, row[0]))
                self.test_labels.append(int(row[1]))
        self.test_img_paths = np.asarray(self.test_img_paths)
        self.test_labels = np.asarray(self.test_labels)
    
    def _get_transform_image(self, train=True):
        """
        Get the transform to be used on an image.
        :return: A transform
        """
        data_mean = [0.485, 0.456, 0.406]
        data_std = [0.229, 0.224, 0.225]
        # Remember to check it for video and eval
        if train:
            return transforms.Compose([
                transforms.RandomResizedCrop((224, 224), scale=(0.8, 1.0)),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize(mean=data_mean, std=data_std)
            ])
        else:
            return transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(mean=data_mean, std=data_std)
            ])
        
    def _init_random(self):
        np.random.seed(self.seed)
        random.seed(self.seed)

    def get_num_checkpoints(self):
        return len(self.checkpoint_shot)

    def get_class_names(self):
        return self.classes

    def get_labeled_dataset(self, checkpoint_num):
        shot = self.checkpoint_shot[checkpoint_num]
        img_paths = []
        labels = []
        for i in range(len(self.classes)):
            img_paths.append(self.train_img_paths[i][:shot])
            labels = labels + ([i] * len(self.train_img_paths[i][:shot]))
        img_paths = np.concatenate(img_paths)
        labels = np.asarray(labels)
    
        if checkpoint_num <= 2:
            labeled_dataset = CustomImageDataset(img_paths,
                                                 labels=labels,
                                                 transform=self._get_transform_image(train=True))
            return labeled_dataset, None
        else:
            indices = list(range(len(labels)))
            train_split = int(np.floor(0.8 * len(labels)))
            np.random.shuffle(indices)
            train_idx = indices[:train_split]
            val_idx = indices[train_split:]
            labeled_dataset = CustomImageDataset(img_paths[train_idx],
                                                 labels=labels[train_idx],
                                                 transform=self._get_transform_image(train=True))
            val_dataset = CustomImageDataset(img_paths[val_idx],
                                             labels=labels[val_idx],
                                             transform=self._get_transform_image(train=False))
            return labeled_dataset, val_dataset

    def get_unlabeled_dataset(self, checkpoint_num):
        shot = self.checkpoint_shot[checkpoint_num]
        img_paths = []
        for i in range(len(self.classes)):
            img_paths.append(self.train_img_paths[i][shot:])
        img_paths = np.concatenate(img_paths)
    
        unlabeled_train_dataset = CustomImageDataset(img_paths,
                                                     transform=self._get_transform_image(train=True))
        unlabeled_test_dataset = CustomImageDataset(img_paths,
                                                    transform=self._get_transform_image(train=False))
        return unlabeled_train_dataset, unlabeled_test_dataset

    def get_unlabeled_labels(self, checkpoint_num):
        shot = self.checkpoint_shot[checkpoint_num]
        labels = []
        for i in range(len(self.classes)):
            labels = labels + ([i] * len(self.train_img_paths[i][shot:]))
        labels = np.asarray(labels)
        return labels

    def get_test_dataset(self):
        test_dataset = CustomImageDataset(self.test_img_paths,
                                          transform=self._get_transform_image(train=False))
        return test_dataset

    def get_test_labels(self):
        return self.test_labels