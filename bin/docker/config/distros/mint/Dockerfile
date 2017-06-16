FROM __image__

USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && \
    apt-get install sudo git ansible -y >> /dev/null

RUN apt-get install python-apt -y >> /dev/null

ENV USER runner
ENV FOLDER /runner
RUN /usr/sbin/groupadd $USER && \
    /usr/sbin/useradd $USER -m -d $FOLDER -g $USER -s /bin/bash && \
    echo $USER 'ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER $USER

WORKDIR $FOLDER
