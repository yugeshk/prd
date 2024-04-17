## Description

This repository contains scripts you will need to generate a PRD template.
It also contains a sample PRD under `sample-pocketcampus` for your reference.
>[!NOTE]
>As you may know, the EPFL Pocketcampus app was a creation of the first iteration
>of this course. 

## Setup

1. Ensure you have python3 on your local machine. 
```
python3 --version
```

2. Fork this repo into your organization and clone it 
```
git clone git@github.com/<your-org-name>/mvp-prd.git
cd mvp-prd
```

3. Create a Virtual Enviornment
```
pip3 install virtualenv
python3 -m virtualenv venv
```

4. Activate the Virtual Environment
```
pip install -r requirements.txt
```

5. Install the `prd_tools` python app
```
pip install -e .
```

## Usage

### Creating a PRD Template

1. Initialize a new PRD template
```
swent_prd init <optional: folder name>
```
If you do not pass a folder name, it will create a default folder called
`sections`. 

### Generating the PDF

1. Run the `generate` command
```
swent_prd generate <folder name>
```

This will create a file called `prd_document.pdf` in the root folder.
