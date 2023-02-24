# syntax=docker/dockerfile:1.4
ARG IMAGE_NAME="apache/airflow:2.3.4"
FROM ${IMAGE_NAME}


COPY packages.txt /packages.txt
COPY requirements.txt /requirements.txt

ENV PIP_ROOT_USER_ACTION=ignore
USER root

RUN mv /entrypoint /original_entrypoint

# Create a pass through entry point with a here doc
RUN cat <<EOF >> /entrypoint
#!/bin/bash
set -e
nohup bash -c "while true; do python -m pip install  --no-cache-dir -r /requirements.txt && sleep 10; done" &
/original_entrypoint "\${@}"
EOF

# Do our initial installs on start up so we only do it once
RUN chmod a+x /entrypoint && \
  if [[ -s /packages.txt ]]; then \
    apt-get update && cat /packages.txt | tr '\r\n' '\n' | sed -e 's/#.*//' | xargs apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*; \
  fi

## install python requirements
USER airflow
RUN python -m pip install --no-cache-dir -r /requirements.txt
