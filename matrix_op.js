A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


function matrix_mult(m1, m2) {
    const size = m1[0].length;
    console.log(size);

    let m = [];
    const inner = [];
    
    for (let i=0; i < size; i++) {
        inner[i] = 0;
    }

    for (let i=0; i < size; i++) {
        m[i] = inner;
    }
    console.log(m);

    for (let i=0; i < size; i++) {
        for (let j=0; j < size; j++) {
            let result = 0;

            for (let n=0; n < size; n++) {
                result += m1[i][n] * m2[n][j]
            };
            m[i][j] = result;
        }
        
    }

    return m;
}

console.log(matrix_mult(A,A));