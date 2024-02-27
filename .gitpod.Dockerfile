FROM gitpod/workspace-full

# Install Graphviz
RUN sudo apt-get update \
    && sudo apt-get -y install graphviz \
    && sudo apt-get -y intall libpq-dev \
    && sudo apt-get clean

# Install Java
RUN bash -c ". /home/gitpod/.sdkman/bin/sdkman-init.sh && \
    sdk install java 17.0.8-tem && \
    sdk default java 17.0.8-tem"
