from bottle import route, run, template
from bottle import route, request, response, template, HTTPResponse
from bottle import static_file
import matplotlib
import matplotlib.pyplot as plt
from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq,whiten
import csv
from Tkinter import *
import random
import json

# Fields in the data set
field_names = ['Sepal_length','Sepal_width','Petal_length','Petal_width']
@route('/')
def index():
    return template('user_interface')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="static")
    
@route('/cluster',  method='POST')
def clusterimage():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
           
            posted_values =  request.forms.dict
            x_param = posted_values["x"][0]
            y_param = posted_values["y"][0]
            noCluster = posted_values["cluster"][0]
            clusters = int(noCluster)
            
            data_arr = get_data_arr(x_param,y_param)
            
            data = vstack( data_arr )
            # Normalizing data
            data = whiten(data)
            # computing K-Means with clusters (clusters)
            centroids, distortion = kmeans(data,clusters)
            # assign each sample to a cluster
            idx,_ = vq(data,centroids)
          
            total_points =[]
            for i in range(clusters):
                result_names = data[idx==i, 0]
                print "================================="
                print "Cluster " + str(i+1)
                count = 0
                for name in result_names:
                   # print name
                    count +=1
                print "Total cluster points: "
                print(count)
                total_points.append(count)
                
            # some plotting using numpy's logical indexing
            print " ==================================="
            print(centroids[0:])
            
            centroid_points = []
            for row in centroids:
                cent = []
                cent.append(row[0])
                cent.append(row[1])
                centroid_points.append(cent)
            
            print(centroid_points[0:])
            
            colour = ["Db","Dr","Dg","Dy","Dk","Dc"]
            fig = plt.figure()
            for i in range(0,clusters):
                for j in range(0,1):
                    plt.plot(data[idx==i,j], data[idx==i,j+1],colour[i])
                    
                
            plt.plot(centroids[:,0],centroids[:,1],'hm',markersize=12)
            filename = "temp.png"
            returnData = json.dumps({'filename':filename,'total_points':total_points,'centroids':centroid_points})
            fig.savefig("./static/"+filename)
            resp = HTTPResponse(body=returnData,status=200)
            return resp
    else:
            return 'This is a normal request'

            
def get_data_arr(x_param, y_param):
    vector = []
    with open('something.csv', 'rb') as f:
        reader = csv.DictReader(f, fieldnames=field_names)
        for row in reader:
            vector_element = []
            vector_element.append(float(row[x_param]))
            vector_element.append(float(row[y_param]))
            vector.append(vector_element)
   
    return vector

run(host="0.0.0.0",port=8080)