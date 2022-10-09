#!/usr/bin/env node

function chain_size(row, col, wrking) {
    if (row < 0 || col < 0 || row >= wrking.length || col >= wrking[row].length)
        return 0;

    if (wrking[row][col] <= 0)  // has been visted or is an empty cell
        return 0;
    
    wrking[row][col] = -1 * wrking[row][col];  // mark space as checked 
    let size = 1;  // bounds check passed and is a region of puyos 
    let temp_current_val = Math.abs(wrking[row][col]);    
    // check adjacent cells
    for (let x = parseInt(-1); x <= 1; x++) {
        for (let y = parseInt(-1); y <= 1; y++) {
            if (x + row > 0 && col + y > 0 && x + row < wrking.length && col + y < wrking[0].length &&
                !(x == 0 && y == 0) &&
                (temp_current_val == wrking[row + x][col + y])) {
                size += chain_size(row + x, col + y, wrking);
            }
        }
    }
    
    // if size is greater than 4 then "pop" the puyo
    if (size >= 4)
        pop_region(row, col, wrking);
    
    return size;
}


// just dfs again
function pop_region(row, col, wrking) {
    if (row < 0 || col < 0 || row >= wrking.length || col >= wrking[row].length)
        return;
    if (wrking[row][col] == 0)
        return;
 
    //wrking[row][col] = 0; // pop the puyo
    popped_puyos.push([row, col]);
    let temp_current_val = Math.abs(wrking[row][col]);
    wrking[row][col] = 0

    for (let x = -1; x <= 1; x++) {
        for (let y = -1; y <= 1; y++) {
            if (x + row > 0 && col + y > 0 && x + row < wrking.length && col + y < wrking[0].length &&
                !(x == 0 && y == 0) && (temp_current_val == Math.abs(wrking[row + x][col + y])))
                pop_region(row + x, col + y, wrking); 
        }
    }
}

// driver code
popped_puyos = []

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
input_array = []
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
  input_array = _input.split("\n");
  main();
})

function main() {
    var [m,n] = input_array[0].split(" ") 
    mat = []
    for (let row = 1; row < parseInt(m) + 1; row++) {
        mat.push(input_array[row].trim().split(" "));
    }
 
    for (let i = 0; i < mat.length; i++) {
        for (let j = 0; j < mat[0].length; j++) {
            chain_size(i, j, mat);
        }
    }
    
    popped_puyos.sort((e1, e2) => {
        if( e1[0] !== e2[0] ) 
            return e1[0] - e2[0];
        else 
            return e1[1] - e2[1];
            
    })

    for (const cord of popped_puyos) {
        console.log("%d %d", cord[0], cord[1]);
    }
}
