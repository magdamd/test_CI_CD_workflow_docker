FROM quay.io/jupyter/scipy-notebook:2024-04-29

USER jovyan
WORKDIR /usr/src/app

# Copy the notebook file to the working directory
#COPY --chown=jovyan:users Test1.ipynb ./
#COPY --chown=jovyan:users ./results/arrayX.txt ./

COPY requirements_PlaygroundMR0_DockerImage.txt ./
RUN pip install --no-cache-dir -r requirements_PlaygroundMR0_DockerImage.txt

# Set permissions on the working directory
RUN chmod -R 777 /usr/src/app

CMD ["jupyter", "nbconvert", "--execute", "Test1.ipynb", "--to", "notebook", "--inplace", "--ExecutePreprocessor.timeout=-1"]

