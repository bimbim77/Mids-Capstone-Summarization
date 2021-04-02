# Model Requirements and Setup

Pegasus library and related models are also added to the repo under Model directory.

## setup 
Run the below commands

1. cd Model
2. export PYTHONPATH=.
3. sh setup_python_env.sh
4. pip install gsutil
5. cd pretrained_downloaded_models/xsum 
6. ```gsutil -m cp   "gs://pegasus_ckpt/xsum/model.ckpt-30000.data-00000-of-00001"   "gs://pegasus_ckpt/xsum/model.ckpt-30000.index"   "gs://pegasus_ckpt/xsum/model.ckpt-30000.meta"```
7. cd pretrained_downloaded_models/cnn_dailymail
8. ```gsutil -m cp   "gs://pegasus_ckpt/cnn_dailymail/model.ckpt-210000.data-00000-of-00001"   "gs://pegasus_ckpt/cnn_dailymail/model.ckpt-210000.index"   "gs://pegasus_ckpt/cnn_dailymail/model.ckpt-210000.meta"```
9. cd pretrained_downloaded_models/ckpt
10. ```gsutil -m cp   "gs://pegasus_ckpt/c4.unigram.newline.10pct.96000.model"   "gs://pegasus_ckpt/c4.unigram.newline.10pct.96000.vocab"   .```

If you face any errors in the above setup, Tensorflow versions may be different in your setup. We need Tensorflow 1.x version to work

## Code Structure
1. pegasus source is present under Model/pegasus folder.
2. The main module to generate summary data at runtime is in Model/summarize.py
3. To generate linkedin summary, call summarize.summarize_linkedin("<article_text>")
4. To generate twitter summary, call summarize.summarize_twitter("<article_text>")


Pegasus stands for Pre-training with Extracted Gap-sentences for Abstractive SUmmarization Sequence-to-sequence models. 
It uses self-supervised objective Gap Sentences Generation (GSG) to train a transformer encoder-decoder model.

@misc{zhang2019pegasus,
    title={PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization},
    author={Jingqing Zhang and Yao Zhao and Mohammad Saleh and Peter J. Liu},
    year={2019},
    eprint={1912.08777},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
