# Flood-Aware Dynamic Delivery Routing via Vision Transformers
CSC173 project proposal, Group 12 (Ajman, Johann, Dale)

Stage 1 of the pipeline: a Vision Transformer that classifies road images into three passability classes.

## Classes
- **clear**: dry road, normal delivery speeds
- **passable**: shallow flooding that high-clearance delivery vehicles can pass
- **impassable**: deep floodwater that blocks delivery vehicles

## Current status (preliminary)
- Model: ViT-Base (ImageNet-pretrained, KerasHub) fine-tuned on 552 labeled images
- Split: 78/84/232 train, 16/15/48 validation, 17/16/46 test (clear/passable/impassable), test set untouched
- Validation results: accuracy 0.861, macro-F1 0.814
- Known weakness: passable vs. impassable (F1 about 0.6 for passable)
- Not yet included: images from Iligan City roads

## Files
- `flood_vit_classifier.ipynb`: training and evaluation (Google Colab, TensorFlow/Keras)
- `splits.csv`: train/val/test assignment per image

## Data
Images are not included in this repo. Sources: Roadway Flooding Image Dataset (Kaggle, saurabhshahane), Clean/Littered Road Classification (Faizal Karim, Krishnav Rajbangshi).
