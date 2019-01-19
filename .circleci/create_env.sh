#!/bin/bash
conda create -y -n colorlover_env python=$PYTHON_VERSION nose coverage zip
source activate colorlover_env