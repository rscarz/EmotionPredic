from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        #I'm glad this happened  -->	alegría
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        #I'm really angry about this  -->	ira
        result_2 = emotion_detector('I am really angry about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        #I feel disgusted just hearing about this  -->	desagrado
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        #I'm so sad about this -->	tristeza
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        #I'm very afraid that this will happen  -->	miedo
        result_5 = emotion_detector('I am very afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()