# coco2017-tfrecord
Create selective class tfrecord from coco2017 dataset
very simple selective class tfrecord creator from coco2017 dataset.

The program works jupyter notebook (.ipynb file)

## Getting Started

1. Clone this Repo .
2. Download cocoa2017 dataset with annotations files from:
http://cocodataset.org/#download

Under **"Images"** download 
```
2017 Train images [118K/18GB]
2017 Val images [5K/1GB]
```

Under **"Annotations"** download 
```
2017 Train/Val annotations [241MB]
```
#### Folder Structure
 - <#Dataset path#>
	 - annotations (folder)
	 - train2017
	 - val2017
	 - test2017 (not compulsory)

### Prerequisites

1. Python 3
2. COCO API
3. Tensorflow
4. numpy
5. PILLOW
6. Jupyter Notebook 

##### 1. Python 3 Installation
This you would already know

##### 2. COCO API Installation (Only if the import statement in jupyter notebook does not work)
You will need COCO API. Installation instruction can be found on this link [COCO API](https://github.com/cocodataset/cocoapi)
Still for your quick reference will list installation instruction:

Clone git repo:
```
git clone https://github.com/cocodataset/cocoapi
cd cocoapi/PythonAPI
make
```
*if you use 'python3' to run python files please make chanes in cocoapi/PythonAPI/Makefile (replace 'python' with 'python3')

##### 3. tensorflow Installation
```
pip3 install tensorflow
```
or 
```
pip3 install tensorflow-gpu
```

##### 4. numpy Installation
```
pip3 install numpy
```

##### 5. PILLOW Installation
```
pip3 install pillow
```

##### 6. Jupyter notebook Installation
```
pip3 install jupyter
```

### Running the program

Post cloning the Repo, go to repo dir.

```
jupyter notebook
```
the notebook will open in a browser. double click on ipynb file and start executing cell by cell :)

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details

### Star the REPO, if you find it useful. Feel free for pull requests.
## CHEERS!!! 

