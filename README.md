# Updates

1. Download the Omnivore repository from GitHub in setup.sh, as the original model-loading implementation is no longer working.

The code replaces the original model-loading approach with:

```
 self.encoder = torch.hub.load("facebookresearch/omnivore", model="omnivore_swinT", pretrained=pretrained)
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

2. update setup.sh to allow it to download and unpack Omnivore source into checkpoints/omnivore-main

3. Add a few test_images

4. Update the arrow line color: deep red at the extreme "looking straight out at the viewer" end, yellow at the boundary (gaze parallel to the paper plane, z≈0), and blue at the extreme "looking straight into the paper/scene" end.

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

4. run the inference on one single image:
   `python demo.py --input-filename data/pexels-jopwell-2422290.jpg --output-dir output/ --modality image`

5. run the inference on the folder `test-images`
   `python run_test.py`
