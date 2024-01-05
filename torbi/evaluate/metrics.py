import torch
import torchutil


###############################################################################
# Aggregate metric
###############################################################################


class Metrics:

    def __init__(self):
        self.rpas = [RPA(k) for k in torbi.PITCH_ERROR_THRESHOLDS]

    def __call__(self):
        return {f'rpa-{rpa.threshold}': rpa() for rpa in self.rpas}

    def update(self, predicted, target):
        for rpa in self.rpas:
            rpa.update(predicted, target)

    def reset():
        for rpa in self.rpas:
            rpa.reset()


###############################################################################
# Individual metrics
###############################################################################


class RPA(torchutil.metrics.Average):

    def __init__(self, threshold):
        super().__init__()
        self.threshold = threshold

    def update(predicted, target):
        super().update(
            torch.abs(predicted - target) <= self.threshold,
            predicted.numel())
