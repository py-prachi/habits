habits = document.querySelectorAll(".table__row")
console.log(habits)

var markData = function(item) {

// mark  is_done true or false depending on whether is already checked
    fetch('/mark_habit', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'id':item.id, 'is_done': true}),
        }
    ).then(
        (response) => response.json()
    ).then((data) => {
        console.log(data)
        if (data["Status"] == "Success"){
                 cell = item.querySelectorAll(".table__cell")
                for (i=0;i<cell.length; ++i){
                     cell[i].style.textDecoration = 'line-through'
                }
        }
        return data
    })
    .catch((error) => {
        console.error('Error:', error);
    });
};

habits.forEach((item, index) => {

    item.onclick = () => {
        id = item.getAttribute("id")
        markData(item)
    }
})

