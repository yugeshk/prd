## Description

This repository contains scripts you will need to generate a PRD template.
It also contains a sample PRD under `samples/epfl-pocketcampus` for your reference.

>[!NOTE]
>As you may know, the EPFL Pocketcampus app was developed in the first iteration
>of this course. 

> [!WARNING]
> If you face issues in getting the PRD setup to work, you can also copy this google doc [template](https://docs.google.com/document/d/1Ow0d1C7g_oLMRQQAzc6ivBJLO2s9G5BXmbU7otUmMdY/edit?usp=sharing) and use it to submit the PRD for M3. 

## Requirements 

1. `python` 

You need `python3` installed to run the `prd-scripts` locally. You can find
instructions for installing python
[here](https://realpython.com/installing-python/).

2. `pandoc`

To convert the `markdown` files in this template to a `pdf` you need the
`pandoc` file format convertor installed locally. Instructions to install the
`pandoc` package are available [here](https://pandoc.org/installing.html).

## Setup

1. Ensure you have python3 on your local machine. 
```
python3 --version
```

2. Fork this repo into your organization and clone it 
```
git clone git@github.com:<your-org-name>/prd.git
cd mvp-prd
```

3. Create a Virtual Enviornment
```
pip3 install virtualenv
python3 -m virtualenv venv
```

4. Activate the Virtual Environment
```
source venv/bin/activate
```

On Windows, if you are using command prompt, you need to run - 
```
path\to\venv\Scripts\activate.bat
```

and if you are using PowerShell, you need to run - 
```
path\to\venv\Scripts\activate.ps1
```
> [!NOTE]
For Windows, you can find the instructions to setup a virtualenv [here](https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html).

5. Install the `prd_tools` python app
```
pip install -r requirements.txt
pip install -e .
```

Once you are done using the virtualenv, you can exit it by typing `deactivate`.

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
swent_prd generate  --team <TeamNumber> <folder name>
```

This will create a file called `Team_<Number>_prd.pdf` in the root folder.

>[!IMPORTANT]
> When you begin filling out the various sections, you should remove the
> comments added in italics. They are only there to help start your thinking
> process.
