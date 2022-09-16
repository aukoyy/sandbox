

def chop(target, array):
  if len(array) == 0:
    return -1
  if len(array) == 1:
    if array[0] == target:
      return 0
    else:
      return -1
  mid = len(array) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return chop(target, array[:mid])
  else:
    return chop(target, array[mid:])



def assert_equal(var1, var2):
  print(f'{var1} == {var2} = {var1 == var2}')
  return var1 == var2


def test_chop():
  assert_equal(-1, chop(3, []))
  assert_equal(-1, chop(3, [1]))
  assert_equal(0,  chop(1, [1]))
  #
  assert_equal(0,  chop(1, [1, 3, 5]))
  assert_equal(1,  chop(3, [1, 3, 5]))
  assert_equal(2,  chop(5, [1, 3, 5]))
  assert_equal(-1, chop(0, [1, 3, 5]))
  assert_equal(-1, chop(2, [1, 3, 5]))
  assert_equal(-1, chop(4, [1, 3, 5]))
  assert_equal(-1, chop(6, [1, 3, 5]))
  #
  assert_equal(0,  chop(1, [1, 3, 5, 7]))
  assert_equal(1,  chop(3, [1, 3, 5, 7]))
  assert_equal(2,  chop(5, [1, 3, 5, 7]))
  assert_equal(3,  chop(7, [1, 3, 5, 7]))
  assert_equal(-1, chop(0, [1, 3, 5, 7]))
  assert_equal(-1, chop(2, [1, 3, 5, 7]))
  assert_equal(-1, chop(4, [1, 3, 5, 7]))
  assert_equal(-1, chop(6, [1, 3, 5, 7]))
  assert_equal(-1, chop(8, [1, 3, 5, 7]))


result = test_chop()
print(result)
