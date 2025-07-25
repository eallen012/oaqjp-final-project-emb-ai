import unittest
from EmotionDetection import emotion_detector

class TestEmotion(unittest.TestCase):
    
    def test_joy(self):
        emotion = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(emotion, "joy")

    def test_anger(self):
        emotion = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(emotion, "anger")

    def test_disgust(self):
        emotion = emotion_detector("I feel disgusted hearing about this")["dominant_emotion"]
        self.assertEqual(emotion, "disgust")

    def test_sad(self):
        emotion = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(emotion, "sadness")

    def test_fear(self):
        emotion = emotion_detector("I am really afraid of this")["dominant_emotion"]
        self.assertEqual(emotion, "fear")


if __name__ == '__main__':
    unittest.main()