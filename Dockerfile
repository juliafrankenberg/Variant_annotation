FROM continuumio/miniconda3

WORKDIR /app  
COPY . /app  

# Create a conda environment and install dependencies
RUN conda env update -f environment.yml  
RUN echo "source activate variant_ann" > ~/.bashrc  

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py  

# Run the application
CMD ["bash", "-c", "source activate variant_ann && flask run --host=0.0.0.0"]
