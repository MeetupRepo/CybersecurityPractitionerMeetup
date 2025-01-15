# LLM Vulnerabilities Demo

This project demonstrates various attacks on a language model (`TinyLLama`) to showcase vulnerabilities and exploits in generative AI. It also provides a Jupyter Notebook for executing the demonstrations interactively.


## Prerequisites
Before proceeding, ensure you have the following installed on your system:
- **Docker**: To set up the model in a container.
- **Jupyter Notebook**: To execute the demo interactively.

---

## Steps to Run the Demo

### Step 1: Clone the Repository
### Step 2: Run the docker container for model
1. sudo docker build -t llm-model-service .
2. sudo docker run -d   --name llm-model   -p 8000:8000   llm-model-service
### Step 3: Use the project notebook to wirk with nodel
### Step 4: Cleanup
1. sudo docker stop $(sudo docker ps -a -q)
2. sudo docker rm $(sudo docker ps -a -q)
3. sudo docker rmi $(sudo docker images -q)
4. sudo docker system prune -a -f

sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
sudo docker rmi $(sudo docker images -q)
sudo docker system prune -a -f

sudo docker build -t llm-model-service .
sudo docker run -d   --name llm-model   -p 8000:8000   llm-model-service