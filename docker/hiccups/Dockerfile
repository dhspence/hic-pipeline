FROM nvidia/cuda:8.0-devel-ubuntu16.04
LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

# Update the repository sources list
# Install base packages: java, git, wget
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    gawk \
    gcc \
    git \
    libz-dev \
    locales \
    make \
    unzip \
    bzip2 \
    libbz2-dev \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /opt/

# Install Juicer
RUN git clone --branch encode https://github.com/theaidenlab/juicer.git
RUN cd juicer && chmod +x CPU/* CPU/common/*

# Install Juicer tools
ADD http://s3.amazonaws.com/hicfiles.tc4ga.com/public/juicer/juicer_tools_1.11.09_jcuda.0.8.jar /opt/juicer/CPU/common
RUN ln -s /opt/juicer/CPU/common/juicer_tools_1.11.09_jcuda.0.8.jar /opt/juicer/CPU/common/juicer_tools.jar
RUN chmod 666 /opt/juicer/CPU/common/juicer_tools_1.11.09_jcuda.0.8.jar
RUN ln -s juicer/CPU scripts

# Version number contained in image
# ADD VERSION .

# For sorting, LC_ALL is C
ENV LC_ALL C
ENV PATH=/opt:/opt/scripts:/opt/scripts/common:$PATH
