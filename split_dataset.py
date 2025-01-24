

import os
import shutil
import random

# Set the source folders for images and labels

image_source_folder = "path/to/source/image"
label_source_folder = "path/to/source/label"

# Set the destination folders for training and testing
train_image_folder = "path/to/target/train/image"
train_label_folder = "path/to/target/train/label"
test_image_folder = "path/to/target/test/image"
test_label_folder = "path/to/target/test/label"

import os
import random
import shutil

# Define the split ratio (e.g., 80% for training, 20% for testing)
split_ratio = 0.8

# Create destination folders if they don't exist
os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(train_label_folder, exist_ok=True)
os.makedirs(test_image_folder, exist_ok=True)
os.makedirs(test_label_folder, exist_ok=True)

# List all image files in the source folder
image_files = os.listdir(image_source_folder)

# Randomly shuffle the image files
random.shuffle(image_files)

# Calculate the number of images for training and testing
split_index = int(len(image_files) * split_ratio)

# Split the image files into training and testing
train_images = image_files[:split_index]
test_images = image_files[split_index:]

# Move the training image and label pairs to their respective folders
for image in train_images:
    label = image.replace(".jpg", ".txt").replace(".png", ".txt")
    label_path = os.path.join(label_source_folder, label)

    if os.path.exists(label_path):
        shutil.move(os.path.join(image_source_folder, image), os.path.join(train_image_folder, image))
        shutil.move(label_path, os.path.join(train_label_folder, label))

# Move the testing image and label pairs to their respective folders
for image in test_images:
    label = image.replace(".jpg", ".txt").replace(".png", ".txt")
    label_path = os.path.join(label_source_folder, label)

    if os.path.exists(label_path):
        shutil.move(os.path.join(image_source_folder, image), os.path.join(test_image_folder, image))
        shutil.move(label_path, os.path.join(test_label_folder, label))

print("Dataset split into training and testing sets with matching image and label pairs.")



