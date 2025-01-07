# Image Captioning using HuggingFace

## Objective
This project is aimed to generate captions for image uploaded by user, based on gen-ai technology.

## Demo of the Project

![this is a demo of how the application works!](static/demo.gif)


## Tech stack
- **Backend** : Open source `Salesforce/blip-image-captioning-base` model from Hugging Face. The BLIP model (Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation) for image captioning is pretrained on COCO dataset - base architecture (with ViT base backbone).
- **Frontend** : Flask framework in python

## How to run the project
### Step 1: Create a virtual environment
```
python -m venv myenv
```
### Step 2: Activate the Virtual Environment
1.  Open the terminal or command prompt.

2.  Navigate to the folder where the virtual environment is located:

```
cd path\to\myenv
```
3. Run the activation script:

- For Command Prompt:
```
myenv\Scripts\activate
```
- For PowerShell:
```
.\myenv\Scripts\Activate.ps1
```
`NOTE`: If you encounter an error regarding script execution policy, you may need to adjust the policy:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
- For Git Bash or other Bash-like shells:
```
source myenv/Scripts/activate
```
### Step 3: Install dependencies
```
pip install -r requirements.txt
```
### Step 4: Run the prerequites
```
python prerequisites.py
```

After running this command, a new folder `blip-image-captioning` will be created in the same directory

### Step 5: Run the application
```
python app.py
```