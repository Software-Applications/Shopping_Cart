# Shopping Cart (Python)

Contains Python scripts to help businesses in tagging products purchased by customers and print receipts.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip
  + Git

## Installation

Fork the repository from [GitHub source](https://github.com/DheerajRekula/Shopping_Cart).

Then use GitHub Desktop or the command-line to "clone" or download your fork onto your local computer:

```sh
git clone https://github.com/YOUR_USERNAME/notification-service-py.git # this is the HTTP address, but you could alternatively use the SSH address
```

Navigate into your local repo of the clone before running any of the other commands below:

```sh
cd //YOUR_CLONE_PATH/shopping_cart
```

## Setup

Create and activate an Anaconda virtual environment. From within the virtual environment, install package dependencies listed in the "requirements.txt" file:

```sh
pip install -r requirements.txt
```

Copy the ".env.example" file to a new file called ".env" (in your local repo, NOT your remote repo), and update the environment variables inside as necessary (see below).

### Email

For email capabilities, [sign up for a SendGrid account](https://signup.sendgrid.com/), click the link in a confirmation email to verify your account, then [create a new API key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions. Note the email address you used, and the value of the API Key, and store them in environment variables called `MY_EMAIL_ADDRESS` and `SENDGRID_API_KEY`, respectively.

## Usage

### Send Email

Send email to the address specified:

```sh
python app/send_email.py
```

## [License](/LICENSE.md)

## Additional Instructions

This script uses my Google API credentials to sign into Google Sheets. If you want to use your own credentials, follow the instructions available in this [link](https://techwithtim.net/tutorials/google-sheets-python-api-tutorial/) to download a "JSON" API credentials file containing your information. Copy and Paste the file in //google_credentials location inside your local project repository.
