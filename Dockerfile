# DSCI_522_Group17 Project Dockerfile
# Author: Chun Chieh Chang, Sakshi Jain, Pan Fan
# Date: 2020/12/12


# Build from base image
FROM rocker/tidyverse

# Run Linux Update
RUN apt-get update

# install the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

# set environment
ENV PATH /opt/conda/bin:$PATH

# reinstall seaborn to resolve version conflict
RUN conda remove -y seaborn
RUN conda install -y seaborn=0.11.*

#install other Python Packages
RUN conda install -y docopt=0.6.*
RUN conda install -y scikit-learn=0.23.*
