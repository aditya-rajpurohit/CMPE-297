# Modern AI with unsloth.ai

## 📋 Project Overview
A comprehensive exploration of fine-tuning techniques for the SmolLM2-135M language model across different domains and tasks.

## 🚀 Projects Breakdown

### 1. 📰 News Topic Classification 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DQPkFwldJZ0LkYIn1xFy_IygrQc-F3cK)

**Objective:** 
- Classify news articles into four topics
- Topics: World, Sports, Business, Sci/Tech
- Dataset: AG News

**Methodology:**
- Full fine-tuning of SmolLM2-135M
- Instruction-style text formatting
- Comprehensive model training approach

**Key Steps:**
- Load pre-trained SmolLM2-135M model
- Prepare AG News dataset
- Format data into instruction prompts
- Train using Hugging Face Trainer
- Evaluate model performance

### 2. 🐦 Tweet Sentiment Analysis
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EzYOFZVQMmHWYQ41514CZyTQyZNpsJZg)

**Objective:**
- Classify tweet sentiments
- Labels: Negative, Neutral, Positive
- Dataset: TweetEval Sentiment

**Methodology:**
- LoRA (Low-Rank Adaptation) fine-tuning
- 4-bit model loading for VRAM efficiency
- Parameter-efficient training

**Key Steps:**
- Load SmolLM2 in 4-bit precision
- Attach LoRA adapters
- Use TRL's SFTTrainer
- Create instruction-style prompts
- Train and generate one-word labels

### 3. 🧮 Math Preference Optimization
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_rVwfLe0W8xhjmxW7v5gxiQhL2JHxTAB)

**Objective:**
- Improve mathematical reasoning
- Train model to prefer correct solutions
- Use preference pairs dataset

**Methodology:**
- Direct Preference Optimization (DPO)
- LoRA + 4-bit quantization
- Unsloth-based efficient training

**Key Steps:**
- Load SmolLM2-135M-Instruct model
- Prepare math reasoning preference dataset
- Attach LoRA adapters
- Run DPO training
- Test model on math problems

### 4. 🔢 Advanced Math Reasoning
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zjOUCCckHdqwD53NOpTKoNU4yi48nLQn)

**Objective:**
- Enhance step-by-step math reasoning
- Improve final answer accuracy
- Dataset: GSM8K

**Methodology:**
- Group Relative Preference Optimization (GRPO)
- Reinforcement learning approach
- Reward-based model improvement

**Key Steps:**
- Load SmolLM2-135M-Instruct
- Prepare GSM8K dataset
- Define reward function
- Generate multiple responses
- Train using relative performance

### 5. 🌍 Turkish Language Adaptation
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1T7qxdDMcEX9ApICzFyiVvyA32pkXhtlB)

**Objective:**
- Adapt model to Turkish language
- Improve linguistic capabilities
- Enable fluent Turkish text generation

**Methodology:**
- Continued Pretraining (CPT)
- Next-token prediction
- Domain-specific language adaptation

**Key Steps:**
- Load base SmolLM2-135M model
- Create Turkish text corpus
- Use causal language modeling
- Train for multiple epochs
- Test Turkish language fluency

## 🛠️ Common Technologies
- Hugging Face Transformers
- Unsloth
- 4-bit Quantization
- LoRA Adapters

## 📦 Resources
- [SmolLM2-135M Model](https://huggingface.co/HuggingFaceTB/SmolLM2-135M)
- [Unsloth GitHub](https://github.com/unslothai/unsloth)
- [Video Demo](https://youtu.be/w3EZLmHZZK4)