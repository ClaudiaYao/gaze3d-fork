#!/bin/bash

# Create weights directory if it doesn't exist
mkdir -p weights

# Download the head detector weights
# https://github.com/MahenderAutonomo/yolov5-crowdhuman/blob/master/weights/download_weights.sh
gdown 'https://drive.google.com/uc?id=1gglIwqxaH2iTvy6lZlXuAcMpd_U0GCUb' -O ./weights/crowdhuman_yolov5m.pt

echo "Download complete: weights/crowdhuman_yolov5m.pt"


# Download and unpack Omnivore source into checkpoints/omnivore-main
OMNIVORE_ZIP_URL="https://github.com/facebookresearch/omnivore/archive/refs/heads/main.zip"
OMNIVORE_ZIP_PATH="checkpoints/omnivore-main.zip"
OMNIVORE_TMP_DIR="checkpoints/omnivore-main-main"
OMNIVORE_TARGET_DIR="checkpoints/omnivore-main"

echo "Downloading Omnivore source zip..."
curl -L "$OMNIVORE_ZIP_URL" -o "$OMNIVORE_ZIP_PATH"

echo "Removing old Omnivore folder (if any)..."
rm -rf "$OMNIVORE_TARGET_DIR" "$OMNIVORE_TMP_DIR"

echo "Unzipping Omnivore..."
unzip -q "$OMNIVORE_ZIP_PATH" -d checkpoints

# GitHub zip extracts to omnivore-main-main; rename to omnivore-main
mv "$OMNIVORE_TMP_DIR" "$OMNIVORE_TARGET_DIR"

# Cleanup zip
rm -f "$OMNIVORE_ZIP_PATH"

echo "Omnivore ready at: $OMNIVORE_TARGET_DIR"