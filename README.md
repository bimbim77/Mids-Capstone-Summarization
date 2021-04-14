# Mids-Capstone-Summarization

## Summarization of news articles for social media marketing
UC Berkeley MIDS Program 
Spring 2021 Capstone Project

### Problem
MIDS Capstone Team "ShortText" is focused on the problem of reducing manual and human text summarization for high velocity content marketing for marketing teams globally.

Our goal for this solution is to build a text summarization tool that captures the essence of the content in these articles that could be used to post messages in social media platforms (LinkedIn and Twitter) for running its advertisement campaigns.

Using CNN news training data and XSUM data, we are applying the state of the art abstractive summarization - PEGASUS model for our MVP for teams working on Social Media Marketing; we intend to use our MVP to contribute to peer and industry learning about the use of abstractive summarization to alleviate the need for human/manual text summarization

Our Chrome Extension application automates the summarization process for content from popular news websites , and facilitates the posting of this content to the Twitter and LinkedIn social media channels with summaries tailored to the post length restrictions of each platform.

## Target User / Customer
Marketing Team in News organizations

## Supported Websites
Currently works on CNN, New York Times, BBC, and ESPN. Additional websites in development.

## Usage Notes
We do not have the EC2 instance that serves as the backend to our Chrome Extension running at all times due to prohibitive cost. The instance and the web server powered by the instance will need to be started for the Chrome Extension to function.

## Data
* TensorFlow Datasets for Summarization - across various domains (news, email, research paper, wiki, patents, legislative bills etc)
* AQUAINT Corpus of English News Text - Contains news articles from the Associated Press and New York Times.
* Document Understanding Conferences Data  - Text Summarization datasets from DUC
* TAC Data  - Past TAC Datasets for text summarization
* English Gigaword - Data Corpus from Linguistic Data Consortium 
* Live Blog Corpus  - Online Blog Corpus 

## Possible data science techniques
* NLP
* Abstractive Text Summarization
* Transformer encoder-decoder models
* Self-Supervised Objective for Summarization
* Language Models

## Related research/products
1. Summarization - HuggingFace Transformer
2. arXiv:1912.08777 - PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization  
3. arXiv:2007.14062 - Big Bird: Transformers for Longer Sequences

## Team Contact Information
Imran Manji - imran.manji@ischool.berkeley.edu 
Julie Nguyen - julie.nguyen@ischool.berkeley.edu 
Jeya Seenivasagam - ksjeyabarani@berkeley.edu 
Vaishnavi Rajagopal - vaishnavi_raj@berkeley.edu 

