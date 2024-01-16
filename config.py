import os

home = os.path.expanduser("~")
root_dirs = {
    'bird': '/mnt/sdb1/pwy/data/CUB_200_2011',
    'car':  '/mnt/sdb1/pwy/data/cars',
    'air':  '/mnt/sdb1/pwy/data/FGVC-aircraft',
    'dog':  '/mnt/sdb1/pwy/data/standford_dogs'
}

class_nums = {
    'bird': 200,
    'car': 196,
    'air': 100,
    'dog': 120
}

HyperParams = {
    'alpha': 0.5,
    'beta':  0.5,
    'gamma': 0.5,
    'kind': 'bird',
    'bs': 38,
    'epoch': 500,
    'arch': 'resnet50'
}
