# YAML 

# GitHub Actions Workflow YAML

name: CI
on: [push]

jobs:

  lint:
    runs-on: ubuntu-latest
    steps:
    
    - uses: actions/checkout@v3
    
    - name: Set up Python  
      uses: actions/setup-python@v3 
      with:
        python-version: "3.9"
