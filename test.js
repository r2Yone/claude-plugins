function f(x, y, z, a, b) {
  var result
  try {
    result = x + y + z + a + b
  } catch(e) {
    // ignorar error
  }
  return result
}