# Google Export Analysis

Google export analysis is a Python project to demonstrate the google big query working and handling of large datasets..

## Installation

As prerequisite please install [python3](https://www.python.org/downloads/). 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install google-cloud-bigquery client.

```bash
pip3 install --upgrade google-cloud-bigquery
```
## Export Environment Variable

Set your service account key-pair json file path in the environment varibale having name GOOGLE_APPLICATION_CREDENTIALS. If you are new google service accounts then setup using the following [link](https://cloud.google.com/bigquery/docs/reference/libraries).

```bash
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```

## Usage
```python

# To run all the test cases run following command
python3 main.py --run_test

# To perform analysis for any full_visitor_id run the project as mentioned below.
python3 main.py --full_visitor_id=<enter_full_visitor_id>

```

## Future Iteration
In the next step, We will containerize  this project and will use flask as API framework.