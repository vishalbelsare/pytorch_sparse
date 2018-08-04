import torch
from torch_sparse import coalesce


def test_coalesce():
    row = torch.tensor([1, 0, 1, 0, 2, 1])
    col = torch.tensor([0, 1, 1, 1, 0, 0])
    index = torch.stack([row, col], dim=0)
    value = torch.tensor([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])

    index, value = coalesce(index, value, torch.Size([4, 2]))
    assert index.tolist() == [[0, 1, 1, 2], [1, 0, 1, 0]]
    assert value.tolist() == [[6, 8], [7, 9], [3, 4], [5, 6]]
