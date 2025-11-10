# 🧠 Full Finetuning of SmolLM2-135M on AG News (Topic Classification)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DQPkFwldJZ0LkYIn1xFy_IygrQc-F3cK?usp=sharing)

## 📋 Overview
This project demonstrates **full finetuning** of the **SmolLM2-135M** model on the **AG News** dataset using Hugging Face Transformers.   The goal is to train the model to classify short news articles into four topics — **World**, **Sports**, **Business**, and **Sci/Tech** — using an **instruction-style text format**.

## ⚙️ Key Details
- **Model:** [`HuggingFaceTB/SmolLM2-135M`](https://huggingface.co/HuggingFaceTB/SmolLM2-135M)  
- **Dataset:** [`ag_news`](https://huggingface.co/datasets/ag_news)  

## 🧩 Notebook Steps
1. **Setup & Installs** – Install lightweight Hugging Face dependencies.  
2. **Imports & Auth** – Load libraries and optionally log in to Hugging Face / W&B.  
3. **Load Model** – Import the SmolLM2 base model and tokenizer.  
4. **Prepare Dataset** – Format AG News into an instruction-style prompt and tokenize.  
5. **Train Model** – Run full fine-tuning using `Trainer`.  
6. **Evaluate & Test** – Generate predictions on unseen news articles.  
7. **Save / Push** – Save the trained model locally or upload to Hugging Face Hub.






# 🚀 LoRA Fine-Tuning of SmolLM2-135M on TweetEval Sentiment

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EzYOFZVQMmHWYQ41514CZyTQyZNpsJZg?usp=sharing)

## 📌 Overview
This project performs **parameter-efficient LoRA fine-tuning** of **SmolLM2-135M** on **TweetEval/Sentiment** (labels: *Negative*, *Neutral*, *Positive*) using **Unsloth**.  
We load the base model in **4-bit** to save VRAM, attach **LoRA adapters**, and train via **TRL’s SFTTrainer** with an **instruction-style prompt**.

## 🧱 Key Components
- **Model**: `unsloth/smollm2-135m`  
- **Dataset**: `tweet_eval` → `sentiment`  
- **Method**: LoRA (`r=16`, `lora_alpha=16`, `lora_dropout=0.05`)  
- **Precision**: 4-bit loading (bitsandbytes) + `bf16/fp16` for training  
- **Trainer**: `trl.SFTTrainer` (supervised finetuning)

## 🔧 Notebook Flow
1. **Installs** – Minimal, pinned to a stable stack for TRL/Transformers + Unsloth.  
2. **Auth** – (Optional) Login to HF Hub + W&B for logging and pushing.  
3. **Load Base Model (4-bit)** – `FastLanguageModel.from_pretrained(...)`.  
4. **Attach LoRA** – `FastLanguageModel.get_peft_model(...)`.  
5. **Dataset & Prompting** – Build instruction-style prompts for Tweet→Label.  
6. **Train** – SFT with `eval_strategy/evaluation_strategy` handled version-safely.  
7. **Inference** – Generate one-word labels (*Negative/Neutral/Positive*).  
8. **Save / Push** – Save LoRA adapters locally or push to HF Hub.




# 🧮 DPO Fine-Tuning of SmolLM2-135M on Math Preference Dataset

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_rVwfLe0W8xhjmxW7v5gxiQhL2JHxTAB?usp=sharing)

## 📘 Overview
This project demonstrates **Direct Preference Optimization (DPO)** fine-tuning of the **SmolLM2-135M-Instruct** model using **Unsloth** for efficient 4-bit and LoRA-based training.  
The dataset contains small **math reasoning preference pairs** — each with a *prompt*, a *preferred (chosen)* solution, and a *rejected* solution.  
The goal is to align the model to prefer **correct mathematical reasoning** and reject incorrect answers.

## ⚙️ Key Details
- **Model:** [`unsloth/SmolLM2-135M-Instruct`](https://huggingface.co/unsloth/SmolLM2-135M-Instruct)  
- **Method:** Direct Preference Optimization (DPO)  
- **Techniques:** LoRA (parameter-efficient) + 4-bit quantization (VRAM-efficient)  

## 🧩 Notebook Flow
1. **Install & Auth** – Sets up Unsloth, TRL, PEFT, and authenticates Hugging Face + W&B.  
2. **Dataset** – Loads or creates a small math preference dataset (`prompt`, `chosen`, `rejected`).  
3. **Model Setup** – Loads SmolLM2 in 4-bit and attaches LoRA adapters.  
4. **DPO Training** – Runs lightweight preference optimization with Unsloth’s patched `DPOTrainer`.  
5. **Inference** – Tests the model on unseen math problems.  
6. **Save / Push** – Saves the fine-tuned model locally or uploads it to the Hugging Face Hub.




