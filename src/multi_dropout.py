from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import random_ops

def multi_dropout(x, keep_prob, name=None):
  """Computes dropout with different probabilities for each value in x.
  With probability `keep_prob`, outputs the input element scaled up by
  `1 / keep_prob`, otherwise outputs `0`.  The scaling is so that the expected
  sum is unchanged.
  By default, each element is kept or dropped independently.
  Args:
    x: A floating point tensor.
    keep_prob: A floating point tensor with the same shape as x.
    name: A name for this operation (optional).
  Returns:
    A Tensor of the same shape of `x`.
  """
  with ops.name_scope(name, "ec_dropout", [x]) as name:
    # Check that x and keep_prob are the same shape

    x = ops.convert_to_tensor(x, name="x")

    random_tensor = keep_prob
    random_tensor += random_ops.random_uniform(array_ops.shape(keep_prob), dtype=x.dtype)

    # 0. if [keep_prob, 1.0) and 1. if [1.0, 1.0 + keep_prob)
    binary_tensor = math_ops.floor(random_tensor)
    #ret = math_ops.div(x, keep_prob) * binary_tensor
    return binary_tensor
