# Intro to Evals

Current repository supports discovery on evals on Macbook Air

Only two models could run on local without crashing
hf/Qwen/Qwen2.5-0.5B
hf/openai-community/gpt2

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

https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/gdm_intercode_ctf