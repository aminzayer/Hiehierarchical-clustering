# Hiehierarchical Clustering

Hierarchical Clustering Algorithm &amp; Methods with Python
In any clustering exercise, determining the number of clusters is a time-consuming process.
Because the commercial side of the business is more concerned with extracting meaning from these groups, it’s crucial to visualize the clusters in two dimensions and see if they’re distinct. 
PCA or Factor Analysis can be used to achieve this goal. This is a common method for presenting final results to various stakeholders, making it easier for everyone to consume the output.

# Example of Hiehierarchical Clustering
Now we look into examples using Python to demonstrate the Hierarchical Clustering Model

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8.10"
    },
    "colab": {
      "name": "hierarchical-clustering.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aminzayer/Hiehierarchical-clustering/blob/main/hierarchical_clustering.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4vmuuoFzvRYp"
      },
      "source": [
        "# Problem : Please Clustering Below Data with Hierarchical Algorithms\n",
        "# (1,3)-(4,2)-(5,6)-(3,1)-(7,2)-(3,3)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
        "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
        "execution": {
          "iopub.execute_input": "2021-12-07T16:07:53.609597Z",
          "iopub.status.busy": "2021-12-07T16:07:53.609240Z",
          "iopub.status.idle": "2021-12-07T16:07:53.615091Z",
          "shell.execute_reply": "2021-12-07T16:07:53.613977Z",
          "shell.execute_reply.started": "2021-12-07T16:07:53.609560Z"
        },
        "id": "_QQDf0AIvRY4"
      },
      "source": [
        "import numpy as np\n",
        "X = np.array([[1,3],[4,2],[5,6],[3,1],[7,2],[3,3],])"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "elIUEFE3vRY7"
      },
      "source": [
        "# Plotting Data "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "execution": {
          "iopub.execute_input": "2021-12-07T16:16:44.206826Z",
          "iopub.status.busy": "2021-12-07T16:16:44.206287Z",
          "iopub.status.idle": "2021-12-07T16:16:44.385770Z",
          "shell.execute_reply": "2021-12-07T16:16:44.384764Z",
          "shell.execute_reply.started": "2021-12-07T16:16:44.206777Z"
        },
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 222
        },
        "id": "or9yjcQJvRY8",
        "outputId": "dc2dea2f-cb67-48da-a47c-86f85e2384f8"
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "labels = range(1, 7)\n",
        "plt.figure(figsize=(7, 3))\n",
        "plt.subplots_adjust(bottom=0.1)\n",
        "plt.scatter(X[:,0],X[:,1], label='True Position')\n",
        "\n",
        "for label, x, y in zip(labels, X[:, 0], X[:, 1]):\n",
        "    plt.annotate(\n",
        "        label,\n",
        "        xy=(x, y), xytext=(-3, 3),\n",
        "        textcoords='offset points', ha='right', va='bottom')\n",
        "plt.show()"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAaIAAADNCAYAAAD63nRUAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAP1klEQVR4nO3db2xVdZ7H8c+HtsYOg9MYygitbudRKUGWwo3EOCGsBso4ZAJCjIrjPwgbs5lA3HQcfLLxiWOsTjRuMgmRnXUcZyYzisTgLNUohoWopFAIo9AHq0ykMFCzqQJpVqjffcDF+Kekt3DP/d0/71fScHvu8Z7Pyb320/M7v9PjiBAAAKlMSh0AAFDbKCIAQFIUEQAgKYoIAJAURQQASIoiAgAkRREBKIjtK23vsX3A9vu2H02dCdXBXEcEoBC2LWlyRJy23SBpl6T1EfFu4miocPWpAwCoDHH+t9bT+W8b8l/8JovLxtAcgILZrrO9X9JJSW9ExHupM6HyUUQAChYRoxExV1KrpBtsz06dCZUvk3NEU6dOjba2tqK/LoDycezYMU2aNEnXXHNN6iioAHv37v0kIprHei6Tc0RtbW3q6+vL4qUBJDI0NKSGhgY1NTVpZGRES5Ys0cMPP6xly5aljoYKYPtvF3uOyQoACnL8+HHde++9Gh0d1RdffKHbb7+dEkJRUEQACjJnzhz19/enjoEqVNBkBdtNtl+yfdj2Ids3Zh0MAFAbCj0iekbS9ohYZfsKSd/JMBOACrK1f1A9vQM6NjyiGU2N6u5q1/LOltSxUEHGLSLb35O0UNJ9khQRn0v6PNtYACrB1v5BbdxyUCNnRyVJg8Mj2rjloCRRRihYIUNzP5A0JOk3tvttP2d7csa5AFSAnt6BL0vogpGzo+rpHUiUCJWokCKqlzRP0q8jolPSGUm/+OZKttfZ7rPdNzQ0VOSYAMrRseGRCS0HxlJIER2VdPQrf8rjJZ0vpq+JiE0RkYuIXHPzmNcsAagyM5oaJ7QcGMu4RRQRf5f0se32/KJbJH2QaSoAFaG7q12NDXVfW9bYUKfurvaL/BfAtxU6a+5nkl7Mz5j7UNL92UUCUCkuTEhg1hwuR0FFFBH7JeUyzgKgAi3vbKF4cFn469sAgKQoIgBAUhQRACApiggAkBRFBABIiiICACRFEQEAkqKIAABJUUQAgKQoIgBAUhQRACApiggAkBRFBABIiiICACRFEQEAkqKIAABJUUQAgKQoIgBAUhQRACApiggAkBRFBABIiiICACRVX8hKto9IOiVpVNK5iMhlGQoAUDsKKqK8f4qITzJLAgCoSQzNAQCSKrSIQtLrtvfaXpdlIABAbSl0aO6HETFoe5qkN2wfjoidX10hX1DrJOm6664rckwAQLUq6IgoIgbz/56U9IqkG8ZYZ1NE5CIi19zcXNyUAICqNW4R2Z5se8qFx5KWSPpr1sEAALWhkKG570t6xfaF9X8fEdszTQUAqBnjFlFEfCjpH0uQBQBQg5i+DQBIiiICACRFEQEAkqKIAABJUUQAgKQoIgBAUhQRACApiggAkBRFBABIiiICACRFEQEAkqKIAABJUUQAgKQoIgBAUhQRACApiggAkBRFBABIiiICACRFEQEAkqKIAABJUUQAgKQKLiLbdbb7bW/LMhAAoLZM5IhovaRDWQUBANSmgorIdqukH0t6Lts4AIBaU+gR0dOSfi7piwyzAABq0LhFZHuZpJMRsXec9dbZ7rPdNzQ0VLSAAIDqVsgR0U2SfmL7iKQ/SrrZ9u++uVJEbIqIXETkmpubixwTAFCtxi2iiNgYEa0R0SbpDklvRcTdmScDANQEriMCACRVP5GVI+JtSW9nkgQAUJM4IgIAJEURAQCSoogAAElRRACApCgiAEBSFBEAICmKCACQFEUEAEiKIgIAJEURAQCSoogAAElRRACApCgiAEBSyYrogQce0LRp0zR79uxUEZCR4eFhrVq1SjNnzlRHR4feeeed1JEAlLFkRXTfffdp+/btqTaPDK1fv15Lly7V4cOHdeDAAXV0dKSOBKCMJSuihQsX6uqrr061eWTk008/1c6dO7VmzRpJ0hVXXKGmpqbEqQCUM84Roag++ugjNTc36/7771dnZ6fWrl2rM2fOpI4FoIxRRCiqc+fOad++fXrwwQfV39+vyZMn6/HHH08dC0AZo4hQVK2trWptbdWCBQskSatWrdK+ffsSpwJQzigiFNU111yja6+9VgMDA5KkN998U7NmzUqcCkA5S1ZEd955p2688UYNDAyotbVVmzdvThUFRfbss89q9erVmjNnjvbv369HHnkkdSQAZcwRUfQXzeVy0dfXV/TXBQBUJtt7IyI31nPjHhHZvtL2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\n",
            "text/plain": [
              "<Figure size 504x216 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c9v50PfyvRZB"
      },
      "source": [
        "# Use Hierarchical Algorithm Single Method"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "execution": {
          "iopub.execute_input": "2021-12-07T16:16:56.892869Z",
          "iopub.status.busy": "2021-12-07T16:16:56.892536Z",
          "iopub.status.idle": "2021-12-07T16:16:57.101980Z",
          "shell.execute_reply": "2021-12-07T16:16:57.100976Z",
          "shell.execute_reply.started": "2021-12-07T16:16:56.892837Z"
        },
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 214
        },
        "id": "xCk70GZlvRZB",
        "outputId": "ea8f74bb-4134-43b7-e35c-ea019b008e4c"
      },
      "source": [
        "from scipy.cluster.hierarchy import dendrogram, linkage\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
        "linked = linkage(X, 'single')\n",
        "\n",
        "labelList = range(1, 7)\n",
        "\n",
        "plt.figure(figsize=(7, 3))\n",
        "dendrogram(linked,orientation='top',labels=labelList,distance_sort='descending',show_leaf_counts=True)\n",
        "plt.show()"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 504x216 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8Z50YBFzvRZD"
      },
      "source": [
        "# Use Hierarchical Algorithm Complete Method"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "execution": {
          "iopub.execute_input": "2021-12-07T16:20:35.276076Z",
          "iopub.status.busy": "2021-12-07T16:20:35.275791Z",
          "iopub.status.idle": "2021-12-07T16:20:35.489041Z",
          "shell.execute_reply": "2021-12-07T16:20:35.487923Z",
          "shell.execute_reply.started": "2021-12-07T16:20:35.276046Z"
        },
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 214
        },
        "id": "2MdRmvlIvRZE",
        "outputId": "5ad3e265-2a8e-4ca6-8734-7254fbd36e48"
      },
      "source": [
        "from scipy.cluster.hierarchy import dendrogram, linkage\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
        "linked = linkage(X, 'complete')\n",
        "\n",
        "labelList = range(1, 7)\n",
        "\n",
        "plt.figure(figsize=(7, 3))\n",
        "dendrogram(linked,orientation='top',labels=labelList,distance_sort='descending',show_leaf_counts=True)\n",
        "plt.show()"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 504x216 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jqpp-NdvvRZF"
      },
      "source": [
        "# Use Hierarchical Algorithm Average Method"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "execution": {
          "iopub.execute_input": "2021-12-07T16:21:45.157157Z",
          "iopub.status.busy": "2021-12-07T16:21:45.156808Z",
          "iopub.status.idle": "2021-12-07T16:21:45.358851Z",
          "shell.execute_reply": "2021-12-07T16:21:45.357873Z",
          "shell.execute_reply.started": "2021-12-07T16:21:45.157080Z"
        },
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 214
        },
        "id": "PYdPnMwKvRZH",
        "outputId": "dc291fa7-1e53-4beb-ff83-1e6886afb64d"
      },
      "source": [
        "from scipy.cluster.hierarchy import dendrogram, linkage\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
        "linked = linkage(X, 'average')\n",
        "\n",
        "labelList = range(1, 7)\n",
        "\n",
        "plt.figure(figsize=(7, 3))\n",
        "dendrogram(linked,orientation='top',labels=labelList,distance_sort='descending',show_leaf_counts=True)\n",
        "plt.show()"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAaIAAADFCAYAAAAWjfY5AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAKrElEQVR4nO3df4hldR3G8edxd0tBrcDJDRWnwixJuObgP2INkvijsv7oD90MlGKk2NAKykDIXyH9Y0JZMrS2kk4iJFH2CymHUNKatSnzJ2Zaay6Olej6Y019+uPetXVznbvunPuZOef9gsPOuffu2WcPu/e533u+93udRAAAVNmrOgAAoNsoIgBAKYoIAFCKIgIAlKKIAAClKCIAQKnVTRz0gAMOyPj4eBOHBgCsQJs2bXo8ydir3ddIEY2Pj2tubq6JQwMAViDbD+/qPt6aAwCUoogAAKUoIgBAKYoIAFCqkckKlaanpZmZ6hSosG6dNDVVnQLA7mrdiGhmRpqfr06BUZuf5wUIsFK1bkQkSb2eNDtbnQKjNDlZnQDA69W6EREAYGWhiAAApSgiAEApiggAUKqVkxW6rotT2LfPlOzapAWmrKMNGBG1UBensPd6/a1LmLKOtmBE1FJMYW+/ro3+0F6MiAAApSgiAEApiggAUIoiAgCUoogAAKUoIgBAqaGLyPYq23+wfWOTgQAA3bI7I6JzJN3TVBAAQDcNVUS2D5b0IUnfbTYOAKBrhh0RXS7pS5Je2tUDbE/ZnrM9t7CwsCThAADtt2gR2f6wpMeSbHqtxyWZTjKRZGJsbGzJAgIA2m2YEdGxkk61/ZCk6yQdb/uaRlMBADpj0SJK8pUkBycZl3SapF8nOaPxZACATuBzRACAUrv1NRBJZiXNNpIEANBJjIgAAKUoIgBAKYoIAFCKIgIAlKKIAAClKCIAQCmKCABQiiICAJSiiAAApSgiAEApiggAUIoiAgCUoogAAKUoIgBAKYoIAFCKIgIAlKKIAAClKCIAQCmKCABQiiICAJSiiAAApSgiAEApiggAUIoiAgCUoogAAKUWLSLbe9v+ne0/2r7L9oWjCAYA6IbVQzxmm6Tjk2y1vUbSLbZ/nuS2hrMBADpg0SJKEklbB7trBluaDAUA6I6hrhHZXmV7XtJjkm5KcnuzsQAAXTFUESV5MUlP0sGSjrH93p0fY3vK9pztuYWFhaXOCQBoqd2aNZfkCUk3SzrpVe6bTjKRZGJsbGyp8gEAWm6YWXNjtt88+HkfSSdIurfpYACAbhhm1tzbJF1te5X6xXV9khubjQUA6IphZs39SdJRI8gCAOggVlYAAJSiiAAApSgiAEApiggAUIoiAgCUGmb6NrDiTG+a1sydM9UxGjW/5XJJ0uTGc4uTNGvdkes0dfRUdQw0iCJCK83cOaP5LfPqre1VR2lM77x2F5AkzW+ZlySKqOUoIrRWb21Ps2fOVsfAHpjcOFkdASPANSIAQCmKCABQiiICAJSiiAAApSgiAEApiggAUIoiAgCUoogAAKUoIgBAKYoIAFCKIgIAlKKIAAClKCIAQCmKCABQiiICAJSiiAAApSgiAEApiggAUGrRIrJ9iO2bbd9t+y7b54wiGACgG1YP8ZgXJH0xyR2295O0yfZNSe5uOBsAoAMWHREleTTJHYOfn5J0j6SDmg4GAOiG3bpGZHtc0lGSbn+V+6Zsz9meW1hYWJp0AIDWG7qIbO8r6YeSzk3y5M73J5lOMpFkYmxsbCkzAgBabKgisr1G/RK6NskNzUYCAHTJMLPmLGmDpHuSXNZ8JABAlwwzIjpW0iclHW97frCd0nAuAEBHLDp9O8ktkjyCLACADmJlBQBAKYoIAFCKIgIAlBpmiR8AK9D0pmnN3DlTHWOPzG+ZlyRNbpysDbKH1h25TlNHT1XHWLYYEQEtNXPnzMtP5CtVb21PvbW96hh7ZH7L/Ip/QdA0RkRAi/XW9jR75mx1jE5b6aO5UWBEBAAoRREBAEpRRACAUhQRAKAURQQAKEURAQBKUUQAgFJ8jghAq1WvMLFcVodYzqs7MCIC0GrVK0wsh9UhlvvqDoyIALRe11eYqB6NLYYREQCgFEUEAChFEQEASlFEAIBSFBEAoBRFBAAoRREBAEpRRACAUhQRAKDUokVk+yrbj9n+8ygCAQC6ZZgR0UZJJzWcAwDQUYsWUZLfSPrXCLIAADpoya4R2Z6yPWd7bmFhYakOCwBouSUroiTTSSaSTIyNjS3VYQEALcesOQBAKYoIAFBqmOnbP5D0W0mH295s+1PNxwIAdMWi39Ca5PRRBAEAdBNvzQEASlFEAIBSFBEAoBRFBAAoRREBAEpRRACAUhQRAKAURQQAKEURAQBKUUQAgFIUEQCgFEUEAChFEQEASlFEAIBSFBEAoBRFBAAoRREBAEpRRACAUhQRAKAURQQAKEURAQBKUUQAgFIUEQCgFEUEAChFEQEASg1VRLZPsn2f7Qdsn9d0KABAdyxaRLZXSbpC0smSjpB0uu0jmg4GAOiGYUZEx0h6IMmDSZ6XdJ2kjzYbCwDQFcMU0UGS/r7D/ubBbQAA7LHVS3Ug21OSpga7W23ft1THfn15Kv/05YFzIPksTgLnoI/zUH4ODt3VHcMU0SOSDtlh/+DBba+QZFrS9G5HAwB02jBvzf1e0mG23277DZJOk/TjZmMBALpi0RFRkhdsr5f0S0mrJF2V5K7GkwEAOsFJqjMAADqMlRUAAKUoIgBAKYoIAFCqVUVk+xrbj9p+0vb9tj9dnWnUbM/afs721sFW+nmuCrbX256zvc32xuo8lWwfNvj3cE11llGz/UbbG2w/bPsp2/O2T67OVcH2abbvsf207b/YPq46045aVUSSLpU0nmR/SadKusT20cWZKqxPsu9gO7w6TIF/SLpE0lXVQZaBK9T/CEYXrVZ/VZgPSHqTpPMlXW97vDDTyNk+QdLXJZ0laT9J75f0YGmonbSqiJLclWTb9t3B9s7CSCiQ5IYkP5L0z+oslWyfJukJSb+qzlIhydNJLkjyUJKXktwo6a+Suvbi9EJJFyW5bXAeHknyf4sSVGpVEUmS7W/bfkbSvZIelfSz4kgVLrX9uO1bbU9Wh8Ho2d5f0kWSvlCdZbmwfaCkd0nqzOcgB9+eMCFpbPA1Ppttf8v2PtXZdtS6IkryWfWHn8dJukHSttf+Ha3zZUnvUH9h2mlJP7HNqLB7Lpa0Icnm6iDLge01kq6VdHWSe6vzjNCBktZI+rj6z4k9SUep/zblstG6IpKkJC8muUX9dfE+U51nlJLcnuSpJNuSXC3pVkmnVOfC6NjuSfqgpG9UZ1kObO8l6fuSnpe0vjjOqD07+PWbSR5N8riky7TMnhOWbPXtZWq1uEYUSSw73C2TksYl/c39Jdj3lbTK9hFJ3leYa+TcPwEb1B8ZnJLkP8WRRirJv21vVv954OWbq/LsSmtGRLbfOpiiuK/tVbZPlHS6OnSh1vabbZ9oe2/bq21/Qv0ZMr+ozjZKg7/73uqvjbhq+/mozjVC0+q/AOsNtisl/VTSiZWhinxH0nskfSTJs4s9uKW+J+lzg+fIt0j6vKQbizO9Qpv+c0b9t+GuVL9gH5Z0bpIurRS+Rv1py++W9KL6EzY+luT+0lSjd76kr+6wf4b6M4cuKEkzYkmekfTM9n3bWyU9l2ShLtXo2T5U0tnqXyfe4v99QdfZSa4tCzZ6F0s6QNL9kp6TdL2kr5Um2gmLngIASrXmrTkAwMpEEQEASlFEAIBSFBEAoBRFBAAoRREBAEpRRACAUhQRAKAURQQAKPVf4RVWDOE5MEAAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 504x216 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WVzERCghzZxJ"
      },
      "source": [
        "# Use Hierarchical Algorithm Ward Method"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 214
        },
        "id": "H9WLB4unzzi_",
        "outputId": "03125ae1-67b5-4108-d622-16cec54bb3e3"
      },
      "source": [
        "from scipy.cluster.hierarchy import dendrogram, linkage\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
        "linked = linkage(X, 'ward')\n",
        "\n",
        "labelList = range(1, 7)\n",
        "\n",
        "plt.figure(figsize=(7, 3))\n",
        "dendrogram(linked,orientation='top',labels=labelList,distance_sort='descending',show_leaf_counts=True)\n",
        "plt.show()"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAaIAAADFCAYAAAAWjfY5AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAL80lEQVR4nO3dcYykd13H8c+Hu4OiLdSkQ89QjkWC1UbClG6aGCyuKLYgon/wx/XAhEazRFPSqolWQwIChvgPYhQhE69cY7uQphSiFauNsmlKoHEXJx7tHQ3WVq720q3a0Gvp1ZaPf8ysnMeVea43z3x353m/ksnOM/Pc7Gcne/PZ3zO/+T1OIgAAqrygOgAAoNsoIgBAKYoIAFCKIgIAlKKIAAClKCIAQKmdbTzoeeedl4WFhTYeGgCwDa2vrz+apHeq+1opooWFBa2trbXx0ACAbcj2g891H4fmAAClKCIAQCmKCABQqlER2T7X9i22D9s+ZPsn2w4GAOiGppMV/kTS7UneYfuFkn6gxUyYYDCQVlaqUwBoat8+aXm5OsXWNXFEZPulkt4oab8kJXk6yWNtB8NzW1mRhsPqFACaGA75w3GSJiOiV0nakPQp26+TtC7pmiRPnLiT7WVJy5K0Z8+eaefESfp9aXW1OgWASZaWqhNsfU3eI9op6fWSPpHkYklPSLru5J2SDJIsJlns9U75mSUAAL5HkyI6IulIkrvH27doVEwAAJyxiUWU5Kikb9q+cHzTz0q6t9VUAIDOaDpr7r2SbhrPmLtf0lXtRQIAdEmjIkoylLTYchYAQAexsgIAoBRFBAAoRREBAEpRRACAUhQRAKAURQQAKEURAQBKUUQAgFIUEQCgFEUEAChFEQEASlFEAIBSFBEAoBRFBAAoRREBAEpRRACAUo1OjGf7AUmPS3pW0jNJOEkeAGAqmp4qXJJ+JsmjrSUBAHQSh+YAAKWaFlEk/b3tddvLbQYCAHRL00NzP5XkIdsvk3SH7cNJ7jxxh3FBLUvSnj17phwTADCvGo2Ikjw0/vqIpM9JuvQU+wySLCZZ7PV6000JAJhbE4vI9g/aPmfzuqSfl/S1toMBALqhyaG58yV9zvbm/itJbm81FQCgMyYWUZL7Jb1uBlkAAB3E9G0AQCmKCABQiiICAJSiiAAApSgiAEApiggAUIoiAgCUoogAAKVO53xEALDtDAbSykrd9x8OR1+XluoySNK+fdLyFj13AiMiAHNtZeW7ZVCh3x9dKg2HtWU8CSMiAHOv35dWV6tT1KkejU3CiAgAUIoiAgCUoogAAKUoIgBAKYoIAFCKIgIAlGpcRLZ32P5n27e1GQgA0C2nMyK6RtKhtoIAALqpURHZvkDSL0j6i3bjAAC6pumI6GOSfkfSd1rMAgDooIlFZPttkh5Jsj5hv2Xba7bXNjY2phYQADDfmoyI3iDp7bYfkPQZSW+yfePJOyUZJFlMstjr9aYcEwAwryYWUZLfS3JBkgVJeyX9Y5J3tZ4MANAJfI4IAFDqtE4DkWRV0morSQAAncSICABQiiICAJSiiAAApSgiAEApiggAUIoiAgCUoogAAKUoIgBAKYoIAFCKIgIAlKKIAAClKCIAQCmKCABQiiICAJSiiAAApSgiAEApiggAUGriGVptnyXpTkkvGu9/S5L3tx3s+RqsD7RycKU6RquGRz8mSVo6cG1xknbte+0+LV+yXB0DQMuanCr8uKQ3JTlme5eku2z/bZKvtJzteVk5uKLh0aH6u/vVUVrTv26+C0iShkeHkkQRAR0wsYiSRNKx8eau8SVthjpT/d19rb57tToGzsDSgaXqCABmpNF7RLZ32B5KekTSHUnuPsU+y7bXbK9tbGxMOycAYE41KqIkzybpS7pA0qW2f+IU+wySLCZZ7PV6084JAJhTpzVrLsljkr4o6Yp24gAAumZiEdnu2T53fP3Fkt4s6XDbwQAA3dBk1twPS7rB9g6NiuvmJLe1GwsA0BVNZs39i6SLZ5AFANBBrKwAAChFEQEASlFEAIBSFBEAoBRFBAAoRREBAEpRRACAUhQRAKAURQQAKEURAQBKUUQAgFIUEQCgFEUEAChFEQEASlFEAIBSFBEAoBRFBAAoNbGIbL/C9hdt32v7HtvXzCIYAKAbJp4qXNIzkn47yVdtnyNp3fYdSe5tORsAoAMmjoiSPJzkq+Prj0s6JOnlbQcDAHTDab1HZHtB0sWS7j7Ffcu212yvbWxsTCcdAGDuNS4i22dL+qyka5N86+T7kwySLCZZ7PV608wIAJhjjYrI9i6NSuimJLe2GwkA0CVNZs1Z0n5Jh5J8tP1IAIAuaTJr7g2SfkXSQdvD8W2/n+QL7cXCmRisD7RycKU6xhkZHh39qi0dWKoNcob2vXafli9Zro4BbGkTiyjJXZI8gyyYkpWDKxoeHaq/u18d5Xnbztk3bZYpRQR8f01GRNiG+rv7Wn33anWMTtvuozlgVljiBwBQiiICAJSiiAAApSgiAEApiggAUIoiAgCUoogAAKX4HBHm0lZYXWIrrA7Byg7YDhgRYS5tri5Rqb+7X7pCxPDosLyMgSYYEWFudX11CVZ2wHbBiAgAUIoiAgCUoogAAKUoIgBAKYoIAFCKIgIAlJpYRLavt/2I7a/NIhAAoFuajIgOSLqi5RwAgI6aWERJ7pT0XzPIAgDooKm9R2R72faa7bWNjY1pPSwAYM5NrYiSDJIsJlns9XrTelgAwJxj1hwAoBRFBAAo1WT69qclfVnShbaP2P7V9mMBALpi4mkgklw5iyAAgG7i0BwAoBRFBAAoRREBAEpRRACAUhQRAKAURQQAKEURAQBKUUQAgFIUEQCgFEUEAChFEQEASlFEAIBSFBEAoBRFBAAoRREBAEpRRACAUo2KyPYVtr9u+xu2r2s7FACgO5qcKnyHpI9LeoukiyRdafuitoMBALqhyYjoUknfSHJ/kqclfUbSL7UbCwDQFU2K6OWSvnnC9pHxbQAAnLGd03og28uSlsebx2x/fVqP/bzyXOXKb78l8BzwHEg8B5vM01D9HLzyue5oUkQPSXrFCdsXjG/7f5IMJA1OOxoAoNOaHJr7J0mvsf0q2y+UtFfSX7UbCwDQFRNHREmesX21pL+TtEPS9UnuaT0ZAKATnKQ6AwCgw1hZAQBQiiICAJSiiAAApeaqiGxfbXvN9nHbB6rzVLL9GttP2b6xOsss2X6R7f22H7T9uO2h7bdU56pge6/tQ7afsP2vti+rzjRrtm+0/bDtb9m+z/avVWeaNdur49eCY+NL6Wc8T2WuikjSf0j6sKTrq4NsAR/XaOp91+zUaCWQn5b0Uknvk3Sz7YXCTDNn+82S/kjSVZLOkfRGSfeXhqrxEUkLSV4i6e2SPmz7kuJMFa5Ocvb4cmF1mJPNVREluTXJ5yX9Z3WWSrb3SnpM0j9UZ5m1JE8k+UCSB5J8J8ltkv5NUtdefP5A0geTfGX8PDyU5Hs+iD7vktyT5Pjm5vjy6sJIOIW5KiJItl8i6YOSfqs6y1Zg+3xJPyqpM599G6+YvyipNz51yxHbf2b7xdXZKtj+c9tPSjos6WFJXyiOVOEjth+1/SXbS9VhTkYRzZ8PSdqf5Eh1kGq2d0m6SdINSQ5X55mh8yXtkvQOSZdJ6ku6WKPDlJ2T5Dc0Ojx5maRbJR3//v9i7vyupB/RaLHqgaS/tr2lRoUU0Ryx3Zf0c5L+uDpLNdsvkPSXkp6WdHVxnFn79vjrnyZ5OMmjkj4q6a2FmUoleTbJXRqtlfnr1XlmKcndSR5PcjzJDZK+pC32uzC11bexJSxJWpD07x4ts3u2pB22L0ry+sJcM+XRD79fo5HBW5P8T3GkmUry37aPaPR+yP/dXJVni9kp3iOKpC21FvlcjYhs77R9lkZr4u2wfZbtLpXtQKP/ZP3x5ZOS/kbS5ZWhCnxC0o9L+sUk356085z6lKT32n6Z7R+S9JuSbivONFPjn32v7bNt77B9uaQr1aFJPLbPtX355muh7XdqNIPy9upsJ5q3F+n3SXr/Cdvv0mj20AdK0sxYkiclPbm5bfuYpKeSbNSlmi3br5T0Ho3eBzjq756A5T1JbioLNnsfknSepPskPSXpZkl/WJpo9qLRYbhPavRH94OSrk3SpbMH7NLoIy0/JulZjSZs/HKS+0pTnYRFTwEApebq0BwAYPuhiAAApSgiAEApiggAUIoiAgCUoogAAKUoIgBAKYoIAFCKIgIAlPpfiLvLkgxPfmkAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 504x216 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fdhuYIeG0WNf"
      },
      "source": [
        "# Use Hierarchical Algorithm Centroid Method"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 214
        },
        "id": "v-3JSI8t0cKn",
        "outputId": "58c108de-5864-4f2c-9710-b229f2930d8b"
      },
      "source": [
        "from scipy.cluster.hierarchy import dendrogram, linkage\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
        "linked = linkage(X, 'centroid')\n",
        "\n",
        "labelList = range(1, 7)\n",
        "\n",
        "plt.figure(figsize=(7, 3))\n",
        "dendrogram(linked,orientation='top',labels=labelList,distance_sort='descending',show_leaf_counts=True)\n",
        "plt.show()"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 504x216 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SMymoVGa02ky"
      },
      "source": [
        "# Use Hierarchical Algorithm Median Method"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 214
        },
        "id": "nJyyTal21DLo",
        "outputId": "8f05a429-da76-47d7-c335-61ec2a05589f"
      },
      "source": [
        "from scipy.cluster.hierarchy import dendrogram, linkage\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
        "linked = linkage(X, 'median')\n",
        "\n",
        "labelList = range(1, 7)\n",
        "\n",
        "plt.figure(figsize=(7, 3))\n",
        "dendrogram(linked,orientation='top',labels=labelList,distance_sort='descending',show_leaf_counts=True)\n",
        "plt.show()"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 504x216 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}
