from er_engine import EmotionRecognitionService

er_engine = EmotionRecognitionService()
er_engine.pack("er_engine", None)

saved_path = er_engine.save()