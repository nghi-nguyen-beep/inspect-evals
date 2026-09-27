# Intro to Evals

Current repository for learning evals (that's runnable on Macbook Air without crashing it). We use a sample dataset containing 5 questions that tests general look-up capabilities. 

Only two models could run on local without crashing
- hf/Qwen/Qwen2.5-0.5B
- hf/openai-community/gpt2

## Installation
```python
pyenv virtualenv 3.10 inspect-evals
pyenv activate inspect-evals
pip install -r requirements.txt
```

## How to Run Evals

```python
inspect eval simpleqa.py --model hf/openai-community/gpt2
```

## How to View Evals
```python
inspect view
```

## Resources
This repo was built off of AI Security Institute open source

https://inspect.aisi.org.uk/
https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/gdm_intercode_ctf