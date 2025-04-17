# MVG IMF

## Description
This repository contains a Multivariate Gaussian (MVG) models for Infrared Molecular Fingerprints (IMF) of human blood samples. Model in this context refers to the mean spectrum and the covariance matrix of a datasplit. Additionally, the script Simulate.py can be used to simulate new spectra using the MVG models. To create cohorts of equal size to the real datasets please refer to the table on datalengths. 

## Usage
New samples can be simulated using Simulate.py
- n: number of samples to be generated
- cohort: name of the cohort:
    - 'luca': Lung cancer
    - 'prca': Prostate cancer
    - 'brca': Breast cancer
    - 'blca': Bladder cancer
- stage: stage information:
    - 'None'
    - 'stage1' to 'stage4': only available for luca
- dataset: specifiy training or test set:
    - 'train'
    - 'test'
- label: healthy or diseased:
    - 0: healthy
    - 1: diseased
- sex:
    - 0: male
    - 1: female
    - _: both

For example:
```python
from Simulate import Simulate

vec = np.loadtxt('vec.txt')

df_hat = pd.DataFrame(Simulate(
    n=100,
    cohort='luca',
    stage='stage3',
    dataset='train',
    label=0,
    sex=0
), columns=vec)

```
