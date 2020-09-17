# Poleval Automatic Cyberbullying API
![Python tests](https://github.com/g0lemXIV/harmfulness_app/workflows/Python%20tests/badge.svg?branch=master)  ![Docker Build&Push](https://github.com/g0lemXIV/harmfulness_app/workflows/Docker%20Build&Push/badge.svg?branch=master) ![License](https://img.shields.io/pypi/l/ansicolortags.svg)

## Task definition
In this task, the participants shall distinguish between three classes of tweets: 0 (non-harmful), 1 (cyberbullying), 2 (hate-speech). There are various definitions of both cyberbullying and hate-speech, some of them even putting those two phenomena in the same group. The specific conditions on which we based our annotations for both cyberbullying and hate-speech, which have been worked out during ten years of research [1] will be summarized in an introductory paper for the task, however, the main and definitive condition to distinguish the two is whether the harmful action is addressed towards a private person(s) (cyberbullying), or a public person/entity/large group (hate-speech).  

## Project description

**The project includes three main assumptions:**
- [x] Make experiments with the train data, and find the best algorithm for sentence classification;
- [x] Develop REST API;
- [x] Test API performance and quality.

**Additional Assumptions v0.1:**
- [x] Docker image smaller than 4GB
- [x] Solution runs on CPU faster than 1 second per observation (~0.25 ms)
- [x] CD/CI good practice (github actions)
- [x] Clean code  (pylint 8.75/10)
- [x] Model Validation
- [x] Simplicity and performance
- [x] Jupyter Notebook with analysis

**In Progress Assumptions v0.2:**
- [ ] Connect to GCP to automatically download models
- [ ] Kubernetes deplyment  
- [ ] Streamlit App  
- [ ] Twitter connection
- [ ] Test more python version
- [ ] JupyterNotebook inside docker
- [ ] Better modeliing to recognize hate-speech/non-harmfull

### Installation (tested on Python 3.7)

1. The application can be pulled directly from the docker hub
```bash
user:~$ docker pull rafikrze/harmfulness_app:0.1
```
2. Invoke docker with command
```bash
user:~$ docker run -p 8082:8000 rafikrze/harmfulness_app:0.1
```

3. Go to http://localhost:8082/docs.
4. Click Authorize and enter the API key, if not changed ```auth_key=test```.
5. Default configuration file can be changed. To do that create ```.env``` file in harmfulness_app like follows:

```txt
debug=True
auth_key=aaaa12456
api_key_gcp=apikey

model_name=regression_pipeline_exp0
```

6. You can use the sample payload when trying out using the API.

**The application can also be checked from the jupyter notebook, for this entry to [/notebooks/Tests_notebooks.ipynb](https://github.com/g0lemXIV/harmfulness_app/blob/master/notebooks/Tests_notebooks.ipynb) and run the first cell.**

**Warning**  
To run the application properly install all additional packages like (Pandas, NumPy, etc.).
Built docker-compose with Jupiter notebook and Streamlit app will be available in release v0.2.  

### Results

The experiment and test part can be viewed in the notebooks directory.

**Model Metrics on [test set](http://2019.poleval.pl/task6/task6_test.zip)**
```python
Logistic Regression Accuracy: 0.875 (Poleval best 0.876)
Logistic Regression F1 micro: 0.875 (Poleval best 0.876)
Logistic Regression F1 macro: 0.48 (Poleval best 0.5175)
```

**Timer**
```python
Same text: 11.2 ms ± 192
Different texts: 25.5 ms ± 1.33 ms
```
