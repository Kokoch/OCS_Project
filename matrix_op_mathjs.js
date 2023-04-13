const math = require('mathjs')

const matrixA = math.matrix([[1,2,3], [4, 5, 6], [7, 8, 9]]);
const matrixB = math.matrix([[1, -1], [-2, 4], [-7, 4]]);

const matrix = math.multiply(matrixA, matrixA)
console.log(matrix)
