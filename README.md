# Updates

1. download https://github.com/facebookresearch/omnivore in setup.sh. The original model loading is not working.

what the code has done is to replace:

```
 # self.encoder = torch.hub.load(
        #     "facebookresearch/omnivore", model="omnivore_swinT", pretrained=pretrained)

```

With:

```
omnivore_path = (
            str(CWD / "checkpoints" / "omnivore-main")
        )
self.encoder = torch.hub.load(
            str(omnivore_path),
            model="omnivore_swinT",
            pretrained=pretrained,
            source="local",
        )
```

2. Add a few test_images

# Usage: The usage is the same as in the original Gaze3D repository.

1. First, we need to clone the repository

```
git clone
cd <name_of_the_repo>
```

2. Next, create the conda environment and activate it after installing the necessary packages:

```
conda env create -f environment.yaml
conda activate gazeCVPR
```

3. Download model for head detection:
   `bash setup.sh`
