# Copyright 2021 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or  implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Configuration parameters for Neural LNS training."""

import ml_collections


def get_light_gnn_model_config():
    """Current best LightGNN config."""
    config = ml_collections.ConfigDict()

    # Tunable parameters
    config.params = ml_collections.ConfigDict()
    config.params.n_layers = 2  # GCN and output MLP layers (layer <=> set of weights)
    config.params.node_model_hidden_sizes = [64, 64]  # output width of each layer in GCN
    config.params.output_model_hidden_sizes = [32, 1]  # output width of each MLP layer (output model)
    config.params.dropout = 0.1

    return config


def get_config():
    """Training configuration."""
    config = ml_collections.ConfigDict()
    config.work_unit_dir = '/Users/sean/Documents/school/phd/courses/deep_learning/neural_lns/models'

    # Training config
    config.learning_rate = 1e-2
    config.decay_steps = 300
    config.num_train_run_steps = 10
    config.num_train_steps = 1000
    config.eval_every_steps = 500
    config.eval_steps = 128
    config.grad_clip_norm = 1.0

    # Each entry is a pair of (<dataset_path>, <prefix>).
    config.train_datasets = [
        ('/Users/sean/Documents/school/phd/courses/deep_learning/neural_lns/data/samples/facilities/test_100_100_5/instance_1.tfrecord', 'train'),
    ]

    config.valid_datasets = [
        ('/Users/sean/Documents/school/phd/courses/deep_learning/neural_lns/data/samples/facilities/test_100_100_5/instance_1.tfrecord', 'valid'),
    ]
    config.model_config = get_light_gnn_model_config()
    return config
