FROM jupyter/base-notebook:python-3.8.13

# create user with a home directory
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

USER root

COPY . ${HOME}

RUN chown -R ${NB_UID} ${HOME}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN rmdir work

USER ${NB_USER}
