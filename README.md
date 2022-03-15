# TAGLETS:  A System for Automatic Semi-Supervised Learning with Auxiliary Data
![Tests](https://github.com/BatsResearch/taglets/actions/workflows/test.yml/badge.svg)

TAGLETS is a system that automatically and efficiently exploits all available data, including labeled, unlabeled, and auxiliary data, for a given task to produce a single, robust classifier. TAGLETS extracts relevant auxiliary data for training using SCADs, a database of auxiliary data aligned with concepts in ConceptNet, and passes all relevant data to an ensemble of user-specified modules, which are trained and distilled into a final classifier.  

![TAGLETS](figures_for_readme/taglets.jpg)

This is the codebase for all the experiments mentioned in [TAGLETS:  A System for Automatic Semi-Supervised Learning with Auxiliary Data](https://arxiv.org/abs/2111.04798).

For general use of TAGLETS, we recommend using [this up-to-date TAGLETS repository](https://github.com/BatsResearch/taglets) instead.

## Installation

The package requires `python3.7`. You first need to clone this repository:
```
git clone https://github.com/BatsResearch/taglets.git
```

Before installing TAGLETS, we recommend creating and activating a new virtual environment which can be done by the following script:
```
python -m venv taglets_venv
source taglets_venv/bin/activate
```

You also want to make sure `pip` is up-to-date:
```
pip install --upgrade pip
```

Then, to install TAGLETS and download related files, run:
```
bash setup.sh
```

## Datasets

Our experiments depend on four different datasets that you will need to download separately.

- [FMD](http://people.csail.mit.edu/celiu/CVPR2010/FMD/index.html): Download the database (.zip) and extract it. When asked to provide a path to this dataset later, please provide the path to the outmost directory of this dataset. 

- [GroceryStoreDataset](https://github.com/marcusklasson/GroceryStoreDataset): Download the repo as a zip file and extract it (or just clone the repo). When asked to provide a path to this dataset later, please provide the path to the inner `dataset` directory of this dataset.

- [Office-Home Dataset](https://www.hemanthdv.org/officeHomeDataset.html): Download the dataset (.zip) and extract it. When asked to provide a path to this dataset later, please provide the path to the inner `OfficeHomeDataset_10072016` directory of this dataset.

- ImageNet-21k

## Running the experiments

## Citation

Please cite the following paper if you are using our framework :)

```
@inproceedings{piriyakulkij:mlsys22,
  Author = {Wasu Piriyakulkij and Cristina Menghini and Ross Briden and Nihal V. Nayak and Jeffrey Zhu and Elaheh Raisi and Stephen H. Bach},
  Title = {{TAGLETS}: {A} System for Automatic Semi-Supervised Learning with Auxiliary Data},
  Booktitle = {Conference on Machine Learning and Systems (MLSys)},
  Year = {2022}}
```