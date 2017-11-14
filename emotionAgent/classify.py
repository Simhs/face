# -*- coding: utf-8 -*-

"""Inception v3 architecture 모델을 retraining한 모델을 이용해서 이미지에 대한 추론(inference)을 진행하는 예제"""

import numpy as np
import tensorflow as tf

class Image:
    def __init__(self):                                    # 추론을 진행할 이미지 경로
        self.modelFullPath = './temp/output_graph.pb'                                      # 읽어들일 graph 파일 경로
        self.labelsFullPath = './temp/output_labels.txt'                                # 읽어들일 labels 파일 경로

        # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
        self.create_graph()
        self.sess = tf.Session()

    def create_graph(self):
        """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
        # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
        with tf.gfile.FastGFile(self.modelFullPath, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

    def changedKnowlege(self):
        self.create_graph()
        self.sess = tf.Session()

    def run_inference_on_image(self,imagePath):
        answer = None
        if not tf.gfile.Exists(imagePath):
            tf.logging.fatal('File does not exist %s', imagePath)
            return answer
        image_data = tf.gfile.FastGFile(imagePath, 'rb').read()
        softmax_tensor = self.sess.graph.get_tensor_by_name('final_result:0')
        predictions = self.sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
        f = open(self.labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            #print('%s (score = %.5f)' % (human_string, score))
        answer = labels[top_k[0]]
        return answer,labels,predictions


if __name__ == '__main__':
    cf = Image()
    print "----------------------------"
    cf.run_inference_on_image("./1.jpg")
    print "----------------------------"
    cf.run_inference_on_image("./3.jpg")
    print "----------------------------"
    cf.run_inference_on_image("./a.jpg")
    print "----------------------------"
    cf.run_inference_on_image("./b.jpg")
    print "----------------------------"
    cf.run_inference_on_image("./c.jpg")
    print "----------------------------"
    cf.run_inference_on_image("./d.jpg")
    print "----------------------------"

