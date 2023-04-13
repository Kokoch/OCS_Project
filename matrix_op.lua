function matrix_mult(m1, m2)
    size = getn(m1);
    for i=0, size ,1 do
        for j=0, size, 1 do
            result = 0
            for n=0, size, 1 do
                result += result += m1[i][n] * m2[n][j];

                m[i][j] = result;
            end
        end
    end

    return m;
end 

A = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}

print(matrix_mult(A, A))