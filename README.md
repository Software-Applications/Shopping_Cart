# Shopping Cart (Python)

Contains python scripts to help businesses in tagging products purchased by customers and printing receipts.

## Features

  + prints receipts on CLI
  + writes receipts to text file in receipts folder
  + reads product and meta data from google sheets
  + handles pricing per pound and pricing per item
  + reads data from barcode scanner
  + validates product input (pytest script)
  + validates price format (pytest script)
  + validates timestamp format (pytest script)
  + validates tax calculation and total price calculation (pytest script)


## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip
  + Git

## Installation

Fork the repository from [GitHub source](https://github.com/DheerajRekula/Shopping_Cart).

Then use GitHub Desktop or the command-line to "clone" or download your fork onto your local computer:

```sh
git clone https://github.com/YOUR_USERNAME/Shopping_Cart.git # this is the HTTP address, but you could alternatively use the SSH address
```

Navigate into your local repo before running any of the other commands below:

```sh
cd //YOUR_CLONE_PATH/shopping_cart
```

## Setup

Create and activate an Anaconda virtual environment. From within the virtual environment, install package dependencies listed in the "requirements.txt" file:

```sh
pip install -r requirements.txt
```

Copy the ".env.example" file to a new file called ".env" (in your local repo, NOT your remote repo), and update the environment variables inside as necessary (see below).

## Usage

### Run Script

Run the command to execute the script

```sh
python shopping_cart.py
```

## Additional Instructions

This script uses my Google API credentials to sign into Google Sheets. If you want to use your own credentials, follow the instructions available in this [link](https://techwithtim.net/tutorials/google-sheets-python-api-tutorial/) to download a "JSON" API credentials file containing your information. Copy and Paste the file in //google_credentials1 location inside your local project repository.

## [License](/LICENSE.md)

