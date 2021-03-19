 **ALDO Automated UI Tests**
- 

### Environment Setup:

### Requirements:
  - Python 3+
  - PIP

### To create virtual environment
    1. install virtualenv 
        - `$ python3 -m pip install virtualenv`
    2. create a virtual environment  
        - `$ python3 -m venv env`
    3. Activate virtual environment 
        Mac os
          - `$ source env/bin/activate`
        Windows os
          - `$ call env/Scripts/activate`

### To install dependencies
    Ensure to be on the uitests folder where requirements.txt file exist and run the below command
    - `$ pip install -r requirements.txt`
    
## How to run a test:
    1. go to the tests folders like Desktop or Mobile respectively (i.e. src/Tests/Desktop)
    2. Command to run a test file  
        - `$pytest TestSuiteFile.Py`
    3. Command to run a specific test from a suite file
        - `$pytest TestSuiteFile.Py::test class::test method`
    
    Sample Commands to run the complete test file or to run a specific test inside the test file.
        1. To run complete set of tests in one module (i.e. Checkouts)_:
          `$pytest -v -m checkouts`
          
        2. To run a specific test from a test suite file 
          (i.e. module: Checkout and single Test name : test_guest_checkout_ship_to_store_creditcard_EE20_1705)
          `$pytest -v -m checkouts -k test_guest_checkout_ship_to_store_creditcard_EE20_1705`
          
    Other Test names and commands
        1. Filters test
          `$pytest -v -m filters`
        2. Footers test
          `$pytest -v -m footers`
        3. PDP Test
          `$pytest -v -m pdp`
        4. Promo and Taxes Test
          `$pytest -v -m promo_and_tax`
        5. Signup Test
          `$pytest -v -m signup`
        6. Wish List Test
          `$pytest -v -m wish_list`
        7. Add to Bag Test
          `$pytest -v -m AddToBag`
