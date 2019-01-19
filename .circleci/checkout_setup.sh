#!/bin/bash
cd colorlover
git checkout ${CIRCLE_BRANCH}
pip install -I .