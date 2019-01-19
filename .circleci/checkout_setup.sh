#!/bin/bash
git clone https://github.com/jackparmer/colorlover.git
cd colorlover
git checkout ${CIRCLE_BRANCH}
pip install -I .