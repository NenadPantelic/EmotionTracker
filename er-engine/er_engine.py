import bentoml
import json
import numpy as np

from deepface import DeepFace
from bentoml.adapters import ImageInput, JsonOutput
from bentoml.service.artifacts import BentoServiceArtifact

@bentoml.env(infer_pip_packages = True)
@bentoml.artifacts([BentoServiceArtifact("er_engine")])
class EmotionRecognitionService(bentoml.BentoService):

    @bentoml.api(input=ImageInput(), output = JsonOutput(), batch=False)
    def predict(self, image):
        return DeepFace.analyze(np.array(image), actions = [ 'emotion' ], enforce_detection = False)