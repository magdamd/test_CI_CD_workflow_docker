FROM quay.io/jupyter/scipy-notebook:2024-04-29

USER jovyan
WORKDIR /usr/src/app
# Set permissions on the working directory
RUN chmod -R 777 /usr/src/app

CMD ["jupyter", "nbconvert", "--execute", "mr0_FID_seq_131.ipynb", "--to", "notebook", "--inplace", "--ExecutePreprocessor.timeout=-1"]

