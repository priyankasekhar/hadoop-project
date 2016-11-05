#!/usr/bin/env python
import os
import weka.core.jvm as jvm
from flask import Flask, render_template,request,redirect,url_for,send_from_directory
import sys
application = Flask(__name__)

HOST = "<>.compute.amazonaws.com"
#PORT = int(os.getenv('VCAP_APP_PORT', 5004))

print"connected"
@application.route('/',methods=['POST', 'GET'])
def run():
    return render_template("index.html")

@application.route('/command',methods=['POST', 'GET'])
def command():
    jvm.start()

    import weka.core.converters as converters
    clusters = request.form['clusternum']
    a1 = request.form['firstcol']
    a2 = request.form['secondcol']
    # print clusters
    # print a1
    # print a2
    data = converters.load_any_file("small_data.csv")
    #data.class_is_last()

    print(data)

    # from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection
    # search = ASSearch(classname="weka.attributeSelection.BestFirst", options=["-D", "1", "-N", "5"])
    # evaluator = ASEvaluation(classname="weka.attributeSelection.CfsSubsetEval", options=["-P", "2", "-E", "1"])
    # attsel = AttributeSelection()
    # attsel.search(search)
    # attsel.evaluator(evaluator)
    # attsel.select_attributes(data)

    from weka.clusterers import Clusterer
    clusterer = Clusterer(classname="weka.clusterers.SimpleKMeans", options=["-N", "{}".format(clusters)])
    clusterer.build_clusterer(data)

    print(clusterer)

    # cluster the data
    for inst in data:
        cl = clusterer.cluster_instance(inst)  # 0-based cluster index
        dist = clusterer.distribution_for_instance(inst)   # cluster membership distribution
        print("cluster=" + str(cl) + ", distribution=" + str(dist))

    return render_template("output.html")

if __name__=="__main__":
    application.run(host=HOST)