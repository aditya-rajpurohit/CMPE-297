# On Selecting Few-Shot Examples for LLM-based Code Vulnerability Detection

## Abstract
Large language models (LLMs) have demonstrated impressive capabilities for many coding tasks, including summarization, translation,
completion, and code generation. However, detecting code vulnerabilities remains a challenging task for LLMs. An effective way
to improve LLM performance is in-context learning (ICL) – providing few-shot examples similar to the query, along with correct
answers, can improve an LLM’s ability to generate correct solutions. However, choosing the few-shot examples appropriately is
crucial to improving model performance. In this paper, we explore two criteria for choosing few-shot examples for ICL used in the
code vulnerability detection task. The first criterion considers if the LLM (consistently) makes a mistake or not on a sample with the intuition that LLM performance on a sample is informative about its usefulness as a few-shot example. The other criterion considers similarity of the examples with the program under query and chooses few-shot examples based on the k-nearest neighbors to the given sample. We perform evaluations to determine the benefits of these criteria individually as well as under various combinations, using open-source models on multiple datasets.

## Medium Article
For a simplified explanation of the topic, you can read the article on Medium:
[Article Link](https://medium.com/@aditya-rajpurohit/when-large-language-models-learn-from-their-mistakes-smarter-few-shot-learning-for-code-ebfd64ea3e70)

## Video Overview
For a detailed explanation of this topic, check out the YouTube video overview:  
[Video Link](https://youtu.be/GunmNbXVvpw)

## Citation
If you use insights from this work, please cite:  
**"On Selecting Few-Shot Examples for LLM-based Code Vulnerability Detection"**
[Research Paper](https://arxiv.org/pdf/2510.27675)

## Contact
For questions or further discussions, feel free to reach out to the authors via their respective academic affiliations listed in the paper.