from pegasus.params import estimator_utils
from pegasus.params import registry
import tensorflow as tf
import pegasus.params.all_params
from pegasus.eval import text_eval
from pegasus.ops import public_parsing_ops
#from pegasus.data import infeed

import itertools
import os
import time

tf.enable_eager_execution()
use_tpu = False
iterations_per_loop = 1000
num_shards = 1


def summarize_linkedin(input_text, beam_size=1, beam_alpha=0.5):
    return summarize(input_text, model_dir="pretrained_downloaded_models/cnn_dailymail/model.ckpt-210000", transformer_name='cnn_dailymail_transformer', beam_size=beam_size, beam_alpha=beam_alpha)


def summarize_twitter(input_text, beam_size=1, beam_alpha=0.1):
    return summarize(input_text, model_dir="pretrained_downloaded_models/xsum/model.ckpt-30000", transformer_name='xsum_transformer', beam_size=beam_size, beam_alpha=beam_alpha)


def summarize(input_text, model_dir, transformer_name='cnn_dailymail_transformer',
              _SPM_VOCAB='./pretrained_downloaded_models/ckpt/c4.unigram.newline.10pct.96000.model', beam_size=5, beam_alpha=0.1):
    param_overrides = "vocab_filename=./pretrained_downloaded_models/ckpt/c4.unigram.newline.10pct.96000.model,batch_size=1,beam_size={0},beam_alpha={1}".format(beam_size, beam_alpha)
    master = ""
    checkpoint_path = model_dir
    params = registry.get_params(transformer_name)(param_overrides)
    pattern = params.dev_pattern
    parser, shapes = params.parser(mode=tf.estimator.ModeKeys.PREDICT)
    estimator = estimator_utils.create_estimator(master,
                                                 model_dir,
                                                 use_tpu,
                                                 iterations_per_loop,
                                                 num_shards, params)
    encoder = public_parsing_ops.create_text_encoder("sentencepiece", _SPM_VOCAB)
    target = input_text

    def input_function(params):
        # Passing input_text as both input_text and target. Disregard the estimator value.
        dataset = tf.data.Dataset.from_tensor_slices({"inputs":[input_text, input_text],"targets":[target, target]}).map(parser)
        dataset = dataset.unbatch()
        dataset = dataset.padded_batch(
            params["batch_size"],
            padded_shapes=shapes,
            drop_remainder=True)
        return dataset

    print("Checkpoint path is {0}".format(checkpoint_path))
    predictions = estimator.predict(input_fn=input_function, checkpoint_path=checkpoint_path)
    return " ".join([text_eval.ids2str(encoder, i['outputs'], None) for i in predictions])

