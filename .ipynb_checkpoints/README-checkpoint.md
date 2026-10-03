# Graduating from Notebooks

These are the notes for my workshop titled *Graduating from Notebooks* given on Thursday, October 8th, 2026 in Mogridge Hall to the *Undergraduate Statistics Club* of the University of Wisconsin–Madison.

**Background.** This workshop assumes that you know either `R` or `python`, and have performed some sort of data analysis in that language (Ex. *linear regression*). I will teach this workshop in `python`, but will try my best to talk about the higher level ideas which generalize to `R`.

**Structure.**  Source Files $\rightarrow$ Project Structure$\rightarrow$Git$\rightarrow$GitHub

### 1. Source Files
----- 

####  **Why do we even need source files at all?**

You might be used to working in Jupyter Notebook. You might also be thinking something like
> I've used Jupyter Notebooks (`.ipynb`) or R Markdown (`.rmd`) for all of my statistics/data science courses. And now you're telling me this isn't enough? What with that?

To motivate this, let's take a look at `diabetes.ipynb`. We can see that it does a few things: 
 1. Uses the [`load_diabetes`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) function to load `X` as a `pd.DataFrame` and `y` as a `pd.Series`. 
 2. Displays them for verification
 3. Performs a `train_test_split`
 4. Fits a `LinearRegression` model using the testing data.
 5. Makes predictions using the testing data
 6. Uses `root_mean_squared_error` to calculate the test loss: 

$$\mathrm{RMSE}=\sqrt{\frac{\sum_{i=1}^n (\hat y_i- y_i)^2}{n}} $$

But then you remember that you should rescale (normalize) your `X` matrix, so that all of your features are on the same scale. So you go ahead and add: 

 7. Use `StandardScaler` to rescale the data to have mean $0$ and variance $1$.

**To see where this is headed:** notice how things are already getting disorganized. *Imagine what happens if you want to extend this, or collaborate with another person?* What happens when: 

- You have multiple data sets
- Mutliple Models, and some sort of model selection procedure
- The data isn't clean, and you have to enforce formatting in one of the columns
- You rerun simmilar code with different inputs

> **Lessson 1.** *Jupyter Notebooks/R Markdown are great developement tools, and they allow for really quick building. But they promote poor coding practice, whereas rewriting imortant code in source files will do the opposite.*

#### **So, what do *source files* even mean?** 

It's simple really, if you're used to Jupyter Notebooks (`.ipynb`), you will now write python (`.py`) files. If you're used to R Markdown (`.Rmd`) you will now write R (`.R`) files. Let's look at what the same analysis would look like in a python file

Take a look at `diabetes.py`. It is about the simplest, most naive way to use a python file. It: 

- Has the same imports
- Loads, and splits the data
- Scales the data
- Fits a model on train data
- Makes predictions on test data
- Prints RMSE

You have to run it in your terminal. This is another key idea of this presentation: 
> **Lessson 2.** *Get hip with your terminal, it's one of the most important and least taught technologies.*

```bash 
(base) spencervenancio@Spencers-Air-2 gfnb $ python3 diabetes.py 
rmse=58.917591439619265
(base) spencervenancio@Spencers-Air-2 gfnb $
``` 
But you almost never actually write data analysis code all in one file like this. You can imagine as your project grows (especially with collaborators), this file could grow to be hundreds, and potentially thousands of lines long. **The solution? Split the project into small files,** where each file handles a specific part. One file for preprocessing, another for training, another for predicting on live data. Now lets talk about:
  
### 2. Project Structure
--- 
#### **Background**
I first started to think about data science project structure when interned at Nokomis Health, and I was really the only one doing data science there. I basically got handed access to an Oracle Cloud Data Science Jupyter Lab, and it was my job to figure out how to set myself up. This was when I discovered [Cookie Cutter Data Science](https://cookiecutter-data-science.drivendata.org/), and learned another fundamental principle of data science: 

> **Lesson 3.** *Good projects die in notebooks. Notebooks are not production ready, and R&D projects that never get finished go unused.*

I won't go over all of the ideas relating to project structure. In general, I think you'll learn the most if you build, and ocassionally learn more as needed. It can be hard to understand **why** a certain choice is good or bad until you make the mistakes. If you want a starting place, I really recommend reading [Opinions Section](https://cookiecutter-data-science.drivendata.org/opinions/) on CCDS. The main ideas they cover are: 

1. Data analysis is a directed acyclic graph
2. Raw data is immutable
3. Data should (mostly) not be kept in source control
5. **Notebooks are for exploration and communication, source files are for repetition**
6. **Refactor the good parts into source code**
7. **Keep your modeling organized**
8. **Build from the environment up**
9. Keep secrets and configuration out of version control
10. Store your secrets and config variables in a special file
12. **Encourage adaptation from a consistent default**

#### **Example Template**

So, what do they recommend? This is a slightly more barebones version of a `ccds` project

```bash
(base) spencervenancio@Spencers-Air-2 gfnb $ ccds 
```
It will then ask you some questions. The barebones answers will create a project with the structure:

```
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         data_challenge and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── data_challenge   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes data_challenge a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```


### 3. Git
--- 

### 4. GitHub
---

These are real emails, between me and my team members from when I did the data challenge in the Fall of 2024

![project_email_chain](emails_redacted.png)
