#FROM quay.io/jupyter/scipy-notebook:2024-04-29

#WORKDIR /usr/src/app

#COPY --chown=jovyan:users Test1.ipynb ./
#RUN chmod -R 777 /usr/src/app

#CMD ["jupyter", "nbconvert", "--execute", "Test1.ipynb", "--to", "notebook", "--inplace", "--ExecutePreprocessor.timeout=-1"]

FROM quay.io/jupyter/scipy-notebook:2024-04-29

USER root  # Switch to root to set permissions
WORKDIR /usr/src/app

# Ensure the directory has the right permissions
RUN mkdir -p /usr/src/app && chown -R jovyan:users /usr/src/app

COPY --chown=jovyan:users Test1.ipynb ./

USER jovyan  # Switch back to the jovyan user

CMD ["jupyter", "nbconvert", "--execute", "Test1.ipynb", "--to", "notebook", "--inplace", "--ExecutePreprocessor.timeout=-1"]

