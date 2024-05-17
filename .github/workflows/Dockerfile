FROM quay.io/jupyter/scipy-notebook:2024-04-29

WORKDIR /usr/src/app

#COPY --chown=jovyan:users Test1.ipynb ./
RUN chmod -R 777 /usr/src/app

CMD ["jupyter", "nbconvert", "--execute", "Test1.ipynb", "--to", "notebook", "--inplace", "--ExecutePreprocessor.timeout=-1"]
