// true means X, false means O
var state = true;
var grid = [[null, null, null],
            [null, null, null],
            [null, null, null]
]
var over = false;



function gameover(){
    for(i=0;i<3;i++){
        if(grid[i][0]!=null && grid[i][0]==grid[i][1] && grid[i][1]==grid[i][2]){
            return [true, grid[i][0]]
        }else if(grid[0][i]!=null && grid[0][i]==grid[1][i] && grid[1][i]==grid[2][i]){
            return [true, grid[0][i]]
        }
    }
    if(grid[0][0]!=null && grid[0][0]==grid[1][1] && grid[1][1]==grid[2][2]){
        return [true, grid[0][0]]
    }

    if(grid[2][0]!=null && grid[0][0]==grid[1][1] && grid[1][1]==grid[0][2]){
        return [true, grid[0][0]]
    }

    return [false, null]
    

}

function editBoard(col, row, string, turn, val, id){
    // console.log(id)
    grid[row][col] = val;
    document.getElementById(id).innerHTML = string;
    document.getElementById('turn').innerHTML = turn;
    state = !state;
}

function resetBoard(){
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            let temp = ((i+1)*10+j+1)
            temp.toString()
            editBoard(j,i,"","Turn: X",null,temp)
        }
    }
}

var elements = document.getElementsByClassName("box");


for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', (e)=>{
        // console.log(e.srcElement.id)
        if(state){
            // console.log('hello')
            var val = 1;
            var string = "X";
            var turn = "Turn: O"
            
        }else{
            var val = 0;
            var string = "O";
            var turn = "Turn: X"
        }
        let col = parseInt(e.srcElement.id[1]-1)
        let row = parseInt(e.srcElement.id[0]-1)

        if(!over && grid[row][col]==null) {
            editBoard(col, row, string, turn, val, e.srcElement.id)
            let result = gameover()
            if(result[0]){
                if(result[1]){
                    var temp = "X"
                }else{
                    var temp = "O"
                }
                alert(temp + " Won!")
            }
            // grid[row][col] = val;
            // document.getElementById(e.srcElement.id).innerHTML = string;
            // document.getElementById('turn').innerHTML = turn;
            // state = !state;
        }
        // e.srcElement.id 

        // console.log(typeof e.srcElement.id)
    });
}
