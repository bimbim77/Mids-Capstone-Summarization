export PYTHONPATH=.
pip3 install -r requirements.txt
pip3 uninstall tensorflow_estimator
sudo apt-get install gcc python-dev python-setuptools libffi-dev
sudo apt-get install python-pip
pip3 install gsutil
pip3 install apache-beam
pip3 install pprint
pip3 install twython
pip3 install pandas
pip3 install sentencepiece
pip3 install tensorflow==1.14
pip3 install tensorflow-datasets==1.2.0
pip3 install tensorflow_text==1.15.1

# To test setup of tensorflow
python3 -c 'import tensorflow as tf; print(tf.sysconfig.get_lib())'

# Force change checksums.py to fix error when downloading models/datasets
sudo cp ./checksums.py /usr/local/lib/python3.7/dist-packages/tensorflow_datasets/core/download/checksums.py
